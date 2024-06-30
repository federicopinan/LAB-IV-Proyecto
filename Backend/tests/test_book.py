import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from models.book import Libro
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
    Book.metadata.create_all(bind=engine)

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

# Tests para la entidad Book
def test_create_book(client):
    book_data = {
        "title": "Test Book",
        "author": "Test Author",
        "isbn": "1234567890"
    }
    response = client.post("/api/books/", json=book_data)
    assert response.status_code == 201
    assert response.json()["title"] == "Test Book"

def test_get_book(client, db_session):
    book = Book(title="Test Book", author="Test Author", isbn="1234567890")
    db_session.add(book)
    db_session.commit()

    response = client.get(f"/api/books/{book.id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"

def test_update_book(client, db_session):
    book = Book(title="Test Book", author="Test Author", isbn="1234567890")
    db_session.add(book)
    db_session.commit()

    update_data = {
        "author": "Updated Author"
    }
    response = client.put(f"/api/books/{book.id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["author"] == "Updated Author"

def test_delete_book(client, db_session):
    book = Book(title="Test Book", author="Test Author", isbn="1234567890")
    db_session.add(book)
    db_session.commit()

    response = client.delete(f"/api/books/{book.id}")
    assert response.status_code == 204
