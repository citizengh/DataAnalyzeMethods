#Взять любую категорию товаров на сайте Леруа Мерлен (если не будет работать, возьмите castorama.ru). Собрать следующие данные:
#● название;
#● все фото;
#● ссылка;
#● цена.

#Реализуйте очистку и преобразование данных с помощью ItemLoader. Цены должны быть в виде числового значения.


import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
from items import  Lesson6ParserItem

class LeroymerlinRuSpider(scrapy.Spider):
    name = 'leroymerlin_ru'
    allowed_domains = ['castorama.ru']
  #  start_urls = ['https://www.castorama.ru/paint/enamels/']
    start_urls = ['https://www.castorama.ru/lighting/interior-lighting/floor-lamps-and-lampshades/']

   

    def parse(self, response: HtmlResponse):
        links = response.xpath("//a[@class = 'product-card__img-link']")
        
        for link in links:
          
            yield response.follow(link, callback=self.parse_data)


    def parse_data(self, response: HtmlResponse):
       # print(response.xpath("//h1/text()"))
        loader = ItemLoader(item=Lesson6ParserItem(), response=response)
        loader.add_xpath('name', "//h1/text()")
        loader.add_xpath('price', "//div[@class='add-to-cart__price js-fixed-panel-trigger']/div/div/div/div/span/span/span/span[1]/text()")
        loader.add_xpath('cur', "//div[@class='add-to-cart__price js-fixed-panel-trigger']/div/div/div/div/span/span/span/span[2]/text()")
       # loader.add_xpath('photos', "//div[@class='js-zoom-container']/img/@src")

       # loader.add_xpath('photos',"//div[@class='product-media__thumbs']/div/ul/li/img/@src | //div[@class='product-media__thumbs']/div/ul/li/img/@srcset")
        loader.add_xpath('photos',"//ul[@class='swiper-wrapper']/li//img/@data-src | //ul[@class='swiper-wrapper']/li//img/@data-srcset")
        loader.add_value('url', response.url)
        yield loader.load_item()

