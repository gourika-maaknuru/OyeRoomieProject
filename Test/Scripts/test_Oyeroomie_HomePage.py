__author__ = 'Gourika Maaknuru'

import sys
import os
sys.path.append(os.path.abspath('../../'))

from Test.TestBase.EnvironmentSetUp import EnvironmentSetUp
from Test.PageObject.Locators import Locator
from selenium import webdriver
from selenium.webdriver.common.by import By
from Test.PageObject.Pages.HomePage import Home
from Test.TestUtility.Screenshot import SS
from time import sleep
import unittest
import HtmlTestRunner
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from io import StringIO


class Oyeroomie_HomePage(EnvironmentSetUp):
    def test_Logo(self):                                 # 1st test case - Click logo and page refreshed #
        driver = self.driver
        self.driver.get(Locator.url)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(30)
        home = Home(driver)
        home.getLogo().click()
        print("Refreshed")

    def test_Slider(self):                               # 2nd test case - Set price Slider #
        driver = self.driver
        self.driver.get(Locator.url)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(30)
        home = Home(driver)
        x = home.getPriceUp()
        y = home.getPriceDown()
        move = ActionChains(driver)
        move.click_and_hold(y).move_by_offset(-40, 0).release().perform()
        move.click_and_hold(x).move_by_offset(20, 0).release().perform()
        print("The prices are selected")


    def test_Cursor(self):                              # 3rd test case - Remove Ad  #
        driver = self.driver
        self.driver.get(Locator.url)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(30)
        home = Home(driver)
        home.getCursor().click()
        print("Ad Dialog box closed")


    def test_Calender(self):                             # 3rd test case - Calender Dates selected  #
        driver = self.driver
        self.driver.get(Locator.url)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(30)
        home = Home(driver)
        home.getCalender().click()
        print("Calender Selected")
        present_date = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, Locator.current_date)))
        present_date.click()
        print("Current date is selected")
        home.getCalender().click()
        last_mon = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.last_month)))
        last_mon.click()
        print("Last Month is selected")
        last_date = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.last_date)))
        last_date.click()
        print("Date is selected")
        home.getCalender().click()
        next_month = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.future_month)))
        next_month.click()
        print("Next Month is selected")
        next_date = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.future_date)))
        next_date.click()
        print("Date is selected")

    def test_Gender(self):                              # 3rd test case - Select Gender  #
        driver = self.driver
        self.driver.get(Locator.url)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(30)
        home = Home(driver)
        home.getMale().click()
        home.getFemale().click()
        sleep(3)
        print("Gender Category Selected")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HtmlTestRunner(output="C:\\Users\\gouri\\PycharmProjects\\WebAutomation\\Reports"))
