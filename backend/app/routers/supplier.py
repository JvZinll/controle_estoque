from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.schemas.supplier import SupplierCreate, SupplierOut, SupplierUpdate

from app.core.deps import get_db
from app.schemas.supplier import SupplierCreate, SupplierOut
from app.services import supplier as supplier_service

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])


@router.post("", status_code=status.HTTP_201_CREATED)
def create_supplier(payload: SupplierCreate, db: Session = Depends(get_db)):
    supplier = supplier_service.create_supplier(db, payload)
    return {"message": "Fornecedor cadastrado com sucesso!", "id": supplier.id}


@router.get("", response_model=List[SupplierOut])
def list_suppliers(db: Session = Depends(get_db)):
    return supplier_service.list_suppliers(db)

@router.put("/{supplier_id}", response_model=SupplierOut)
def update_supplier(supplier_id: int, payload: SupplierUpdate, db: Session = Depends(get_db)):
    return supplier_service.update_supplier(db, supplier_id, payload)

@router.delete("/{supplier_id}", status_code=status.HTTP_200_OK)
def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    supplier_service.delete_supplier(db, supplier_id)
    return {"message": "Fornecedor deletado com sucesso!"}