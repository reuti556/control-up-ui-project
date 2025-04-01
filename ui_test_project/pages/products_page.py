from playwright.sync_api import Page

from ui_test_project.helper.config import PageTitle
from ui_test_project.pages.base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self,page: Page):
        super().__init__(page)
        self.page = page
        self.item = self.page.locator("[data-test='inventory-item']")
        self.title = self.page.locator("[data-test='title']")
        self.add_to_cart_btn = self.page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.remove_from_cart_btn = self.page.locator("[data-test='remove-sauce-labs-backpack']")
        self.cart_badge = self.page.locator("[data-test='shopping-cart-badge']")

    def get_products_inventory_amount(self):
        self.logger.info("Going to get all product items from inventory page")
        items = self.get_all_elements(self.item)
        return len(items)

    def get_cart_badge_amount(self):
        self.logger.info("Going to get cart badge amount")
        cart_badge_amount = self.get_element_text_content(self.cart_badge)
        if cart_badge_amount.isdigit():
            amount_int = int(cart_badge_amount)
            return amount_int
        else:
            self.logger.info("Failed return cart badge amount - element text not a digit")
            return None
    
    def is_products_inventory_page(self):
        title_name = self.get_element_text_content(self.title)
        if (title_name ==  PageTitle.INVENTORY_PRODUCTS.value):
            return True
        else:
            self.logger.info("not the page")
            return False
        
    def add_item_to_cart(self):
        self.click_element(self.add_to_cart_btn)
        remove_visible = self.is_visible(self.remove_from_cart_btn)
        if remove_visible:
            self.logger.info("item added successfully")
            return True
        return False

