import datetime
import uuid

from sqlalchemy import (
    Column, String, Numeric, SmallInteger, ForeignKey, DateTime)
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship


from app.database import Base


class Client(Base):

    __tablename__ = "clients"

    id = Column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String(length=80), index=True)
    cpf = Column(String(length=11), index=True)
    phone = Column(String(length=12), unique=True)


class Product(Base):

    __tablename__ = "products"

    id = Column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String(length=80), index=True)
    price = Column(Numeric(precision=8, scale=2))
    weight = Column(Numeric(precision=8, scale=2))
    volume = Column(Numeric(precision=8, scale=2))


class OrderItem(Base):

    __tablename__ = "order_items"

    id = Column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    product_id = Column(UUID, ForeignKey("products.id"))
    order_id = Column(UUID, ForeignKey("orders.id"))
    quantity = Column(SmallInteger())
    unit_price = Column(Numeric(precision=8, scale=2))
    total_price = Column(Numeric(precision=8, scale=2))
    unit_weight = Column(Numeric(precision=8, scale=2))
    total_weight = Column(Numeric(precision=8, scale=2))
    unit_volume = Column(Numeric(precision=8, scale=2))
    total_volume = Column(Numeric(precision=8, scale=2))

    product = relationship("Product", lazy="joined")


class Order(Base):

    __tablename__ = "orders"

    id = Column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    created_at = Column(DateTime(), default=datetime.datetime.utcnow)
    client_id = Column(UUID, ForeignKey("clients.id"))
    total_price = Column(Numeric(precision=8, scale=2), default=0)
    total_weight = Column(Numeric(precision=8, scale=2), default=0)
    total_volume = Column(Numeric(precision=8, scale=2), default=0)

    client = relationship("Client", lazy="joined")
    items = relationship(
        "OrderItem", lazy="joined", cascade='all, delete-orphan')
