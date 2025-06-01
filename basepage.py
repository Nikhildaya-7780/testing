from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(Config.BASE_URL)

    def find_element(self, by, value):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))

    def click(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def type(self, by, value, text):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def is_element_present(self, by, value):
        try:
            self.find_element(by, value)
            return True
        except:
            return False
