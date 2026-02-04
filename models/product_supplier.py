from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint

from app.core.database import Base


class ProductSupplier(Base):
    __tablename__ = "product_suppliers"
    __table_args__ = (UniqueConstraint("product_id", "supplier_id", name="uq_product_supplier"),)

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=False)
