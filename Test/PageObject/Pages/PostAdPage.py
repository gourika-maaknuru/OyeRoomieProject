__author__ = 'Gourika Maaknuru'

from Test.TestBase.EnvironmentSetUp import EnvironmentSetUp
from Test.PageObject.Locators import Locator
from selenium import webdriver
from selenium.webdriver.common.by import By

class PostAd(object):
    def __init__(self, driver):
        self.driver = driver
        self.submit_property = driver.find_element(By.XPATH, Locator.submit_property)
        self.guest_login = driver.find_element(By.XPATH, Locator.guest_login)
        #self.room_rent = driver.find_element(By.XPATH, Locator.room_rent)

        #self.verify_email = driver.find_element(By.XPATH, Locator.verify_email)


    def getSubmitProperty(self):
        return self.submit_property

    def getGuestLogin(self):
        return self.guest_login














