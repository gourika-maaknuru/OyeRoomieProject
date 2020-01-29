__author__ = 'Gourika Maaknuru'


from Test.TestBase.EnvironmentSetUp import EnvironmentSetUp
from Test.PageObject.Locators import Locator
from selenium import webdriver
from selenium.webdriver.common.by import By
class Home(object):
    def __init__(self, driver):
        self.driver = driver

#HomePage locators defining

# 1st Locator - Click logo and page refreshed #

        self.logo = driver.find_element(By.XPATH, Locator.logo)

# 2nd Locators - Set price Slider #

        self.price_up = driver.find_element(By.XPATH, Locator.price_up)
        self.price_down = driver.find_element(By.XPATH, Locator.price_down)

# 3rd Locator - Remove Ad  #

        self.cursor = driver.find_element(By.XPATH, Locator.cursor)

#4th Locator - Calender #

        self.calender = driver.find_element(By.XPATH, Locator.calender)

# 5th Locator - Gender #
        self.male = driver.find_element(By.XPATH, Locator.male)
        self.female = driver.find_element(By.XPATH, Locator.female)

# Method 1 - Click logo and page refreshed #

    def getLogo(self):
        return self.logo

# Method 2 - Set price Slider #

    def getPriceUp(self):
        return self.price_up

    def getPriceDown(self):
        return self.price_down

# Method 3 - Remove Ad #

    def getCursor(self):
        return self.cursor

# Method 4 - Calender #

    def getCalender(self):
        return self.calender

# Method 4 - Gender #

    def getMale(self):
        return self.male

    def getFemale(self):
        return self.female

