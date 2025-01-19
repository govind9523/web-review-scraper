from flask import Flask, request, jsonify, render_template
from reviews_extractor import extract_reviews_from_page
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    url = request.args.get('page')
    if not url:
        return jsonify({"error": "Missing 'page' query parameter"}), 400

    try:
        reviews = extract_reviews_from_page(url)
        return jsonify({
            "reviews_count": len(reviews),
            "reviews": reviews
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


app.run()
