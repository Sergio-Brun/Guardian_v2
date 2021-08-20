from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class menu():

    def __init__(self, myDriver):
        self.driver = myDriver
        self.proposed_insured = (By.XPATH, '(//div[@class="sc-tree-item-content__title"])[3]')

    def go_to_proposed_insured(self):
        self.driver.find_element(*self.proposed_insured).click()