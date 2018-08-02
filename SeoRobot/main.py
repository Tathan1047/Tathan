import os
import pprint
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

driver = WebDriver(executable_path=os.path.join(BASE_DIR, 'driver', 'chromedriver'))
wait_driver = WebDriverWait(driver=driver, timeout=30)


def get_element(driver, wait, by, value, retry=3):
    attemps = 0
    while (attemps < retry):
        try:
            wait.until(EC.element_to_be_clickable((by, value)))
            return driver.find_element(by, value)
        except:
            attemps += 1
    return None


def excuteGoogle(url, keywords):
    try:
        print("Start SeoRobot Google")
        driver.get(url)  # Url de la pagina a Buscar
        driver.find_element_by_name('q').send_keys(keywords, Keys.ENTER)
        links = driver.find_elements_by_css_selector('.rc > .r a')
        print("Geting Links...")
        time.sleep(3)
        pprint.pprint(dict([(i, _.get_attribute('href')) for i, _ in enumerate(links, 1) ]))
        print("Finished SeoRobot Google")

    finally:
        time.sleep(10)
        driver.quit()


def excuteBing(url, keywords):
    try:
        print("Start SeoRobot Bing")
        driver.get(url)  # Url de la pagina a Buscar
        driver.find_element_by_name('q').send_keys(keywords, Keys.ENTER)
        links = driver.find_elements_by_css_selector('.b_algo a')
        print("Geting Links...")
        time.sleep(3)
        pprint.pprint(dict([(i, _.get_attribute('href')) for i, _ in enumerate(links, 1)]))
        print("Finished SeoRobot Bing")

    finally:
        time.sleep(10)
        driver.quit()

def excuteDuckDuck(url, keywords):
    try:
        print("Start SeoRobot DuckDuck")
        driver.get(url)  # Url de la pagina a Buscar
        driver.find_element_by_name('q').send_keys(keywords, Keys.ENTER)
        links = driver.find_elements_by_css_selector('.result__title a')
        print("Geting Links...")
        time.sleep(3)
        pprint.pprint(dict([(i, _.get_attribute('href')) for i, _ in enumerate(links, 1)]))
        print("Finished SeoRobot DuckDuck")

    finally:
        time.sleep(10)
        driver.quit()

def excuteYahoo(url, keywords):
    try:
        print("Start SeoRobot Yahoo")
        driver.get(url)  # Url de la pagina a Buscar
        driver.find_element_by_name('p').send_keys(keywords, Keys.ENTER)
        time.sleep(10)
        links = driver.find_elements_by_css_selector('h3.title a')
        print("Geting Links...")
        pprint.pprint(dict([(i, _.get_attribute('href')) for i, _ in enumerate(links, 1)]))
        print("Finished SeoRobot Yahoo")

    finally:
        time.sleep(10)
        driver.quit()

if __name__ == "__main__":

    excuteBing('http://www.bing.com', 'bancolombia')
    excuteGoogle('http://www.google.com', 'bancolombia')
    excuteDuckDuck('https://duckduckgo.com/', 'bancolombia')
    excuteYahoo('https://www.yahoo.com/', 'bancolombia')