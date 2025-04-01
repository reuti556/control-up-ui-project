from ui_test_project.helper.config import CREDENTIALS, VALIDATION_TEST_DATA
from ui_test_project.pages.main_login_page import MainLoginPage

def test_item_added_to_cart(setup):
    expected_cart_badge = VALIDATION_TEST_DATA["expected_cart_badge"]
    user_name, password = CREDENTIALS.values()
    login_page = MainLoginPage(setup)

    #Navigate to the login URL
    login_page.navigate_login_url()

    #Perform login
    products_page = login_page.perform_login(user_name, password)    
    assert products_page is not None, "The perform_login method returned None!"

    #Add item to cart
    result = products_page.add_item_to_cart()
    assert result ,f"Failed - item was not added to the cart"
    
    #Get cart badge amount and validate
    cart_badge_amount = products_page.get_cart_badge_amount()
    assert cart_badge_amount ==  expected_cart_badge , f"Failed - cart badge is {cart_badge_amount} which is different from the expected {expected_cart_badge}"
