import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from models.loan import Prestamo
from app.main import app
from app.database import DATABASE_URL
from starlette.testclient import TestClient

# Configuración de la conexión a MySQL
SQLALCHEMY_DATABASE_URL = DATABASE_URL


# Conexión a la base de datos de prueba
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Configuración de la base de datos para tests
def setup_module(module):
    Loan.metadata.create_all(bind=engine)

def teardown_module(module):
    clear_mappers()

# Fixture para obtener una sesión de prueba
@pytest.fixture
def db_session():
    session = TestingSessionLocal()
    yield session
    session.close()

# Cliente de prueba para ejecutar requests HTTP
@pytest.fixture
def client(db_session):
    def override_get_db():
        return db_session
    app.dependency_overrides[app.get_db] = override_get_db
    return TestClient(app)

# Tests para la entidad Loan
def test_create_loan(client):
    loan_data = {
        "user_id": 1,
        "book_id": 1,
        "due_date": "2024-07-31"
    }
    response = client.post("/api/loans/", json=loan_data)
    assert response.status_code == 201
    assert response.json()["user_id"] == 1

def test_get_loan(client, db_session):
    loan = Loan(user_id=1, book_id=1, due_date="2024-07-31")
    db_session.add(loan)
    db_session.commit()

    response = client.get(f"/api/loans/{loan.id}")
    assert response.status_code == 200
    assert response.json()["user_id"] == 1

def test_update_loan(client, db_session):
    loan = Loan(user_id=1, book_id=1, due_date="2024-07-31")
    db_session.add(loan)
    db_session.commit()

    update_data = {
        "due_date": "2024-08-31"
    }
    response = client.put(f"/api/loans/{loan.id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["due_date"] == "2024-08-31"

def test_delete_loan(client, db_session):
    loan = Loan(user_id=1, book_id=1, due_date="2024-07-31")
    db_session.add(loan)
    db_session.commit()

    response = client.delete(f"/api/loans/{loan.id}")
    assert response.status_code == 204
