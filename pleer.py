from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient
import time

client = MongoClient('127.0.0.1',27017)

s = Service('./chromedriver')

chromeOptions = Options()
chromeOptions.add_argument('start-maximized')


driver = webdriver.Chrome(service=s, options=chromeOptions)
driver.implicitly_wait(10)
driver.get('https://www.pleer.ru/')


i = 0
while i < 10:

    goods = driver.find_elements(By.XPATH, '//a[@class="product-card product-card--sale"]')

    j = 1
    while j < 5:
        product_name = goods[(j)*(i+1)].find_element(By.XPATH, ".//h3[@class='product-card__title']").text
        product_price = goods[(j)*(i+1)].find_element(By.XPATH,".//div[@class='product-card__price']").text
        
        product_struct = {
        'product_name' : product_name,
        'product_price' : product_price
        }

        print(product_struct)
        db = client.db_pleer
        db.products.insert_one(product_struct)
        
        print(product_name, product_price)
        j+=1

    wait = WebDriverWait(driver, 10)
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='slider__arrow js-slider-arrow-next']")))
    next_button.click()
    i += 1





#goods = driver.find_elements(By.XPATH, './/a[@class="product-card product-card--sale"]')

#for good in goods:
 #   product_name = good.find_element(By.XPATH, ".//h3[@class='product-card__title']").text
 #   product_price = good.find_element(By.XPATH,".//div[@class='product-card__price']").text
    
    print(product_name, product_price)

