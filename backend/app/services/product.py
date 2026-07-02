from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.product import Product
from app.models.supplier import Supplier
from app.models.product_supplier import ProductSupplier
from app.schemas.product import ProductCreate, ProductUpdate


def create_product(db: Session, payload: ProductCreate) -> Product:
    if payload.barcode:
        existing = db.query(Product).filter(Product.barcode == payload.barcode).first()
        if existing:
            raise HTTPException(status_code=400, detail="Produto com este código de barras já está cadastrado!")

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
    return product


def list_products(db: Session) -> list[Product]:
    return db.query(Product).order_by(Product.id.desc()).all()


def add_supplier_to_product(db: Session, product_id: int, supplier_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado!")

    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    if not supplier:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado!")

    existing = db.query(ProductSupplier).filter(
        ProductSupplier.product_id == product_id,
        ProductSupplier.supplier_id == supplier_id
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Associação já existe!")

    association = ProductSupplier(product_id=product_id, supplier_id=supplier_id)
    db.add(association)
    db.commit()


def remove_supplier_from_product(db: Session, product_id: int, supplier_id: int):
    association = db.query(ProductSupplier).filter(
        ProductSupplier.product_id == product_id,
        ProductSupplier.supplier_id == supplier_id
    ).first()
    if not association:
        raise HTTPException(status_code=404, detail="Associação não encontrada!")

    db.delete(association)
    db.commit()


def list_suppliers_of_product(db: Session, product_id: int) -> list[Supplier]:
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado!")

    associations = db.query(ProductSupplier).filter(
        ProductSupplier.product_id == product_id
    ).all()

    supplier_ids = [a.supplier_id for a in associations]
    return db.query(Supplier).filter(Supplier.id.in_(supplier_ids)).all()
def update_product(db: Session, product_id: int, payload: ProductUpdate) -> Product:
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado!")

    if payload.name is not None:
        product.name = payload.name
    if payload.barcode is not None:
        existing = db.query(Product).filter(
            Product.barcode == payload.barcode,
            Product.id != product_id
        ).first()
        if existing:
            raise HTTPException(status_code=400, detail="Código de barras já está em uso!")
        product.barcode = payload.barcode
    if payload.description is not None:
        product.description = payload.description
    if payload.quantity is not None:
        product.quantity = payload.quantity
    if payload.category is not None:
        product.category = payload.category
    if payload.expiration_date is not None:
        product.expiration_date = payload.expiration_date
    if payload.image_url is not None:
        product.image_url = payload.image_url

    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado!")

    db.delete(product)
    db.commit()