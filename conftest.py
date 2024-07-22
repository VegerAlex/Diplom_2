import pytest
import requests

BASE_URL = "https://stellarburgers.nomoreparties.site/api"

@pytest.fixture(scope="module")
def base_url():
    return BASE_URL

@pytest.fixture(scope="module")
def unique_email():
    import uuid
    return f"{uuid.uuid4()}@test.com"

@pytest.fixture
def user_data(unique_email):
    return {
        "email": unique_email,
        "password": "password123",
        "name": "Test User"
    }

@pytest.fixture
def create_user(base_url, user_data):
    response = requests.post(f"{base_url}/auth/register", json=user_data)
    return response

@pytest.fixture
def login_user(base_url, user_data):
    response = requests.post(f"{base_url}/auth/login", json=user_data)
    if response.status_code == 200:
        return response.json()["accessToken"]
    return None
