from app.models.product import Product  # noqa: F401
from app.schemas.product import ProductCreate, ProductOut
from typing import List 
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import Base, engine
from app.core.deps import get_db
from app.models.supplier import Supplier
from app.schemas.supplier import SupplierCreate, SupplierOut


app = FastAPI(title="Controle de Estoque")

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/suppliers", status_code=status.HTTP_201_CREATED)
def create_supplier(payload: SupplierCreate, db: Session = Depends(get_db)):
    # 1) Verificar se já existe CNPJ
    existing = db.query(Supplier).filter(Supplier.cnpj == payload.cnpj).first()
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Fornecedor com esse CNPJ já está cadastrado!"
        )

    # 2) Criar e salvar
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

    return {
        "message": "Fornecedor cadastrado com sucesso!",
        "id": supplier.id
    }

@app.get("/suppliers", response_model=List[SupplierOut])
def list_suppliers(db: Session = Depends(get_db)):
    suppliers = db.query(Supplier).all()
    return suppliers

@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(payload: ProductCreate, db: Session = Depends(get_db)):
    if payload.barcode:
        existing = db.query(Product).filter(Product.barcode == payload.barcode).first()
        if existing:
            raise HTTPException(
                status_code=400,
                detail="Produto com este código de barras já está cadastrado!"
            )

    product = Product(
        name=payload.name,
        barcode=payload.barcode,
        description=payload.description,
        quantity=payload.quantity,
        category=payload.category,
        expiration_date=payload.expiration_date,
        image_url=payload.image_url,
    )
    db.add(product)
    db.commit()
    db.refresh(product)

    return {"message": "Produto cadastrado com sucesso!", "id": product.id}

@app.get("/products", response_model=List[ProductOut])
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).order_by(Product.id.desc()).all()
