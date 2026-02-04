from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    cnpj = Column(String, nullable=False, unique=True, index=True)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    main_contact = Column(String, nullable=False)
    notes = Column(String, nullable=True)   