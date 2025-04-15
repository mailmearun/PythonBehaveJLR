import time

from features.pages.BasePage import BasePage
from utils.Config import ReadConfig


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def clickCompanyTab(self):
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

    def verifyLinks(self, list_links):
        try:
            self.hoverElement(ReadConfig.getValue("locator-common", "company_tab"))
            ListWbeElements = self.getWebelements(ReadConfig.getValue("locator-common", "company_links"))
            for link in ListWbeElements:
                self.getText(link)

        except Exception as e:
            print(str(e))