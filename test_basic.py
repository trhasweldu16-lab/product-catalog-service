import requests

BASE = "http://127.0.0.1:5000"

def test_health():
    r = requests.get(f"{BASE}/health")
    assert r.status_code == 200
    assert "healthy" in r.json().get("status", "")

def test_products_list():
    r = requests.get(f"{BASE}/products")
    assert r.status_code == 200
    data = r.json()
    assert "products" in data

if __name__ == "__main__":
    test_health()
    test_products_list()
    print("Basic tests passed.")
