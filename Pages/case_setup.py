from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class case_setup():
    def __init__(self, myDriver):
        self.driver = myDriver
        self.dob = (By.NAME, 'PIDOB')
        self.owner_aplicant_no = (By.XPATH, '(//input[@name="Applicant_IsInsured"])[2]')
        self.owner_type = (By.XPATH, '(//div[@class="select is-searchable has-warning"])[1]')

    def enter_dob(self, dob):
        date_of_birth = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(self.dob))
        date_of_birth.clear()
        date_of_birth.send_keys(dob)

    def set_owner_applicant_no(self):
        self.driver.find_element(*self.owner_aplicant_no).click()

    def set_owner_type(self, type):
        Select(self.driver.find_element(*self.owner_type)).select_by_visible_text(type)

