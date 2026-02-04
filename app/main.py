from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import Base, engine, get_db
from app.models.product import Product
from app.models.product_supplier import ProductSupplier
from app.models.supplier import Supplier
from app.schemas.product import ProductCreate, ProductOut
from app.schemas.supplier import SupplierCreate, SupplierOut

app = FastAPI(title="Controle de Estoque")

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/suppliers", response_model=SupplierOut, status_code=status.HTTP_201_CREATED)
def create_supplier(payload: SupplierCreate, db: Session = Depends(get_db)):
    existing_supplier = db.query(Supplier).filter(Supplier.cnpj == payload.cnpj).first()
    if existing_supplier:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Fornecedor com esse CNPJ já está cadastrado!",
        )
    supplier = Supplier(**payload.dict())
    db.add(supplier)
    db.commit()
    db.refresh(supplier)
    return supplier


@app.post("/products", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
def create_product(payload: ProductCreate, db: Session = Depends(get_db)):
    existing_product = db.query(Product).filter(Product.barcode == payload.barcode).first()
    if existing_product:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Produto com este código de barras já está cadastrado!",
        )
    product = Product(**payload.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


@app.post(
    "/products/{product_id}/suppliers/{supplier_id}",
    status_code=status.HTTP_201_CREATED,
)
def associate_supplier(product_id: int, supplier_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado.")
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    if not supplier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fornecedor não encontrado.")

    existing_link = (
        db.query(ProductSupplier)
        .filter(
            ProductSupplier.product_id == product_id,
            ProductSupplier.supplier_id == supplier_id,
        )
        .first()
    )
    if existing_link:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Fornecedor já está associado a este produto!",
        )
    association = ProductSupplier(product_id=product_id, supplier_id=supplier_id)
    db.add(association)
    db.commit()
    return {"message": "Fornecedor associado com sucesso ao produto!"}


@app.delete("/products/{product_id}/suppliers/{supplier_id}")
def disassociate_supplier(product_id: int, supplier_id: int, db: Session = Depends(get_db)):
    association = (
        db.query(ProductSupplier)
        .filter(
            ProductSupplier.product_id == product_id,
            ProductSupplier.supplier_id == supplier_id,
        )
        .first()
    )
    if not association:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Fornecedor não está associado a este produto.",
        )
    db.delete(association)
    db.commit()
    return {"message": "Fornecedor desassociado com sucesso!"}
    
