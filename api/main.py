"""Order intake API used by the warehouse tablets."""
from fastapi import Body, FastAPI

app = FastAPI()
ORDERS = []


@app.post("/orders")
def create_order(sku: str = Body(...), qty: int = Body(1)):
    """Create an order.

    The tablet app always sends every field and uses JSON null for "not filled in".
    A null quantity means the default of one unit.
    """
    order = {"id": len(ORDERS) + 1, "sku": sku, "qty": qty}
    ORDERS.append(order)
    return order


@app.get("/orders/count")
def count():
    return {"count": len(ORDERS)}
