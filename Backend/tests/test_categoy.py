import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from models.category import Categoria
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
    Category.metadata.create_all(bind=engine)

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

# Tests para la entidad Category
def test_create_category(client):
    category_data = {
        "name": "Test Category",
        "description": "Test Description"
    }
    response = client.post("/api/categories/", json=category_data)
    assert response.status_code == 201
    assert response.json()["name"] == "Test Category"

def test_get_category(client, db_session):
    category = Category(name="Test Category", description="Test Description")
    db_session.add(category)
    db_session.commit()

    response = client.get(f"/api/categories/{category.id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Category"

def test_update_category(client, db_session):
    category = Category(name="Test Category", description="Test Description")
    db_session.add(category)
    db_session.commit()

    update_data = {
        "description": "Updated Description"
    }
    response = client.put(f"/api/categories/{category.id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["description"] == "Updated Description"

def test_delete_category(client, db_session):
    category = Category(name="Test Category", description="Test Description")
    db_session.add(category)
    db_session.commit()

    response = client.delete(f"/api/categories/{category.id}")
    assert response.status_code == 204
