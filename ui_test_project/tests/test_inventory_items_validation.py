from ui_test_project.helper.config import CREDENTIALS, VALIDATION_TEST_DATA
from ui_test_project.pages.main_login_page import MainLoginPage

def test_inventory_items_validation(setup):
    expected_items = VALIDATION_TEST_DATA["expected_items"]
    user_name, password = CREDENTIALS.values()
    login_page = MainLoginPage(setup)

    #Navigate to the login URL
    login_page.navigate_login_url()

    #Perform login
    products_page = login_page.perform_login(user_name, password)    
    assert products_page is not None, "The perform_login method returned None!"

    #Get products inventory amount and verify as expected
    items = products_page.get_products_inventory_amount()
    assert int(items) == expected_items ,f"Failed - product inventory should display {expected_items} items and not {int(items)}"
