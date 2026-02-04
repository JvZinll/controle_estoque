from datetime import date

from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2)
    barcode: str = Field(..., pattern=r"^\d{6,14}$")
    description: str = Field(..., min_length=5)
    quantity: int | None = Field(default=None, ge=0)
    category: str = Field(..., min_length=2)
    expiry_date: date | None = None
    image_url: str | None = None


class ProductOut(BaseModel):
    id: int
    name: str
    barcode: str

    class Config:
        orm_mode = True
