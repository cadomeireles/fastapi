from typing import List

from pydantic import UUID4, BaseModel


class OrderItemGET(BaseModel):
    product: str
    quantity: int

    class Config:
        orm_mode = True


class OrderGET(BaseModel):
    id: UUID4
    client: str
    items: List[OrderItemGET]

    class Config:
        orm_mode = True


class OrderItemPOST(BaseModel):
    product: str
    quantity: int

    class Config:
        orm_mode = True


class OrderPOST(BaseModel):
    client: str
    items: List[OrderItemPOST]

    class Config:
        orm_mode = True
