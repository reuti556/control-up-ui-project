from playwright.sync_api import Page
from ui_test_project.helper.config import LOGIN_URL
from ui_test_project.pages.base_page import BasePage
from ui_test_project.pages.products_page import ProductsPage

class MainLoginPage(BasePage):
    def __init__(self,page: Page):
        super().__init__(page)
        self.page = page
        self.login_section = self.page.locator("[data-test='login-container']")
        self.user_field = self.page.locator("[data-test='username']")
        self.pass_field = self.page.locator("[data-test='password']")
        self.login_btn = self.page.locator("[data-test='login-button']")


    def navigate_login_url(self):
        self.logger.info("navigate url")
        self.page.goto(LOGIN_URL)
        self.logger.info("Verify navigation url succeeded")
        result = self.is_visible(locator=self.login_section)
        assert result , "Failed to navigate login url"

    def perform_login(self,user_name,password):
        self.logger.info("perform login")
        self.fill_text(locator=self.user_field,text=user_name)
        self.fill_text(locator=self.pass_field,text=password)
        self.click_element(locator=self.login_btn)
        products_page = ProductsPage(self.page)
        if products_page.is_products_inventory_page():
            return products_page
        else:
            return None
