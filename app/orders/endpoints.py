from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from .schemas import OrderPOST
from .services import OrderService

router = APIRouter()


@router.post("/order/save/")
async def create_order(order: OrderPOST, db: Session = Depends(get_db)):
    order_service = OrderService()
    order = order_service.create_order(db, order)

    return order
