# tests/test_sample.py

import pytest
from src.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_soma_positiva(client):
    response = client.get("/soma?a=2&b=3")
    data = response.get_json()
    assert response.status_code == 200
    assert data["resultado"] == 5

def test_soma_negativa(client):
    response = client.get("/soma?a=-2&b=-3")
    data = response.get_json()
    assert response.status_code == 200
    assert data["resultado"] == -5

def test_soma_decimal(client):
    response = client.get("/soma?a=2.5&b=3.1")
    data = response.get_json()
    assert response.status_code == 200
    assert data["resultado"] == pytest.approx(5.6)

def test_soma_parametro_faltando(client):
    response = client.get("/soma?a=2")
    data = response.get_json()
    assert response.status_code == 200
    assert data["resultado"] == 2  # b=0 por padrão

def test_soma_parametro_invalido(client):
    response = client.get("/soma?a=abc&b=3")
    data = response.get_json()
    assert response.status_code == 400
    assert "erro" in data
