from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.schemas.product import ProductCreate, ProductOut, ProductUpdate
from app.schemas.supplier import SupplierOut
from app.services import product as product_service

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("", status_code=status.HTTP_201_CREATED)
def create_product(payload: ProductCreate, db: Session = Depends(get_db)):
    product = product_service.create_product(db, payload)
    return {"message": "Produto cadastrado com sucesso!", "id": product.id}


@router.get("", response_model=List[ProductOut])
def list_products(db: Session = Depends(get_db)):
    return product_service.list_products(db)


@router.post("/{product_id}/suppliers/{supplier_id}", status_code=status.HTTP_201_CREATED)
def add_supplier_to_product(product_id: int, supplier_id: int, db: Session = Depends(get_db)):
    product_service.add_supplier_to_product(db, product_id, supplier_id)
    return {"message": "Fornecedor associado ao produto com sucesso!"}


@router.delete("/{product_id}/suppliers/{supplier_id}")
def remove_supplier_from_product(product_id: int, supplier_id: int, db: Session = Depends(get_db)):
    product_service.remove_supplier_from_product(db, product_id, supplier_id)
    return {"message": "Fornecedor desassociado do produto com sucesso!"}


@router.get("/{product_id}/suppliers", response_model=List[SupplierOut])
def list_suppliers_of_product(product_id: int, db: Session = Depends(get_db)):
    return product_service.list_suppliers_of_product(db, product_id)
@router.put("/{product_id}", response_model=ProductOut)
def update_product(product_id: int, payload: ProductUpdate, db: Session = Depends(get_db)):
    return product_service.update_product(db, product_id, payload)


@router.delete("/{product_id}", status_code=status.HTTP_200_OK)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product_service.delete_product(db, product_id)
    return {"message": "Produto deletado com sucesso!"}