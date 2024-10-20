import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test that the homepage loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"DEPI DevOps Project" in response.data

def test_static_file(client):
    """Test that the static file (image) is served correctly."""
    response = client.get('/static/docker2.jpg')
    assert response.status_code == 200

