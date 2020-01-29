__author__ = 'Gourika Jaiswal'


import unittest
from Test.TestBase.EnvironmentSetUp import EnvironmentSetUp

class MyTestCase(EnvironmentSetUp):

    def test_Navigate(self):
        self.driver.get("https://oyeroomie.com/")
        print(self.driver.title)

if __name__ == '__main__':
    unittest.main()
