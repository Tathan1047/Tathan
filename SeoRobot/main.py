import os
import pprint
import time
import threading
import datetime
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


BASE_DIR = os.path.dirname(__file__)

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


# def excuteGoogle(url, keywords):
#     try:
#         print("Start SeoRobot Google")
#         driver2.get(url)  # Url de la pagina a Buscar
#         driver2.find_element_by_name('q').send_keys(keywords, Keys.ENTER)
#         links = driver2.find_elements_by_css_selector('.rc > .r a')
#         print("Geting Links...")
#         time.sleep(3)
#         pprint.pprint(dict([(i, _.get_attribute('href')) for i, _ in enumerate(links, 1)]))
#         print("Finished SeoRobot Google")
#
#     finally:
#         time.sleep(10)
#         driver2.quit()
#
#
# def excuteBing(url, keywords):
#     try:
#         print("Start SeoRobot Bing")
#         driver3.get(url)  # Url de la pagina a Buscar
#         driver3.find_element_by_name('q').send_keys(keywords, Keys.ENTER)
#         links = driver3.find_elements_by_css_selector('.b_algo a')
#         print("Geting Links...")
#         time.sleep(3)
#         pprint.pprint(dict([(i, _.get_attribute('href')) for i, _ in enumerate(links, 1)]))
#         print("Finished SeoRobot Bing")
#
#     finally:
#         time.sleep(10)
#         driver3.quit()
#
#
# def excuteDuckDuck(url, keywords):
#     try:
#         print("Start SeoRobot DuckDuck")
#         driver4.get(url)  # Url de la pagina a Buscar
#         driver4.find_element_by_name('q').send_keys(keywords, Keys.ENTER)
#         links = driver4.find_elements_by_css_selector('.result__title a')
#         print("Geting Links...")
#         time.sleep(3)
#         pprint.pprint(dict([(i, _.get_attribute('href')) for i, _ in enumerate(links, 1)]))
#         print("Finished SeoRobot DuckDuck")
#
#     finally:
#         time.sleep(10)
#         driver4.quit()
#
#
# def excuteYahoo(url, keywords):
#     try:
#         print("Start SeoRobot Yahoo")
#         driver.get(url)  # Url de la pagina a Buscar
#         driver.find_element_by_name('p').send_keys(keywords, Keys.ENTER)
#         time.sleep(10)
#         links = driver.find_elements_by_css_selector('h3.title a')
#         print("Geting Links...")
#         pprint.pprint(dict([(i, _.get_attribute('href')) for i, _ in enumerate(links, 1)]))
#         print("Finished SeoRobot Yahoo")
#
#     finally:
#         time.sleep(10)
#         driver.quit()

users = ['diomyc1020@outlook.com', 'JulimarceBerdugo13@gmail.com', 'luisangelparra@hotmail.com',
'mromero803@outlook.es', 'linajf@outlook.com','lruizinformatica@gmail.com','dilanlokura22@hotmail.com',
'jrodriguez803@outlook.es', 'yurleis03@outlook.com', 'elidamoralez8@gmail.com', 'luzelenamercado8@gmail.com',
'puellocarmen8@gmail.com', 'jaiderllamab@hotmail.com','yimilethb@gmail.com', 'castrodiazharlin86@gmail.com',
'taliaquintero.18@hotmail.com', 'jdiazpajaro57@gmail.com', 'diazpajaro29@gmail.com', 'jcastillav24@gmail.com',
'hectoralfonsomart8@gmail.com', 'yuvadyb@gmail.com','sanchezestada847@gmail.com'

         ]

def titan():
    url='https://titanes.noticias.caracoltv.com'
    try:
        driver.get(url)
        driver.maximize_window()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[2]/header/div[1]/div/div/div[2]/div/div[1]/div/a[1]').click()

        time.sleep(3)

        for user in users:
            Login(user)


    finally:
        time.sleep(5)
        driver.quit()


def Login(user):
    driver.find_element_by_xpath('//*[@id="edit-name"]').send_keys(user)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="edit-pass"]').send_keys('franktitanes', Keys.ENTER)
    time.sleep(3)
    driver.find_element_by_xpath(
        '/html/body/div[2]/div[2]/main/div[2]/div[2]/div[1]/div/div[1]/div/div/a/img').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="voto"]').click()
    time.sleep(3)
    driver.refresh()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/header/div[1]/div/div/div[2]/div/div[1]/div/a').click()
    driver.find_element_by_xpath('/html/body/div[2]/header/div[1]/div/div/div[2]/div/div[1]/div/a[1]').click()


tiempo_ini= datetime.datetime.now()

t1 = threading.Thread(target=titan, args= ())
#t2 = threading.Thread(target=titan1, args=('https://titanes.noticias.caracoltv.com','mh550348@gmail.com','franktitanes'))




if __name__ == "__main__":

    t1.start()
    #t2.start()

    #t2.join()


    tiempo_fin = datetime.datetime.now()
    print("Process Time" + str(tiempo_fin.second - tiempo_ini.second))
    print("Listo Todos Los Votos")

    # excuteBing('http://www.bing.com', 'bancolombia')
    #excuteGoogle('http://www.google.com', 'esperanzagomez')
    # excuteDuckDuck('https://duckduckgo.com/', 'bancolombia')
    # excuteYahoo('https://www.yahoo.com/', 'bancolombia')

    # titan('https://titanes.noticias.caracoltv.com','jmmdaya@gmail.com','jmm1047384159')
