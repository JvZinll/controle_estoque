from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    barcode = Column(String, nullable=False, unique=True, index=True)
    description = Column(String, nullable=False)
    quantity = Column(Integer, nullable=True)
    category = Column(String, nullable=False)
    expiry_date = Column(Date, nullable=True)
    image_url = Column(String, nullable=True)

    suppliers = relationship(
        "Supplier",
        secondary="product_suppliers",
        back_populates="products",
    )
