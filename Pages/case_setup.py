from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class case_setup():
    def __init__(self, myDriver):
        self.driver = myDriver
        self.dob = (By.NAME, 'PIDOB')
        self.owner_aplicant_no = (By.XPATH, '(//input[@name="Applicant_IsInsured"])[2]')
        self.owner_type = (By.XPATH, '(//div[@class="select is-searchable has-warning"])[1]')
        self.sign_state = (By.XPATH, '(//input[@name="Applicant_SignState"])[2]')

    def enter_dob(self, dob):
        self.driver.find_element(*self.dob).clear()
        for i in range(10):
            self.driver.find_element(*self.dob).send_keys(Keys.BACK_SPACE)
            print('juani gato')
        self.driver.find_element(*self.dob).send_keys(dob)

    def set_state(self, state):
        self.driver.find_element(*self.sign_state).send_keys(state)
        self.driver.find_element(*self.sign_state).send_keys(Keys.DOWN)
        self.driver.find_element(*self.sign_state).send_keys(Keys.RETURN)




