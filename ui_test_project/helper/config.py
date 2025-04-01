from enum import Enum

LOGIN_URL ="https://www.saucedemo.com"

class PageTitle(Enum):
    INVENTORY_PRODUCTS = "Products"

CREDENTIALS = {
    "user_name":"standard_user",
    "password":"secret_sauce"
}

VALIDATION_TEST_DATA = {
    "expected_cart_badge" : 1 ,
    "expected_items" : 6
}