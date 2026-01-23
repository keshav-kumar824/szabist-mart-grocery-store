import flask
import json
from flask import Flask, request, render_template, redirect, url_for
from pathlib import Path

app = Flask(__name__, static_folder='static', static_url_path='/static')

# Add headers to allow external images
@app.after_request
def add_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Referrer-Policy'] = 'no-referrer-when-downgrade'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# Global products data
products = []

def load_products():
    """Load products from JSON file into global products list"""
    global products
    with open('products.json', 'r') as f:
        products = json.load(f)

def save_products():
    """Save products to JSON file"""
    with open('products.json', 'w') as f:
        json.dump(products, f, indent=2)

# Initialize products data on startup
load_products()

# ================== HOME PAGE ==================
@app.route("/")
def index():
    return render_template('index.html', products=products)

# ================== PRODUCTS PAGE ==================
@app.route("/products")
def products_page():
    return render_template('products.html', products=products)

# ================== PRODUCT DETAIL PAGE ==================
@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = None
    for p in products:
        if p['product_id'] == product_id:
            product = p
            break
    
    if product is None:
        return "Product not found", 404
    
    return render_template('product_detail.html', product=product)

# ================== ABOUT & CONTACT PAGE ==================
@app.route("/about")
def about():
    return render_template('about_contact.html')

# ================== SEARCH API ==================
@app.route("/api/search", methods=['POST'])
def search_products():
    """Search products by name, category, or description"""
    data = request.get_json()
    query = data.get('query', '').lower()
    
    if not query:
        return flask.jsonify(products)
    
    filtered = [
        p for p in products
        if query in p['name'].lower() 
        or query in p['category'].lower()
        or query in p['description'].lower()
    ]
    
    return flask.jsonify(filtered)

# ================== UPDATE STOCK ==================
@app.route("/update/<int:product_id>", methods=['POST'])
def update_product(product_id):
    """Update product quantity/stock"""
    data = request.get_json()
    new_stock = int(data.get('stock', 0))
    
    for product in products:
        if product['product_id'] == product_id:
            product['stock'] = new_stock
            save_products()
            return flask.jsonify({
                "message": "Product updated successfully",
                "product": product
            }), 200
    
    return flask.jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

