from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class invite_client_to_data_entry():

    def __init__(self, myDriver):
        self.driver = myDriver
        self.next = (By.XPATH, '(//button[@class ="field field-button btn-block btn-default runtime-btn btn btn-primary"])[2]')
        self.invite_client_no = (By.XPATH, '(//input[@name="INVITE_ParticipateYesNo"])[2]')

    def click_next(self):
        invite = WebDriverWait(self.driver, 60).until(EC.element_located_to_be_selected(self.next))
        invite.click()

    def set_invite_client_no(self):
        #invite = WebDriverWait(self.driver, 60).until(EC.element_located_to_be_selected(self.invite_client_no))
        #invite.click()
        self.driver.find_element(*self.invite_client_no).click()
