from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class pi():

    def __init__(self, myDriver):
        self.driver = myDriver
        self.name = (By.NAME, 'PIFirstName')
        self.last_name = (By.NAME, 'PILastName')
        self.change_name_no = (By.XPATH, '(//input[@name ="PINameChanged"])[2]')
        self.street_address = (By.NAME, 'PIAddress_Line1')
        self.city = (By.NAME, 'PIAddress_City')
        self.zip = (By.NAME, 'PIAddress_Zip')
        self.state = (By.NAME, 'PIAddress_State')
        self.years_in_address = (By.NAME, 'PIAddress_YearsAtAddress')
        self.mailing_same_as_residence_yes = (By.XPATH, '(//input[@name="PIAddress_MailingSameAsStreet"])[1]')
        self.phone_number = (By.NAME, 'PIPhone')
        self.email = (By.NAME, 'PIEMail')
        self.place_of_birth = (By.XPATH, '(//div[@class="select-placeholder"])[6]')
        self.citizen_usa = (By.XPATH, '(//input[@name="PICitizen"])[1]')
        self.drivers_license_yes = (By.XPATH, '(//input[@name="PIDL_Valid"])[1]')

    def set_drivers_license_yes(self):
        self.driver.find_element(*self.drivers_license_yes).click()

    def set_citizen_usa_yes(self):
        self.driver.find_element(*self.citizen_usa).click()

    def set_place_of_birth(self, place):
        self.driver.find_element(*self.place_of_birth).send_keys(place)
        self.driver.find_element(*self.place_of_birth).send_keys(Keys.DOWN)
        self.driver.find_element(*self.place_of_birth).send_keys(Keys.RETURN)

    def set_email(self, email):
        self.driver.find_element(*self.email).send_keys(email)

    def set_phone_number(self, number):
        self.driver.find_element(*self.phone_number).send_keys(number)

    def set_mailing_same_as_residence_yes(self):
        self.driver.find_element(*self.mailing_same_as_residence_yes).click()

    def set_years_in_address(self, years):
        self.driver.find_element(*self.years_in_address).send_keys(years)

    def set_state(self, state):
        self.driver.find_element(*self.state).click()
        self.driver.find_element(*self.state).send_keys(state)
        self.driver.find_element(*self.state).send_keys(Keys.DOWN)
        self.driver.find_element(*self.state).send_keys(Keys.RETURN)

    def set_zip(self, zip):
        self.driver.find_element(*self.zip).click()

        for i in range(10):
            self.driver.find_element(*self.name).send_keys(Keys.ARROW_LEFT)

        self.driver.find_element(*self.zip).send_keys(zip)

    def set_city(self, city):
        self.driver.find_element(*self.city).send_keys(city)

    def set_street_addres(self,street):
        self.driver.find_element(*self.street_address).send_keys(street)

    def set_change_name_no(self):
        self.driver.find_element(*self.change_name_no).click()

    def set_pi_name(self, nombre):
        piname = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(self.name))
        piname.click()
        for i in range(9):
            self.driver.find_element(*self.name).send_keys(Keys.BACK_SPACE)
        self.driver.find_element(*self.name).send_keys(nombre)

    def set_pi_last_name(self, last_name):
        for i in range(8):
            self.driver.find_element(*self.last_name).send_keys(Keys.BACK_SPACE)
        self.driver.find_element(*self.last_name).send_keys(last_name)

