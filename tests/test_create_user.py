import pytest
import allure
import requests

@allure.feature("User Registration")
class TestCreateUser:

    @allure.story("Create unique user")
    def test_create_unique_user(self, base_url, user_data):
        response = requests.post(f"{base_url}/auth/register", json=user_data)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.story("Create user already registered")
    def test_create_user_already_registered(self, base_url, create_user, user_data):
        response = requests.post(f"{base_url}/auth/register", json=user_data)
        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"

    @allure.story("Create user with missing required field")
    def test_create_user_missing_field(self, base_url):
        incomplete_user_data = {
            "email": "incomplete@test.com",
            "password": "password123"
        }
        response = requests.post(f"{base_url}/auth/register", json=incomplete_user_data)
        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"
