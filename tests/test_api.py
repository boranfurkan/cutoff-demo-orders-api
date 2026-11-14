from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_create_with_quantity():
    r = client.post("/orders", json={"sku": "AB1", "qty": 3})
    assert r.status_code == 200 and r.json()["qty"] == 3


def test_quantity_defaults_when_omitted():
    r = client.post("/orders", json={"sku": "AB1"})
    assert r.status_code == 200 and r.json()["qty"] == 1


def test_missing_sku_rejected():
    assert client.post("/orders", json={"qty": 2}).status_code == 422


def test_count():
    assert client.get("/orders/count").json()["count"] >= 2
