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

users = ['estivensondrh@gmail.com','florezposadaedna@gmail.com','frankamilo@live.com','galaco0707@gmail.com',
         'garcia.echeverria@hotmail.com','gil1941@hotmail.com','giselamichel05@hotmail.com','greyliscolmenares12@gmail.com',
         'isabellapadillanadia@gmail.com','itztroller9k@gmail.com','jdlt5544@gmail.com','jesusarnedo720@gmail.com',
         'johannyquintero@ouhook.es','joseandresurbano76@gmail.com','jotapm16@hotmail.com','juandiegotch2526@gmail.com',
         'julianaramirez606@gmail.com','kalethdavidp2@gmail.com','karen.pbo2806@gmail.com','kevinzab123@gmail.com',
         'leal29523@gmail.com','leguiatovardanamarcela@gmail.com','losteletubis90@gmail.com','maurocarnabal@gmail.com',
         'mokarla2002@gmail.com','nubiafredy007@gmail.com','odamelo40@hotmail.com',
         'oscarlorduy12345@gmail.com','reyesaaa286@gmail.com','rowisong@hotmail.com','sararosales1602@gmail.com',
         'sierratinocosergioenrrique@gmail.com','sneidergonzalez.123@hotmail.com','stevencarranzanavarro@gmail.com',
         'susanaykaterin@hotmail.com','teamojheicol134@gmail.com','yenuar.galindo.madrid@hotmail.com',
         'yerles.angel@hotmail.com','yersproxxwtf13@hotmail.com','brochero134@gmail.com','jesusmartine312@gmail.com',
         'juancarlosmecino@gmail.com','kevinmsaguilar@gmail.com','angie040717@gmail.com','yoryeperez29@gmail.com',
         'bernatecalvo@gmail.com','karinaneira434@gmail.com','salazarmarimar.2001@gmail.com','elim6271@gmail.com',
         'dairisdimas20@gmail.com','mirleysdayana@gmail.com','camilablanco.124@gmail.com','leynervasquez14@gmail.com',
         'cristianamaris0@gmail.com','emelycolinajimenez@gmail.com','felixcarrillobarreto@gmail.com',
         'evitalevita3@gmail.com','yaisa0920@gmail.com','carolayrocha0@gmail.com','danielanassi0601@gmail.com',
         'wilfrandavidromerobonett@gmail.com','vpsb205@gmail.com','Ymoralestsi103@gmail.com','keity200209@gmail.com',
         'castrogarciaandrea2@gmail.com','davidmedina0715@gmail.com','lhernandezmercado101@gmail.com',
         'victormanuelarrieta2002@gmail.com','stivendaniel30@gmail.com','juandavidlora123@gmail.com',
         'arlinolave25@gmail.com','adriiortega034@gmail.com','bayueloana10@gmail.com','marlonpenamarmolejo@gmail.com',
         'kamiloospino03@gmail.com','avilamarilian@gmail.com','jadrycabarcas03@gmail.com','wendypaolaorozcobuelvas@gmail.com',
         'luisavanessa509@gmail.com','batistaherreraselene@gmail.com','oscaral221817@gmail.com','diomyc1020@outlook.com',
         'JulimarceBerdugo13@gmail.com','linajf@outlook.com','lruizinformatica@gmail.com','dilanlokura22@hotmail.com',
         'jrodriguez803@outlook.es','yurleis03@outlook.com','elidamoralez8@gmail.com','luzelenamercado8@gmail.com',
         'puellocarmen8@gmail.com','castrodiazharlin86@gmail.com','castrodiazharlin86@gmail.com','jdiazpajaro57@gmail.com',
         'diazpajaro29@gmail.com', 'angelismartnz@gmail.com','angelismartnz@gmail.com','araquedelacruz@gmail.com',
         'arianambz01@gmail.com','claudimar09576@gmail.com','cm4590107@gmail.com','davidbossio0808@gmail.com',
         'echegarretaalcireh@gmail.com','raimundito1@gmail.com','mariapamarti@gmail.com','marielacifuentes1903@gmail.com',
         'gustavoquin31@gmail.com', 'guerreroherreram@gmail.com','juanchoajo99@gmail.com', 'andreszcalle@gmail.com',
         'yinapatriciaberriosuarez@gmail.com','brianhelyc@gmail.com','johanavalderrmarenteria@gmail.com',
         'andresespinosag@yahoo.es', 'jacintoblancoberrio@hotmai.com', 'dadapepe@hotmail.com', 'andresfelipefernandez19@gmail.com',
         'jbuelvasnavarro@gmail.com ','irisbuelvascastro@gmail.com','musicodelahoz@hotmail.com','sandraalarconlengua@gmail.com ',
         'vanessa_zacal@hotmail.com','mariceanaya@gmail.com','julianjavier6428@gmail.com','jheisy0124outlook.es ',
         'estefanny3006@outlook.es','janiapaba14@hotmail.com','belygora@hotmail.com','paolaangelenfermeria@gmail.com',
         'secretariaapcbol@gmail.com', 'kelly.gonzalez@unicolombo.edu.co','shadocas08@hotmail.com','vidomelany19@gmail.com',
         'keylamdominguez@gmail.com', 'carlosguerreroporras@gmail.com ','rosmery1021@hotmail.com', 'katty.p_@hotmail.com',
         'caroymary19@gmail.com','cairo-1720@hotmail.com','hernandoquintana10m@gmail.com','andervl2022@gmail.com',
         'guschavez2008@hotmail.com', 'jaiferospino19@gmail.com ','victormrojas0910@gmail.com', 'jorgedanielbg@gmail.com',
         'catia2803@outlook.com', 'richardandres204@gmail.com', 'juancarlosangel@gmail.com', 'mrorly2006@hotmail.com',
         'veromanager_@hotmail.com', 'dianagarcia-1@hotmail.com', 'lisambla@hotmail.com','makle1992@gmail.com',
         'isaacperz01@gmail.com','fyciol@hotmail.com', 'julioespinosa@hotmail.com', 'patidelarosa2196@gmail.com',
         'samueljosebarrios1112@hotmail.com','angelamari29@hotmail.com','vperezr1@unicartagena.edu.co',
         'vasquezrossinestor@gmail.com','jaenpub19@gmail.com.es', 'onixdejesusbello@gmail.com','verónicaovis81@gmail.com',
         'monicacaromorales@gmai.com','kevindominguez01d@gmail.com','blancantillo20c@gmail.com','odiseo-xp@hotmail.com',
         'Elianajulio.2011@hotmail.com','catia2803@outlook.com','karinamer57@gmail.com','dikadika1@gmail.com',
         'garcianina29@outlook.com', 'sulami20@hotmail.com','laurapalencia@hotmail.com','johanaperez07@outlook.es',
         'caturoca@yahoo.es', 'marhyna.prens@hotmail.com', 'dra.lourdesvilladiego@hotmail.com', 'elibman11@hotmail.com',
         'etelvina.romero@tecnar.edu.co', 'estela.marrugo@tecnar.edu.co','danialuz_1993@hotmail.com',
         'yizethatenc163@gmail.com', 'luisreyesortega@hotmail.com','laurahernandezlager@hotmail.com',
         'acortinaa@yahoo.com', 'Yorkjey07@gmail.com', 'Rofer.2@hotmail.com', 'Ana.luklee@gmail.com','Alejandromt3080@hotmail.com',
         'aleja8109@hotmail.es','Santiagopereira50@gmail.com'
         ]

def titan():
    cont=0
    cont2=0
    url='https://titanes.noticias.caracoltv.com/user'
    try:
        driver.get(url)
        driver.maximize_window()
        time.sleep(3)

        for user in users:
            try:
                Login(user)
                cont2=cont2+1
            except:
                cont=cont+1
                print(user)
                driver.find_element_by_xpath('//*[@id="edit-name"]').clear()
                continue


    finally:
        print(cont)
        time.sleep(5)
        driver.quit()


def Login(user):
    driver.find_element_by_xpath('//*[@id="edit-name"]').send_keys(user)
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
