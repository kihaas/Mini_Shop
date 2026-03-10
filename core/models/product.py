from sqlalchemy.orm import Mapped

from .base import Base


class Product(Base):
    __tablename__ = "products"

    name: Mapped[str]  # mapped чтобы скaзать что это колонки
    description: Mapped[str]
    price: Mapped[int]


# .
