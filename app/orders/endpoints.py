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


@router.get("/order/detail/{id}")
async def get_order(id: str, db: Session = Depends(get_db)):
    service = OrderService()
    order = service.get_order_by_id(db, id)

    return order
