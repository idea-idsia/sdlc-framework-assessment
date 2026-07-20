from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/tickets/category-count', methods=['GET'])
def category_count():
    categories = db.session.query(Category).all()

    # Fetch and cluster tickets based on category counts
    # Example logic goes here (fetching data, clustering, etc.)
    category_counts = {}

    return jsonify({"category_counts": category_counts}), 200