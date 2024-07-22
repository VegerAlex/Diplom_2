import pytest
import allure
import requests

@allure.feature("Get User Orders")
class TestGetUserOrders:

    @allure.story("Get orders of authorized user")
    def test_get_orders_authorized(self, base_url, login_user):
        headers = {"Authorization": login_user}
        response = requests.get(f"{base_url}/orders", headers=headers)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.story("Get orders of unauthorized user")
    def test_get_orders_unauthorized(self, base_url):
        response = requests.get(f"{base_url}/orders")
        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"
