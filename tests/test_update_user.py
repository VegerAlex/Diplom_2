import pytest
import allure
import requests

@allure.feature("Update User Data")
class TestUpdateUser:

    @allure.story("Update user data with authorization")
    def test_update_user_authorized(self, base_url, login_user):
        updated_data = {
            "name": "Updated User"
        }
        headers = {"Authorization": login_user}
        response = requests.patch(f"{base_url}/auth/user", json=updated_data, headers=headers)
        assert response.status_code == 200
        assert response.json()["user"]["name"] == "Updated User"

    @allure.story("Update user data without authorization")
    def test_update_user_unauthorized(self, base_url):
        updated_data = {
            "name": "Updated User"
        }
        response = requests.patch(f"{base_url}/auth/user", json=updated_data)
        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"
