def test_create_supplier(client):
    response = client.post("/suppliers", json={
        "company_name": "Fornecedor Teste",
        "cnpj": "12.345.678/0001-99",
        "address": "Rua das Flores, 123",
        "phone": "86999999999",
        "email": "contato@fornecedor.com",
        "main_contact": "João Silva"
    })
    assert response.status_code == 201
    assert response.json()["message"] == "Fornecedor cadastrado com sucesso!"


def test_create_supplier_duplicate_cnpj(client):
    payload = {
        "company_name": "Fornecedor Teste",
        "cnpj": "12.345.678/0001-99",
        "address": "Rua das Flores, 123",
        "phone": "86999999999",
        "email": "contato@fornecedor.com",
        "main_contact": "João Silva"
    }
    client.post("/suppliers", json=payload)
    response = client.post("/suppliers", json=payload)
    assert response.status_code == 400
    assert "CNPJ" in response.json()["detail"]


def test_list_suppliers(client):
    client.post("/suppliers", json={
        "company_name": "Fornecedor Teste",
        "cnpj": "12.345.678/0001-99",
        "address": "Rua das Flores, 123",
        "phone": "86999999999",
        "email": "contato@fornecedor.com",
        "main_contact": "João Silva"
    })
    response = client.get("/suppliers")
    assert response.status_code == 200
    assert len(response.json()) == 1