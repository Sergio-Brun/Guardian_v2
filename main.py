import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.get_token import token
from Pages.dtc import dtc
from Pages.case_setup import case_setup
import time

class regression(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--start-maximized')
        options.add_argument('incognito')
        self.driver = webdriver.Chrome('chromedriver.exe', options= options)
        self.driver.implicitly_wait(5)
        self.driver.get('https://ipipeline.github.io/DTCCarrierTest/210115_Guardian_SDK_POC/GuardianIntermediaryLifeQA5.html')
        self.token = token()
        self.dtc = dtc(self.driver)
        self.case_setup = case_setup(self.driver)

    def test_prueba(self):
        a = self.token.get_token()
        time.sleep(5)
        self.dtc.enter_token(a)
        self.dtc.enter_logon_ID()
        self.dtc.click_create_unique_id()
        self.dtc.enter_case_state('AZ')
        self.dtc.click_load_igo()
        time.sleep(30)
        print('proyecto del ojete')
        self.case_setup.set_state('Arizona')
        self.case_setup.enter_dob('01/03/1991')

        time.sleep(10)



    def tearDown(self):

        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

#hola
