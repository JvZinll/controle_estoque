from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.supplier import Supplier
from app.schemas.supplier import SupplierCreate, SupplierUpdate


def create_supplier(db: Session, payload: SupplierCreate) -> Supplier:
    existing = db.query(Supplier).filter(Supplier.cnpj == payload.cnpj).first()
    if existing:
        raise HTTPException(status_code=400, detail="Fornecedor com esse CNPJ já está cadastrado!")

    supplier = Supplier(
        company_name=payload.company_name,
        cnpj=payload.cnpj,
        address=payload.address,
        phone=payload.phone,
        email=str(payload.email),
        main_contact=payload.main_contact,
    )
    db.add(supplier)
    db.commit()
    db.refresh(supplier)
    return supplier


def list_suppliers(db: Session) -> list[Supplier]:
    return db.query(Supplier).all()

def update_supplier(db: Session, supplier_id: int, payload: SupplierUpdate) -> Supplier:
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    if not supplier:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado!")

    if payload.company_name is not None:
        supplier.company_name = payload.company_name
    if payload.cnpj is not None:
        existing = db.query(Supplier).filter(
            Supplier.cnpj == payload.cnpj,
            Supplier.id != supplier_id
        ).first()
        if existing:
            raise HTTPException(status_code=400, detail="CNPJ já está em uso por outro fornecedor!")
        supplier.cnpj = payload.cnpj
    if payload.address is not None:
        supplier.address = payload.address
    if payload.phone is not None:
        supplier.phone = payload.phone
    if payload.email is not None:
        supplier.email = str(payload.email)
    if payload.main_contact is not None:
        supplier.main_contact = payload.main_contact

    db.commit()
    db.refresh(supplier)
    return supplier

def delete_supplier(db: Session, supplier_id: int):
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    if not supplier:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado!")

    db.delete(supplier)
    db.commit()