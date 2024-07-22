# Diplom_2

Файл tests/test_create_user.py

test_create_unique_user - проверяет создание уникального пользователя.
test_create_user_already_registered - проверяет попытку создания пользователя, который уже зарегистрирован.
test_create_user_missing_field - проверяет создание пользователя без заполнения одного из обязательных полей.

Файл tests/test_login_user.py

test_login_existing_user - проверяет логин под существующим пользователем.
test_login_incorrect_credentials - проверяет логин с неверным логином и паролем.

Файл tests/test_update_user.py

test_update_user_authorized - проверяет изменение данных пользователя с авторизацией.
test_update_user_unauthorized - проверяет изменение данных пользователя без авторизации, ожидая ошибку.

Файл tests/test_create_order.py

test_create_order_authorized - проверяет создание заказа с авторизацией.
test_create_order_unauthorized - проверяет создание заказа без авторизации, ожидая ошибку.
test_create_order_with_ingredients - проверяет создание заказа с ингредиентами.
test_create_order_without_ingredients - проверяет создание заказа без ингредиентов, ожидая ошибку.
test_create_order_invalid_ingredient_hash - проверяет создание заказа с неверным хешем ингредиентов, ожидая ошибку.

Файл tests/test_get_user_orders.py

test_get_orders_authorized - проверяет получение заказов конкретного пользователя, который авторизован.
test_get_orders_unauthorized - проверяет получение заказов конкретного пользователя, который не авторизован, ожидая ошибку.