import pytest
import allure
import requests

@allure.feature("Create Order")
class TestCreateOrder:

    @allure.story("Create order with authorization")
    def test_create_order_authorized(self, base_url, login_user):
        ingredients = ["60d3b41abdacab0026a733c6", "609646e4dc916e00276b2870"]
        headers = {"Authorization": login_user}
        response = requests.post(f"{base_url}/orders", json={"ingredients": ingredients}, headers=headers)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.story("Create order without authorization")
    def test_create_order_unauthorized(self, base_url):
        ingredients = ["60d3b41abdacab0026a733c6", "609646e4dc916e00276b2870"]
        response = requests.post(f"{base_url}/orders", json={"ingredients": ingredients})
        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"

    @allure.story("Create order with ingredients")
    def test_create_order_with_ingredients(self, base_url, login_user):
        ingredients = ["60d3b41abdacab0026a733c6", "609646e4dc916e00276b2870"]
        headers = {"Authorization": login_user}
        response = requests.post(f"{base_url}/orders", json={"ingredients": ingredients}, headers=headers)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.story("Create order without ingredients")
    def test_create_order_without_ingredients(self, base_url, login_user):
        headers = {"Authorization": login_user}
        response = requests.post(f"{base_url}/orders", json={}, headers=headers)
        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.story("Create order with invalid ingredient hash")
    def test_create_order_invalid_ingredient_hash(self, base_url, login_user):
        ingredients = ["invalid_hash"]
        headers = {"Authorization": login_user}
        response = requests.post(f"{base_url}/orders", json={"ingredients": ingredients}, headers=headers)
        assert response.status_code == 500
