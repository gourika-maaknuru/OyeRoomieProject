__author__ = 'Gourika Maaknuru'

class Locator(object):

#HomePage locators
    url = "https://oyeroomie.com"
    logo = "//img[@id='logo_image']"
    price_up = "//div[@id='slider_price']//span[1]"
    price_down = "//div[@id='slider_price']//span[2]"
    cursor = "//*[@id='myCarousel']/i"
    calender = "//input[@id='available-from']"
    current_date = "//a[contains(@class, 'highlight')]"
    last_month = "//span[@class ='ui-icon ui-icon-circle-triangle-w']"
    last_date = "//a[contains(text(),'8')]"
    future_month = "//span[@class ='ui-icon ui-icon-circle-triangle-e']"
    future_date = "//a[contains(text(),'5')]"
    male = "//div[@id='search_wrapper']//input[@id='male']"
    female = "//div[@id='search_wrapper']//input[@id='female']"

#PostAd locator
    submit_property = "//a[@class='headerBtn submitProperty']"
    guest_login = "//div[@class='login-links']//div[@id='guestloginsidebar_topbar']"
    room_rent = "//div[@id ='room-to-rent']//input[@id='room_rent']"
    language = "//div[@id='room-to-rent']//input[@name='language']"
    title = "//div[@id='room-to-rent']//input[@id='prop_title']"
    description = "//div[@id='room-to-rent']//div[@class='form-group col-md-12 full-width']//textarea"
    property_address = "//input[@id='property_address']"
    name = "//div[@id='room-to-rent']//div[@class='form-group col-md-6']//input[@id='agent_name']"
    email = "//div[@id='room-to-rent']//div[@class='form-group col-md-6']//input[@id='agent_user_email']"
    verify_email = "//div[@id='room-to-rent']//div//div[@class='form-group col-md-6']//span[@id='varify_cont_email']"
    source_url = "view-source:https://oyeroomie.com/"
    location = "C:\\Users\\gouri\\Desktop\\Selenium and python\\selenium programs\\Excel_sel_py.xlsx"



