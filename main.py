import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.get_token import token
from Pages.dtc import dtc
from Pages.case_setup import case_setup
from Pages.invite_client_to_data_entry import invite_client_to_data_entry
from Pages.proposed_insured import pi
from Pages.menu import menu
import time

class regression(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--start-maximized')
        options.add_argument('incognito')
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome('chromedriver.exe', options= options)
        self.driver.implicitly_wait(5)
        self.driver.get('https://ipipeline.github.io/DTCCarrierTest/210115_Guardian_SDK_POC/GuardianIntermediaryLifeQA5.html')
        self.token = token()
        self.dtc = dtc(self.driver)
        self.case_setup = case_setup(self.driver)
        self.invite = invite_client_to_data_entry(self.driver)
        self.pi = pi(self.driver)
        self.menu = menu(self.driver)

    def test_prueba(self):
        a = self.token.get_token()
        time.sleep(5)
        self.dtc.enter_token(a)
        self.dtc.enter_logon_ID()
        self.dtc.click_create_unique_id()
        self.dtc.enter_case_state('AZ')
        self.dtc.click_load_igo()
        time.sleep(30)
        self.case_setup.set_sign_state('Arizona')
        self.case_setup.set_res_state('Arizona')
        self.case_setup.enter_dob('01/03/1991')
        self.case_setup.set_service_agent_yes()
        self.case_setup.set_email_address('juani_gato@gmail.com')
        self.case_setup.set_aget_writting_code()
        time.sleep(2)
        self.case_setup.validate_agent()
        time.sleep(4)
        self.case_setup.validate_agent()
        time.sleep(4)
        self.case_setup.set_military_inst_no()
        self.case_setup.set_disability_no()
        self.case_setup.set_premium_financing_no()
        self.case_setup.set_agent_english_no()
        self.case_setup.click_next_button()
        time.sleep(10)
        self.invite.set_invite_client_no()
        self.menu.go_to_proposed_insured()
        #self.invite.click_next()
        self.pi.set_pi_name('pancha')


'''
    def tearDown(self):

        self.driver.close()
        self.driver.quit()
'''
if __name__ == '__main__':
    unittest.main()

#hola ultima version