from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    barcode: Optional[str] = None
    description: str
    quantity: int = 0
    category: str
    expiration_date: Optional[str] = None
    image_url: Optional[str] = None

class ProductOut(ProductCreate):
    id: int

    class Config:
        from_attributes = True
