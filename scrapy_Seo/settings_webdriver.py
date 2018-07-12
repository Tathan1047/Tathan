import os
import sys
from telnetlib import EC

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

BASE_DIR = os.path.dirname(__file__)


class ChromeWebDriver:

    def __init__(self):
        self.__driver = WebDriver(
            executable_path=self._get_executable_path(),
            options=self.get_options
        )
        self.__driver_wait = WebDriverWait(driver=self.__driver, timeout=20)

    def _get_executable_path(self):
        "get the browser driver according to the platform that we are using"
        if sys.platform != 'linux':
            return self._path_chromedriver('chromedriver.exe')
        return self._path_chromedriver('chromedriver')

    def _path_chromedriver(self, chromedriver):
        return os.path.join(BASE_DIR, 'drivers', chromedriver)

    @property
    def get_options(self):
        options = Options()
        options.add_argument('--incognito')#options for start browser in incognito
        options.add_argument('start-maximized')#open browser with widows maximized
        return options

    @property
    def driver(self):
        return self.__driver

    def get_element(self, xpath):#this method is the provider of waits still load any elements

        return self.__driver_wait.until(EC.element_to_be_clickable(By.XPATH, xpath))



