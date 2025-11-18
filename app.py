from flask import Flask, jsonify, request
import uuid
from datetime import datetime

app = Flask(__name__)

# Sample product data - RESET to original state
products = {
    1: {"id": 1, "name": "Laptop", "price": 999.99, "category": "Electronics"},
    2: {"id": 2, "name": "Book", "price": 29.99, "category": "Education"}
}

# Home endpoint 
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to Product Catalog API",
        "status": "running",
        "endpoints": {
            "home": "/",
            "health": "/health", 
            "all_products": "/products",
            "get_product": "/products/1"
        }
    })

# Health endpoint
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "service": "Product Catalog",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "products": "/products",
            "product_by_id": "/products/<product_id>"
        }
    })

# GET all products
@app.route("/products", methods=["GET"])
def get_products():
    return jsonify({
        "count": len(products),
        "products": products
    })

# GET one product by ID
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    if product_id in products:
        return jsonify(products[product_id])
    return jsonify({"error": "Product not found"}), 404

# POST – Add new product 
@app.route("/products", methods=["POST"])
def add_product():
    data = request.get_json()
    
    # Validation
    if not data or not all(k in data for k in ['name', 'price', 'category']):
        return jsonify({"error": "Missing required fields: name, price, category"}), 400
    
    try:
        price = float(data['price'])
    except ValueError:
        return jsonify({"error": "Price must be a number"}), 400
    
    # Create new product
    new_id = max(products.keys()) + 1
    new_product = {
        "id": new_id,
        "name": data['name'],
        "price": price,
        "category": data['category']
    }
    products[new_id] = new_product
    return jsonify(new_product), 201  # Returns the PRODUCT, not a message

# PUT – Update product 
@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    if product_id not in products:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Update only provided fields
    if 'name' in data:
        products[product_id]['name'] = data['name']
    if 'price' in data:
        try:
            products[product_id]['price'] = float(data['price'])
        except ValueError:
            return jsonify({"error": "Price must be a number"}), 400
    if 'category' in data:
        products[product_id]['category'] = data['category']
    
    return jsonify(products[product_id])  # Returns the PRODUCT, not a message

# DELETE – Remove product
@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    if product_id not in products:
        return jsonify({"error": "Product not found"}), 404

    deleted = products.pop(product_id)
    return jsonify({
        "message": "Product deleted successfully",
        "deleted_product": deleted
    })

# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)