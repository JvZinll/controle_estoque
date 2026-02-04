from fastapi import FastAPI

from app.core.database import Base, engine
from app.models.supplier import Supplier  # noqa: F401

app = FastAPI(title="Controle de Estoque")

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}
    