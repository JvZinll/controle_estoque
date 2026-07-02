from pydantic import BaseModel, EmailStr        
from typing import Optional

class SupplierCreate(BaseModel):
    company_name: str
    cnpj: str
    address: str
    phone: str
    email: EmailStr
    main_contact: str

class SupplierOut(BaseModel):
    id: int
    company_name: str
    cnpj: str
    address: str
    phone: str
    email: EmailStr
    main_contact: str

    class Config:
        from_attributes = True  

class SupplierUpdate(BaseModel):
    company_name: Optional[str] = None
    cnpj: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    main_contact: Optional[str] = None
