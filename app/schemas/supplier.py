from pydantic import BaseModel, EmailStr, Field


class SupplierCreate(BaseModel):
    company_name: str = Field(..., min_length=2)
    cnpj: str = Field(..., pattern=r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$")
    address: str = Field(..., min_length=5)
    phone: str = Field(..., pattern=r"^\(\d{2}\) \d{4,5}-\d{4}$")
    email: EmailStr
    main_contact: str = Field(..., min_length=2)
    notes: str | None = None


class SupplierOut(BaseModel):
    id: int
    company_name: str
    cnpj: str

    class Config:
        orm_mode = True
