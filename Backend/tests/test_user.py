import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from models.user import Usuario
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
    User.metadata.create_all(bind=engine)

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

# Tests para la entidad User
def test_create_user(client):
    user_data = {
        "username": "test_user",
        "password": "test_password",
        "email": "test@example.com"
    }
    response = client.post("/api/users/", json=user_data)
    assert response.status_code == 201
    assert response.json()["username"] == "test_user"

def test_get_user(client, db_session):
    user = User(username="test_user", password="test_password", email="test@example.com")
    db_session.add(user)
    db_session.commit()

    response = client.get(f"/api/users/{user.id}")
    assert response.status_code == 200
    assert response.json()["username"] == "test_user"

def test_update_user(client, db_session):
    user = User(username="test_user", password="test_password", email="test@example.com")
    db_session.add(user)
    db_session.commit()

    update_data = {
        "email": "updated_test@example.com"
    }
    response = client.put(f"/api/users/{user.id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["email"] == "updated_test@example.com"

def test_delete_user(client, db_session):
    user = User(username="test_user", password="test_password", email="test@example.com")
    db_session.add(user)
    db_session.commit()

    response = client.delete(f"/api/users/{user.id}")
    assert response.status_code == 204
