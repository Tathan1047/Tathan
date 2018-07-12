import time
from selenium.webdriver.common.keys import Keys
from settings_webdriver import ChromeWebDriver



class Robot:
    def __init__(self, name, webdriver):
        self._state = 'Processing'
        self.name = name
        self.webdriver = webdriver

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value


class SeoRobot(Robot):

    def __init__(self, webdriver):
        super().__init__(webdriver=webdriver, name='Seo_Robot')

    def login(self, username=None, password=None):
        self.webdriver.find_by_id('email').send_keys(username)
        self.webdriver.find_by_id('pass').send_keys(password, Keys.ENTER)

    def list_result(self, count_result=None):
        return













