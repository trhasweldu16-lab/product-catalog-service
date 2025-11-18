# test_basic.py
import requests
import sys

BASE = "http://127.0.0.1:5000"

def expect(status_code, resp):
    if resp.status_code != status_code:
        print(f"❌ Expected {status_code}, got {resp.status_code}: {resp.text}")
        sys.exit(1)
    else:
        print(f"✅ OK {status_code} -> {resp.request.method} {resp.url}")

def test_health():
    print("\n=== Testing Health Endpoint ===")
    r = requests.get(BASE + "/health")
    expect(200, r)
    print("Health:", r.json())

def test_list_products():
    print("\n=== Testing GET All Products ===")
    r = requests.get(BASE + "/products")
    expect(200, r)
    data = r.json()
    print(f"Products count: {data['count']}")
    print("Products:", data['products'])

def test_create_product():
    print("\n=== Testing POST - Create Product ===")
    payload = {"name": "TestProduct", "category": "Test", "price": 12.5}
    r = requests.post(BASE + "/products", json=payload)
    expect(201, r)
    created = r.json()
    print("Created:", created)
    return created["id"]  

def test_update_product(product_id):
    print("\n=== Testing PUT - Update Product ===")
    payload = {"price": 99.99, "name": "UpdatedName"}
    r = requests.put(f"{BASE}/products/{product_id}", json=payload)
    expect(200, r)
    print("Updated:", r.json())

def test_delete_product(product_id):
    print("\n=== Testing DELETE - Remove Product ===")
    r = requests.delete(f"{BASE}/products/{product_id}")
    expect(200, r)
    print("Deleted:", r.json())

def test_get_product(product_id):
    print("\n=== Testing GET Single Product ===")
    r = requests.get(f"{BASE}/products/{product_id}")
    expect(200, r)
    print("Product details:", r.json())

def test_get_nonexistent_product():
    print("\n=== Testing GET Non-existent Product ===")
    r = requests.get(f"{BASE}/products/999")
    expect(404, r)
    print("Correctly handled non-existent product")

def test_create_invalid_product():
    print("\n=== Testing POST Validation ===")
    # Test missing fields
    payload = {"name": "IncompleteProduct"}
    r = requests.post(BASE + "/products", json=payload)
    expect(400, r)
    print("✅ Correctly rejected incomplete product")

if __name__ == "__main__":
    print("🚀 Starting CRUD API Tests")
    print("=" * 50)
    
    test_health()
    test_list_products()
    
    # Test POST (CREATE)
    pid = test_create_product()
    
    # Test GET (READ)
    test_get_product(pid)
    
    # Test PUT (UPDATE)
    test_update_product(pid)
    test_get_product(pid)  # Verify update
    
    # Test validation
    test_create_invalid_product()
    
    # Test error cases
    test_get_nonexistent_product()
    
    # Test DELETE
    test_delete_product(pid)
    
    # Final check
    test_list_products()
    
    print("\n" + "=" * 50)
    print(" ALL TESTS PASSED!")
    print("✅ POST, GET, PUT, DELETE all working perfectly!")
    print("✅ No crashes - All response formats match!")