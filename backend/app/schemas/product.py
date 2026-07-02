from pydantic import BaseModel
from typing import Optional
from datetime import date

class ProductCreate(BaseModel):
    name: str
    barcode: Optional[str] = None
    description: str
    quantity: int = 0
    category: str
    expiration_date: Optional[str] = None
    expiration_date: Optional[date] = None  
    image_url: Optional[str] = None

class ProductOut(ProductCreate):
    id: int

    class Config:
        from_attributes = True
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    barcode: Optional[str] = None
    description: Optional[str] = None
    quantity: Optional[int] = None
    category: Optional[str] = None
    expiration_date: Optional[date] = None
    image_url: Optional[str] = None
