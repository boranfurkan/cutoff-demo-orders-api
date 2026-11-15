"""Order intake API used by the warehouse tablets."""
from typing import Optional

from fastapi import Body, FastAPI

app = FastAPI()
ORDERS = []


@app.post("/orders")
def create_order(sku: str = Body(...), qty: Optional[int] = Body(1)):
    """Create an order.

    The tablet app always sends every field and uses JSON null for "not filled in".
    A null quantity means the default of one unit.
    """
    # Map null to the default explicitly instead of relying on the framework
    # to treat a null body field as missing.
    if qty is None:
        qty = 1
    order = {"id": len(ORDERS) + 1, "sku": sku, "qty": qty}
    ORDERS.append(order)
    return order


@app.get("/orders/count")
def count():
    return {"count": len(ORDERS)}
