from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    barcode = Column(String, unique=True, index=True, nullable=True)
    description = Column(Text, nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    category = Column(String, nullable=False)
    expiration_date = Column(String, nullable=True)   # depois melhoramos para Date
    image_url = Column(String, nullable=True)
