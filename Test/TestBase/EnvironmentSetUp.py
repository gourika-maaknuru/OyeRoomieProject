__author__ = 'Gourika Maaknuru'

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import unittest

class EnvironmentSetUp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\gouri\\PycharmProjects\\WebAutomation\\Drivers\\chromedriver.exe")
        self.driver.set_page_load_timeout(30)




    def tearDown(self):
        if (self.driver != None):
            print("completed")
            self.driver.close()







if __name__ == '__main__':
    unittest.main()
