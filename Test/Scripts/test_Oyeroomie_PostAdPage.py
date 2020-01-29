__author__ = 'Gourika Maaknuru'

import unittest
from Test.TestBase.EnvironmentSetUp import EnvironmentSetUp
from Test.PageObject.Locators import Locator
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Test.PageObject.Pages.PostAdPage import PostAd
from Test.TestUtility.Screenshot import SS
from time import sleep

class Oyeroomie_PostAdPage(EnvironmentSetUp):
    def test_SubmitProperty(self):
        driver = self.driver
        self.driver.get(Locator.url)
        self.driver.get(Locator.source_url)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(30)
        states = self.driver.find_elements_by_partial_link_text("state")
        print(len(states))
        cur_win = driver.current_window_handle  # get current/main window
        try:
          for link in states:
                link.click()
                driver.switch_to.window([win for win in driver.window_handles if win != cur_win][0])
                postad = PostAd(driver)
                postad.getSubmitProperty().click()
                print("Submit Property is selected")
                postad.getGuestLogin().click()
                print("Submit Property is selected")
                roomrent = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, Locator.room_rent)))
                roomrent.send_keys("650")
                print("Room Rent is entered")
                lang = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, Locator.language)))
                lang.send_keys("Telugu/English")
                print("Language is selected")
                subject = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, Locator.title)))
                subject.send_keys("650")
                print("Looking for Room mate")
                data = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, Locator.description)))
                data.send_keys("Looking for Room mate. Reach me")
                print("Description is entered")
                address = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, Locator.property_address)))
                address.send_keys("172 River Street, Waltham, MA, USA")
                print("Address is entered")
                fullname = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, Locator.name)))
                fullname.send_keys("Riks")
                print("Name is entered")
                emailadd = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, Locator.email)))
                emailadd.send_keys("gourika.jaiswal@gmail.com")
                print("Email address is entered")
                verify = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, Locator.verify_email)))
                verify.click()
                print("Verify Email Address")
                driver.close()
                driver.switch_to.window(cur_win)


        except:
            print("Exception Occured")




if __name__ == '__main__':
    unittest.main()
