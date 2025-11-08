import requests

BASE_URL = "https://product-catalog-service.onrender.com"

def test_health():
    r = requests.get(f"{BASE_URL}/health")
    assert r.status_code == 200
    print("✅ Health endpoint OK")

def test_products():
    r = requests.get(f"{BASE_URL}/products")
    assert r.status_code == 200
    data = r.json()
    assert "products" in data
    print("✅ Products endpoint OK")

if __name__ == "__main__":
    test_health()
    test_products()
    print("🎉 All tests passed successfully!")
