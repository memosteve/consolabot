import time
from selenium import webdriver
import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager
import tweepy
from datetime import datetime

now = datetime.now()
timestamp = datetime.timestamp(now)

timestamp=str(timestamp)

# Credenciales del Twitter
auth = tweepy.OAuthHandler("zCJnlIyjzIdbGcX0gGlTEJXY1", 
    "rZJowVAdD4vX9ERbrBPqFY4XCO2Io113lK28YbdhNqWtjbC4BI")
auth.set_access_token("1308175947024146432-9OZCLgWA9SxIyw0im7EF22xOXHUpwK", 
    "jAspLz5xteYglaCTmqiMRRhpteQbeoNHF3WEFEbt2TQsB")

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

intro= "Precio de "
final= " En el link "
precio_digital=11499
precio_normal=13999
deal=" es una Oferta"

GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.binary_location = GOOGLE_CHROME_PATH

driver = webdriver.Chrome(execution_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
link= 'https://www.elpalaciodehierro.com/playstation-consola-playstation-5-825-gb-blanco-41282468.html'
driver.get(link);
driver.implicitly_wait(10)
Nombre = driver.find_element_by_class_name('b-product_main_info-name').text
Precio = driver.find_element_by_class_name('b-product_price-value').text
compara= Precio.replace(',','')
compara= compara.replace('MXN','')
if "digital" in Nombre or "Digital" in Nombre:
	if float(compara.replace('$',''))<precio_digital:
		deal= " es una Oferta"
	else:
		deal= " no es una Oferta"
else: 
	if float(compara.replace('$',''))<precio_normal:
		deal= " es una Oferta"
	else:
		deal= " no es una Oferta"

twitt= intro+Nombre+" es de "+Precio+deal+final+link+" "+timestamp
# print(twitt)

api.update_status(status=twitt)

link= 'https://www.sears.com.mx/producto/233159/preventa-consola-playstation-5/'
driver.get(link);
driver.implicitly_wait(10)
Nombre = driver.find_element_by_xpath('//html/body/div[5]/div/div[1]/div[1]/div[2]/div[1]/h1').text
Precio = driver.find_element_by_class_name('price').text
compara= Precio.replace(',','')
compara= compara.replace('MXN','')
if "digital" in Nombre or "Digital" in Nombre:
	if float(compara.replace('$',''))<precio_digital:
		deal= " es una Oferta"
	else:
		deal= " no es una Oferta"
else: 
	if float(compara.replace('$',''))<precio_normal:
		deal= " es una Oferta"
	else:
		deal= " no es una Oferta"

twitt= intro+Nombre+" es de "+Precio+deal+final+link+" "+timestamp
# print(twitt)
api.update_status(status=twitt)

link= 'https://www.sanborns.com.mx/resultados/q=playstation%205/1'
driver.get(link);
driver.implicitly_wait(10)
Nombre = driver.find_element_by_xpath('//html/body/main/section/div[2]/div/div[2]/div[1]/article[1]/div/a/div[1]').text
Precio = driver.find_element_by_class_name('infoDesc').text
compara= Precio.replace(',','')
compara= compara.replace('MXN','')
if "digital" in Nombre or "Digital" in Nombre:
	if float(compara.replace('$',''))<precio_digital:
		deal= " es una Oferta"
	else:
		deal= " no es una Oferta"
else: 
	if float(compara.replace('$',''))<precio_normal:
		deal= " es una Oferta"
	else:
		deal= " no es una Oferta"

twitt= intro+Nombre+" es de "+Precio+deal+final+link+" "+timestamp
# print(twitt)
api.update_status(status=twitt)

link= 'https://www.sams.com.mx/search/Ntt=%22Playstation-5%22'
driver.get(link);
driver.implicitly_wait(10)
Nombre = driver.find_element_by_class_name('item-name').text
Precio = driver.find_element_by_class_name('normal').text
compara= Precio.replace(',','')
compara= compara.replace('MXN','')
if "digital" in Nombre or "Digital" in Nombre:
	if float(compara.replace('$',''))<precio_digital:
		deal= " es una Oferta"
	else:
		deal= " no es una Oferta"
else: 
	if float(compara.replace('$',''))<precio_normal:
		deal= " es una Oferta"
	else:
		deal= " no es una Oferta"

twitt= intro+Nombre+" es de "+Precio+deal+final+link+" "+timestamp
api.update_status(status=twitt)
driver.quit()


