# 📦 Controle de Estoque

API REST fullstack para controle de estoque com cadastro de produtos, fornecedores e associação entre eles.

Desenvolvido como projeto acadêmico utilizando Python, FastAPI e JavaScript puro.

---

## 🚀 Tecnologias utilizadas

**Backend**
- Python 3.13
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Pytest

**Frontend**
- HTML5
- CSS3
- JavaScript (Fetch API)

---

## 📁 Estrutura do projeto

```
controle_estoque/
├── app/
│   ├── main.py
│   ├── core/
│   │   ├── database.py
│   │   └── deps.py
│   ├── models/
│   │   ├── product.py
│   │   ├── supplier.py
│   │   └── product_supplier.py
│   ├── schemas/
│   │   ├── product.py
│   │   └── supplier.py
│   ├── routers/
│   │   ├── product.py
│   │   └── supplier.py
│   └── services/
│       ├── product.py
│       └── supplier.py
├── frontend/
│   └── index.html
├── tests/
│   ├── conftest.py
│   ├── test_product.py
│   └── test_supplier.py
├── estoque.db
└── README.md
```

---

## ⚙️ Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/controle-estoque.git
cd controle-estoque
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install fastapi uvicorn sqlalchemy pydantic[email] pytest httpx
```

### 4. Rode o servidor

```bash
uvicorn app.main:app --reload
```

### 5. Abra o frontend

Abra o arquivo `frontend/index.html` diretamente no navegador.

### 6. Acesse a documentação da API

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Rodando os testes

```bash
pytest tests/ -v
```

Resultado esperado: **8 testes passando**

---

## 📌 Rotas da API

### Health Check
| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/health` | Verifica se a API está rodando |

### Fornecedores
| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/suppliers` | Lista todos os fornecedores |
| POST | `/suppliers` | Cadastra um fornecedor |
| PUT | `/suppliers/{id}` | Atualiza um fornecedor |
| DELETE | `/suppliers/{id}` | Deleta um fornecedor |

### Produtos
| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/products` | Lista todos os produtos |
| POST | `/products` | Cadastra um produto |
| PUT | `/products/{id}` | Atualiza um produto |
| DELETE | `/products/{id}` | Deleta um produto |

### Associação Produto ↔ Fornecedor
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/products/{id}/suppliers/{id}` | Associa fornecedor ao produto |
| DELETE | `/products/{id}/suppliers/{id}` | Remove associação |
| GET | `/products/{id}/suppliers` | Lista fornecedores do produto |

---

## 📝 Exemplos de uso

### Criar fornecedor
```json
POST /suppliers
{
  "company_name": "Fornecedor Exemplo",
  "cnpj": "12.345.678/0001-99",
  "address": "Rua das Flores, 123",
  "phone": "86999999999",
  "email": "contato@fornecedor.com",
  "main_contact": "João Silva"
}
```

### Criar produto
```json
POST /products
{
  "name": "Arroz 5kg",
  "barcode": "7891234560001",
  "description": "Arroz branco tipo 1",
  "quantity": 100,
  "category": "Alimentos",
  "expiration_date": "2026-12-31"
}
```

---

## 👨‍💻 Autor

Desenvolvido por João — Projeto acadêmico de desenvolvimento backend com FastAPI.