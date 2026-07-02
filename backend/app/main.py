from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine
from app.models import product, supplier, product_supplier  # noqa: F401
from app.routers import product as product_router
from app.routers import supplier as supplier_router

app = FastAPI(title="Controle de Estoque")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(supplier_router.router)
app.include_router(product_router.router)

@app.get("/health")
def health():
    return {"status": "ok"}