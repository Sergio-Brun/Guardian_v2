from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class pi():

    def __init__(self, myDriver):
        self.driver = myDriver
        self.name = (By.NAME, 'PIFirstName')

    def set_pi_name(self, nombre):
        piname = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(self.name))
        piname.send_keys(nombre)
