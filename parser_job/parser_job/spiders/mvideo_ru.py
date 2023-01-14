#Написать программу, которая собирает товары «В тренде» с сайта техники mvideo
#  и складывает данные в БД. Сайт можно выбрать и свой. 
# Главный критерий выбора: динамически загружаемые товары

import scrapy
from scrapy.http import HtmlResponse
from lxml import html
from pymongo import MongoClient
from pprint import pprint
import time

class MvideoRuSpider(scrapy.Spider):
    name = 'mvideo_ru'
    allowed_domains = ['pleer.ru']
    
    
    start_urls = ['https://www.pleer.ru/']
    client = MongoClient('127.0.0.1',27017)

    def parse(self, response: HtmlResponse):
        
       
      
        links = response.xpath('//a[@class="product-card product-card--sale"]/@href').getall()
     
        for link in links:
            time.sleep(3)
            yield  response.follow(link,callback=self.parse_data)

    def parse_data(self,response: HtmlResponse):
       
        product_name = response.xpath("//span[@class='product_title']//text()").getall()
        product_price = response.xpath("//div[@class='product_buy_buttons']/div[3]/div/div[1]/div[1]//text()").getall()
        

        product_struct = {
        'link' : response.url ,
        'product_name' : product_name,
        'product_price' : product_price
        }

        print(product_struct)
        db = self.client.db_pleer
        db.products.insert_one(product_struct)

       