import os
import json
import time
from playwright.sync_api import sync_playwright
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

fallback_selectors = {
    "review": ".review",
    "title": ".review-title",
    "body": ".review-body",
    "rating": ".review-rating",
    "reviewer": ".reviewer",
    "next_page": ".pagination-next"
}

def retry_openai(prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return json.loads(response['choices'][0]['message']['content'])
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
            else:
                raise e

def detect_css_selectors(html_content):
    prompt = f"""
    Analyze the following HTML and suggest JSON with CSS selectors for:
    1. Review container
    2. Review title
    3. Review body
    4. Review rating
    5. Reviewer name
    6. Next page button
    
    HTML:
    {html_content[:2000]}  

    Return the result in JSON format.
    """
    try:
        return retry_openai(prompt)
    except Exception as e:
        print(f"Error detecting CSS selectors: {e}. Using fallback selectors.")
        return fallback_selectors

def extract_reviews_from_page(url):
    reviews = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        html_content = page.content()
        css_selectors = detect_css_selectors(html_content)

        while True:
            review_elements = page.query_selector_all(css_selectors.get("review", ".review"))
            for element in review_elements:
                title = element.query_selector(css_selectors.get("title", ".review-title"))
                body = element.query_selector(css_selectors.get("body", ".review-body"))
                rating = element.query_selector(css_selectors.get("rating", ".review-rating"))
                reviewer = element.query_selector(css_selectors.get("reviewer", ".reviewer"))

                reviews.append({
                    "title": title.inner_text() if title else "No Title",
                    "body": body.inner_text() if body else "No Body",
                    "rating": rating.inner_text() if rating else "No Rating",
                    "reviewer": reviewer.inner_text() if reviewer else "Anonymous"
                })

            next_button = page.query_selector(css_selectors.get("next_page", ".pagination-next"))
            if next_button:
                next_button.click()
                time.sleep(2)  
            else:
                break

        browser.close()
    return reviews
