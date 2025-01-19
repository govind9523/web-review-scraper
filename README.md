
```markdown
# Web Review Scraper

## 📖 Introduction

**Web Review Scraper** is a Python-based tool for web scraping, designed to dynamically extract reviews from any product webpage. By utilizing OpenAI's LLM (Large Language Model), the scraper intelligently identifies CSS selectors, making it adaptable to different website structures. The tool is integrated into a Flask web application, providing an easy-to-use interface where users can input a URL and view extracted reviews effortlessly.

---

## 📋 Table of Contents

- [Introduction](#📖-introduction)
- [Features](#🧐-features)
- [Built With](#💻-built-with)
- [Installation](#🚀-installation)
- [Usage](#📖-usage)
- [Configuration](#⚙️-configuration)
- [Examples](#🌟-examples)
- [Troubleshooting](#🛠-troubleshooting)

---

## 🧐 Features

Here are some of the top features of the project:

- **Dynamic CSS Selector Detection**: Uses OpenAI's LLM to dynamically identify suitable CSS selectors on webpages.
- **Pagination Support**: Extracts reviews seamlessly across multiple pages.
- **Flask Frontend**: Provides an intuitive web interface for entering URLs and viewing reviews.

---

## 💻 Built With

This project has been developed using the following technologies:

- **Python**: Core programming language for backend functionality.
- **Flask**: Framework for developing the web application's frontend.
- **Playwright**: For reliable and efficient browser automation.
- **OpenAI GPT-3.5**: To dynamically analyze and identify CSS selectors.

---

## 🚀 Installation

Follow these steps to set up the project on your local system:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/govind9523/web-review-scraper.git
   cd web-review-scraper


2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright**:
   ```bash
   playwright install
   ```

---

## 📖 Usage

1. **Run the Flask App**:
   ```bash
   python app.py
   ```

2. **Access the Application**:
   Open your browser and visit `http://127.0.0.1:5000`.

3. **Scrape Reviews**:
   - Enter the URL of a product page in the input field.
   - View the extracted reviews on the interface.

---

## ⚙️ Configuration

- **API Key**: Ensure your OpenAI API key is set in the environment variables:
  ```bash
  export OPENAI_API_KEY=your_api_key
  ```
- **Playwright Setup**: Make sure Playwright browsers are correctly installed using the command `playwright install`.

---

## 🌟 Examples

1. **Input**: A product page URL.
2. **Output**: A list of reviews displayed on the web interface.

---

## 🛠 Troubleshooting

- **Issue**: "Playwright is not installed or functioning properly."
  - **Solution**: Run `playwright install` to ensure all required browsers are installed.

- **Issue**: "OpenAI API key is missing."
  - **Solution**: Verify that the environment variable `OPENAI_API_KEY` is set correctly.

---

```

