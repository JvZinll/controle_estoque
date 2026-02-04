from pydantic import BaseModel, EmailStr

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
