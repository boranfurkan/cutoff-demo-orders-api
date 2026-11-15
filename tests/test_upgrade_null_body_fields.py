from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_null_quantity_means_default_of_one():
    r = client.post("/orders", json={"sku": "AB1", "qty": None})
    assert r.status_code == 200, r.text
    assert r.json()["qty"] == 1


def test_explicit_quantity_still_respected():
    r = client.post("/orders", json={"sku": "AB1", "qty": 5})
    assert r.status_code == 200 and r.json()["qty"] == 5


def test_null_sku_rejected():
    assert client.post("/orders", json={"sku": None, "qty": 2}).status_code == 422
