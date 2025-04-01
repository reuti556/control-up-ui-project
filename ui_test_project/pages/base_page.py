import logging
from playwright.sync_api import Page,Locator
from ui_test_project.helper.logger import logger  


class BasePage():
    def __init__(self,page:Page):
        self.page = page
        self.logger = logger
    
    def perform_safe_interaction(self, action, *args):
            try:
                return action(*args)
            except Exception as e:
                self.logger.error(f"Failed to perform action on element. Exception: {str(e)}")
                raise

    def click_element(self,locator:Locator):
        self.perform_safe_interaction(locator.click)


    def fill_text(self,text:str,locator:Locator):
        self.perform_safe_interaction(locator.fill,text)


    def is_visible(self,locator:Locator):
        return self.perform_safe_interaction(locator.is_visible)
    
    def get_element_text_content(self,locator:Locator):
        return self.perform_safe_interaction(locator.text_content)

    def get_all_elements(self,locator:Locator):
        return self.perform_safe_interaction(locator.all)
