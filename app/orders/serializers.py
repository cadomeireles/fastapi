from . import schemas
from .models import Order


class PydanticSerializer:

    def serialize(self, order: Order):
        items = [
            schemas.OrderItemGET(
                product=item.product.name, quantity=item.quantity)
            for item in order.items
        ]

        return schemas.OrderGET(
            id=order.id, client=order.client.name, items=items,
        )
