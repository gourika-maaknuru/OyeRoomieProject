__author__ = 'Gourika Maaknuru'

from selenium import webdriver
import unittest


class SS(object):

    def __init__(self, driver):
        self.driver = driver

    def ScreenShot(self, path):
        directory = "C:\\Users\\gouri\\Desktop\\Selenium and python\\selenium programs\\Pgm_Screenshots"
        self.driver.get_screenshot_as_file(directory+path)
