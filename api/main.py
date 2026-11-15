"""Order intake API used by the warehouse tablets."""
from typing import Optional

from fastapi import Body, FastAPI

app = FastAPI()
ORDERS = []
DEFAULT_QTY = 1


@app.post("/orders")
def create_order(sku: str = Body(...), qty: Optional[int] = Body(DEFAULT_QTY)):
    """Create an order.

    The tablet app always sends every field and uses JSON null for "not filled in".
    A null quantity means the default of one unit.
    """
    # Explicitly map JSON null to the default rather than relying on the
    # framework to substitute the Body() default for an explicit null.
    if qty is None:
        qty = DEFAULT_QTY
    order = {"id": len(ORDERS) + 1, "sku": sku, "qty": qty}
    ORDERS.append(order)
    return order


@app.get("/orders/count")
def count():
    return {"count": len(ORDERS)}
