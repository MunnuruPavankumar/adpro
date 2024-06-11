from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import scrape_amazon, scrape_flipkart

app = Flask(__name__)
CORS(app)

@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400
    amazon_results = scrape_amazon(query)
    flipkart_results = scrape_flipkart(query)
    results = {
        "amazon": amazon_results,
        "flipkart": flipkart_results
    }
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
