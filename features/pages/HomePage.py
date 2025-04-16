import time

from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage
from utils.Config import ReadConfig


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def moveToCompanyTab(self):
        try:
            self.hoverElement(ReadConfig.getValue("locator-common", "company_tab"))
        except Exception as e:
            print(str(e))

    def verifyPageTitle(self):
        title = ''
        try:
            title = self.getTitle()
        except Exception as e:
            print(str(e))
        return title

    def verifyLinks(self):
        act_list = []
        try:
            self.hoverElement(ReadConfig.getValue("locator-common", "company_tab"))
            ListWbeElements = self.getWebelements(ReadConfig.getValue("locator-common", "company_links"))
            for link in ListWbeElements:
                act_list.append(self.getText(link))
        except Exception as e:
            print(str(e))
        return act_list

    def verifyLinkNavigation(self, linkText):
        print(linkText)
        self.driver.find_elements(By.XPATH, "//a[@class='nav-2024__dropdown-item--first'][text()='"+linkText+"']")
        time.sleep(20)
        return self.getTitle()