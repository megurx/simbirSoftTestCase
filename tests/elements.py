from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = driver.find_element(By.ID, "firstName")
        self.last_name = driver.find_element(By.ID, "lastName")
        self.email = driver.find_element(By.ID, "userEmail")
        self.gender_radio = driver.find_element(By.ID,"gender-radio-1")
        self.user_number = driver.find_element(By.ID, "userNumber")
        self.date_of_birth_click = driver.find_element(By.ID, "dateOfBirthInput")
        self.subject = driver.find_element(By.ID, "subjectsInput")
        self.hobbies_radio = driver.find_element(By.ID,"hobbies-checkbox-1")
        self.upload_button = driver.find_element(By.ID, "uploadPicture")
        self.current_address = driver.find_element(By.ID, "currentAddress")
        self.state_dropdown = driver.find_element(By.ID, "state")
        self.city_dropdown = driver.find_element(By.ID, "city")
        self.sumbit = driver.find_element(By.ID, "submit")
    
    def fill_form(self, first_name,last_name,email,user_number,current_address):
        self.first_name.send_keys(first_name)
        self.last_name.send_keys(last_name)
        self.email.send_keys(email)
        self.user_number.send_keys(user_number)
        self.current_address.send_keys(current_address)

    def select_gender(self):
        gender = self.gender_radio
        self.driver.execute_script("arguments[0].click();", gender)

    def select_hobby(self):
        hobbies = self.hobbies_radio
        self.driver.execute_script("arguments[0].click();", hobbies)

    def date_of_birth(self, month, year, day):
        self.date_of_birth_click.click()
        time.sleep(2)
        Select(self.driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")).select_by_value(month)
        Select(self.driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")).select_by_value(year)
        self.driver.find_element(By.XPATH, f"//div[contains(text(),'{day}')]").click()

    def select_subject(self, subject):
        self.subject.send_keys(subject)
        self.subject.send_keys(Keys.RETURN)
    
    def upload_picture(self, picture_path):
        upload_button = self.driver.find_element(By.ID, "uploadPicture")
        upload_button.send_keys(picture_path)
    
    def select_state(self, state):
        self.state_dropdown.click()
        time.sleep(1)
        state_option = self.driver.find_element(By.XPATH, f"//div[@id='state']//div[text()='{state}']")
        state_option.click()

    def select_city(self, city):
        self.city_dropdown.click()
        time.sleep(1)
        city_option = self.driver.find_element(By.XPATH, f"//div[@id='city']//div[text()='{city}']")
        city_option.click()
    
    def submit_form(self):
        self.sumbit.click()