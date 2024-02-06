import pytest
from selenium import webdriver
from elements import FormPage
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_fill_form(browser):
    browser.get("https://demoqa.com/automation-practice-form")
    elements = FormPage(browser)
    elements.fill_form("Nikita", "Polyakov", "testemail@test.com", "0123456789", "123 Street")
    elements.date_of_birth("2","1999","20")
    elements.select_subject("Math")
    elements.upload_picture("C:/Users/megurx/Downloads/DJ3AVD69F7g.jpg")
    elements.select_state("NCR")
    elements.select_city("Delhi")
    elements.select_gender()
    elements.select_hobby()
    elements.submit_form()
    time.sleep(10)
    browser.close()