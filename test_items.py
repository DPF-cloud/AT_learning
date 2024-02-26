import pytest
import time
from selenium.webdriver.common.by import By



class Test():
    @pytest.mark.smoke
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
    def test_element(self, browser, link):
        browser.implicitly_wait(7)
        browser.get(link)
        basket_button = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button")
        assert basket_button.is_displayed()