import pytest
import allure
import requests

@allure.feature("User Login")
class TestLoginUser:

    @allure.story("Login with existing user")
    def test_login_existing_user(self, base_url, create_user, user_data):
        response = requests.post(f"{base_url}/auth/login", json=user_data)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.story("Login with incorrect credentials")
    def test_login_incorrect_credentials(self, base_url):
        invalid_user_data = {
            "email": "nonexistent@test.com",
            "password": "wrongpassword"
        }
        response = requests.post(f"{base_url}/auth/login", json=invalid_user_data)
        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"
