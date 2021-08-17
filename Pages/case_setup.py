from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class case_setup():
    def __init__(self, myDriver):
        self.driver = myDriver
        self.dob = (By.NAME, 'PIDOB')
        self.owner_aplicant_no = (By.XPATH, '(//input[@name="Applicant_IsInsured"])[2]')
        self.owner_type = (By.XPATH, '(//div[@class="select is-searchable has-warning"])[1]')
        self.sign_state = (By.XPATH, '(//input[@name="Applicant_SignState"])[2]')
        self.resident_state = (By.XPATH,'(//input[@name="Situs_ResidenceState"])[2]')
        self.service_agent_yes_button = (By.XPATH, '(//input[@name="CS_AGENT_IsServicingAgent"])[1]')
        #self.validate_agent_button = (By.XPATH, '(//button[@class = "field field-button btn-block btn-default runtime-btn btn btn-primary"])[1]')
        self.validate_agent_button = (By.XPATH, '(//div[@class= "field-main-container field-main-container_button"])[1]')
        self.agent_email_address = (By.NAME, 'CS_AGENT_Email')
        self.disability_income_no = (By.XPATH, '(//input[@name = "CS_AGENT_DisabilityIncome"])[2]')
        self.premium_financing_no = (By.XPATH, '(//input[@name = "CS_AGENT_Financing"])[2]')
        self.agent_english_no = (By.XPATH, '(//input[@name = "CS_AGENT_English"])[2]')
        self.next_button = (By.XPATH, '(//button[@class = "field field-button btn-block btn-default runtime-btn btn btn-primary"])[3]')


    def enter_dob(self, dob):
        self.driver.find_element(*self.dob).clear()
        for i in range(10):
            self.driver.find_element(*self.dob).send_keys(Keys.BACK_SPACE)
        self.driver.find_element(*self.dob).send_keys(dob)

    def set_sign_state(self, state):
        self.driver.find_element(*self.sign_state).send_keys(state)
        self.driver.find_element(*self.sign_state).send_keys(Keys.DOWN)
        self.driver.find_element(*self.sign_state).send_keys(Keys.RETURN)

    def set_res_state(self, state):
        self.driver.find_element(*self.resident_state).send_keys(state)
        self.driver.find_element(*self.resident_state).send_keys(Keys.DOWN)
        self.driver.find_element(*self.resident_state).send_keys(Keys.RETURN)

    def set_service_agent_yes(self):
        self.driver.find_element(*self.service_agent_yes_button).click()

    def validate_agent(self):
        self.driver.find_element(*self.validate_agent_button).click()

    def set_email_address(self, email):
        for i in range(18):
            self.driver.find_element(*self.agent_email_address).send_keys(Keys.BACK_SPACE)
        self.driver.find_element(*self.agent_email_address).send_keys(email)

    def set_disability_no(self):
        self.driver.find_element(*self.disability_income_no).click()

    def set_premium_financing_no(self):
        self.driver.find_element(*self.premium_financing_no).click()

    def set_agent_english_no(self):
        self.driver.find_element(*self.agent_english_no).click()

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

