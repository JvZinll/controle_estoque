def test_create_product(client):
    response = client.post("/products", json={
        "name": "Arroz 5kg",
        "barcode": "7891234560001",
        "description": "Arroz branco tipo 1",
        "quantity": 100,
        "category": "Alimentos",
        "expiration_date": "2026-12-31",
        "image_url": None
    })
    assert response.status_code == 201
    assert response.json()["message"] == "Produto cadastrado com sucesso!"


def test_create_product_duplicate_barcode(client):
    payload = {
        "name": "Arroz 5kg",
        "barcode": "7891234560001",
        "description": "Arroz branco tipo 1",
        "quantity": 100,
        "category": "Alimentos",
        "expiration_date": "2026-12-31",
        "image_url": None
    }
    client.post("/products", json=payload)
    response = client.post("/products", json=payload)
    assert response.status_code == 400
    assert "barras" in response.json()["detail"]


def test_list_products(client):
    client.post("/products", json={
        "name": "Arroz 5kg",
        "barcode": "7891234560001",
        "description": "Arroz branco tipo 1",
        "quantity": 100,
        "category": "Alimentos",
        "expiration_date": "2026-12-31",
        "image_url": None
    })
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_add_supplier_to_product(client):
    client.post("/suppliers", json={
        "company_name": "Fornecedor Teste",
        "cnpj": "12.345.678/0001-99",
        "address": "Rua das Flores, 123",
        "phone": "86999999999",
        "email": "contato@fornecedor.com",
        "main_contact": "João Silva"
    })
    client.post("/products", json={
        "name": "Arroz 5kg",
        "barcode": "7891234560001",
        "description": "Arroz branco tipo 1",
        "quantity": 100,
        "category": "Alimentos",
        "expiration_date": "2026-12-31",
        "image_url": None
    })
    response = client.post("/products/1/suppliers/1")
    assert response.status_code == 201
    assert response.json()["message"] == "Fornecedor associado ao produto com sucesso!"


def test_list_suppliers_of_product(client):
    client.post("/suppliers", json={
        "company_name": "Fornecedor Teste",
        "cnpj": "12.345.678/0001-99",
        "address": "Rua das Flores, 123",
        "phone": "86999999999",
        "email": "contato@fornecedor.com",
        "main_contact": "João Silva"
    })
    client.post("/products", json={
        "name": "Arroz 5kg",
        "barcode": "7891234560001",
        "description": "Arroz branco tipo 1",
        "quantity": 100,
        "category": "Alimentos",
        "expiration_date": "2026-12-31",
        "image_url": None
    })
    client.post("/products/1/suppliers/1")
    response = client.get("/products/1/suppliers")
    assert response.status_code == 200
    assert len(response.json()) == 1