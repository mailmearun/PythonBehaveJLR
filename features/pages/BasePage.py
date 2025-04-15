import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import logging
from utils.LogFile import Logger
from utils.Config import ReadConfig

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def launh_url(self):
        self.driver.get(ReadConfig.getValue("basic", "test_url"))
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    @staticmethod
    def getWebelement(self, locator):
        global webElement
        locator_type = str(locator).split('~')[0]
        locator_value = str(locator).split('~')[1]
        if str(locator).startswith("xpath"):
            webElement = self.driver.find_element(By.XPATH, locator_value)
        elif str(locator).startswith("css"):
            webElement = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        elif str(locator).startswith("class"):
            webElement = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif str(locator).startswith("name"):
            webElement = self.driver.find_element(By.NAME, locator_value)
        elif str(locator).startswith("id"):
            webElement = self.driver.find_element(By.ID, locator_value)
        elif str(locator).startswith("link"):
            webElement = self.driver.find_element(By.LINK_TEXT, locator_value)

    @staticmethod
    def getWebelements(self, locator):
        global webElements
        locator_type = str(locator).split('~')[0]
        locator_value = str(locator).split('~')[1]
        if str(locator).startswith("xpath"):
            webElements = self.driver.find_elements(By.XPATH, locator_value)
        elif str(locator).startswith("css"):
            webElements = self.driver.find_elements(By.CSS_SELECTOR, locator_value)
        elif str(locator).startswith("class"):
            webElements = self.driver.find_elements(By.CLASS_NAME, locator_value)
        elif str(locator).startswith("name"):
            webElements = self.driver.find_elements(By.NAME, locator_value)
        elif str(locator).startswith("id"):
            webElements = self.driver.find_elements(By.ID, locator_value)
        elif str(locator).startswith("link"):
            webElements = self.driver.find_elements(By.LINK_TEXT, locator_value)

    def click(self, locator):
        try:
            self.getWebelement(self, locator).click()
            log.logger.info("Clicking on locator " + locator + " is successsful")
            time.sleep(2)
        except Exception as e:
            print(str(e))
            log.logger.info("Clicking on locator " + locator + " is failed")

    def enterText(self, locator, text):
        try:
            self.getWebelement(self, locator).send_keys(text)
            log.logger.info("Input text in locator " + locator + " is successsful")
            time.sleep(2)
        except Exception as e:
            print(str(e))
            log.logger.info("Input text in locator " + locator + " is failed")

    def getText(self, locator):
        text = ''
        try:
            text = self.getWebelement(self, locator).text
            log.logger.info("get text from locator " + locator + " is successsful")
        except Exception as e:
            print(str(e))
            log.logger.info("get text from locator " + locator + " is failed")
        return text

    def getTitle(self):
        title = self.driver.title
        log.logger.info("Get the Page Title")
        return title

    def hoverElement(self, locator):
        action = ActionChains(self.driver)
        action.move_to_element(self.getWebelement(self, locator)).perform()
        log.logger.info("Hover to an element: " + locator)
