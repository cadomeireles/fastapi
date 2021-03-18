from typing import List

from sqlalchemy.orm import Session

from app.services import QueryService
from . import models
from . import schemas
from . import serializers


class OrderService:

    def __init__(self):
        self.query_service = QueryService()
        self.serializer = serializers.PydanticSerializer()

    def get_order_by_id(self, db: Session, id: str):
        order = self.query_service.get_by_id(db, models.Order, id)

        return self.serializer.serialize(order)

    def create_order(self, db: Session, data: schemas.OrderPOST):
        order = models.Order()
        order.client_id = data.client

        new_order = self.query_service.save(db, order)
        self.__save_order_items(db, new_order, data.items)
        self.__calculate_totals(db, new_order)

        return self.serializer.serialize(new_order)

    def __save_order_items(
        self, db: Session, order: models.Order,
        items_data: List[schemas.OrderItemPOST]
    ):
        items = []

        for item_data in items_data:
            item = models.OrderItem()
            product = self.query_service.get_by_id(
                db, models.Product, item_data.product)

            item.product_id = str(product.id)
            item.order_id = str(order.id)
            item.quantity = item_data.quantity

            self.__calculate_item_totals(item, product)

            items.append(item)

        self.query_service.bulk_save(db, items)

    def __calculate_item_totals(
            self, item: models.OrderItem, product: models.Product):
        item.unit_price = product.price
        item.total_price = product.price * item.quantity
        item.unit_weight = product.weight
        item.total_weight = product.weight * item.quantity
        item.unit_volume = product.volume
        item.total_volume = product.volume * item.quantity

    def __calculate_totals(self, db: Session, order: models.Order):
        for item in order.items:
            order.total_price += item.total_price
            order.total_weight += item.total_weight
            order.total_volume += item.total_volume

        self.query_service.update(db)
