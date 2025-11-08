from flask import Flask, jsonify, request
import uuid
from datetime import datetime

app = Flask(__name__)

# In-memory products (simple sample data)
products = [
    {"id": "1", "name": "Laptop", "category": "Electronics", "price": 999.99, "in_stock": True},
    {"id": "2", "name": "Book",   "category": "Education",   "price": 29.99,  "in_stock": True},
]

@app.route("/")
def home():
    return jsonify({
        "service": "Product Catalog",
        "version": "1.0.0",
        "endpoints": {
            "products": "/products",
            "product_by_id": "/products/<product_id>",
            "health": "/health"
        }
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "product-catalog", "timestamp": str(datetime.utcnow())})

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify({"products": products, "count": len(products)})

@app.route("/products/<product_id>", methods=["GET"])
def get_product(product_id):
    for p in products:
        if p["id"] == product_id:
            return jsonify(p)
    return jsonify({"error": "Product not found"}), 404

# optional: create a product (simple)
@app.route("/products", methods=["POST"])
def create_product():
    data = request.get_json() or {}
    if "name" not in data or "price" not in data:
        return jsonify({"error": "Missing name or price"}), 400
    new_id = str(uuid.uuid4())[:8]
    p = {
        "id": new_id,
        "name": data["name"],
        "category": data.get("category", "Misc"),
        "price": float(data["price"]),
        "in_stock": bool(data.get("in_stock", True)),
        "created_at": str(datetime.utcnow())
    }
    products.append(p)
    return jsonify({"message": "Product created", "product": p}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
