from selenium.webdriver.common.by import By

class dtc():
    def __init__(self, myDriver):
        self.driver = myDriver
        self.auth_token =(By.ID, 'token')
        self.logon_id = (By.ID,'logonID')
        self.create_unique_id_button = (By.XPATH, '//button[@onclick = "createUUID()"]')
        self.case_state = (By.ID,'CaseState')
        self.load_igo = (By.NAME, 'btnGenerate')

    def enter_token(self, token):
        self.driver.find_element(*self.auth_token).send_keys(token)

    def enter_logon_ID(self):
        self.driver.find_element(*self.logon_id).send_keys('testAgentIntermediary')

    def click_create_unique_id(self):
        self.driver.find_element(*self.create_unique_id_button).click()

    def enter_case_state(self, state):
        self.driver.find_element(*self.case_state).clear()
        self.driver.find_element(*self.case_state).send_keys(state)

    def click_load_igo(self):
        self.driver.find_element(*self.load_igo).click()