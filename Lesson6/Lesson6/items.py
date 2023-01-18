# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Compose

def process_price(value):
    money = 0
    
    if value:
        money = float(value[0].replace(' ',''))
        
    return money

def process_name(value):
    name = ''
    
    if value:
       for line in value:
        name +=  line.replace('\n','').strip()
        
    return name

class Lesson6ParserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor=Compose(process_name), output_processor=TakeFirst())
    price =  scrapy.Field(input_processor=Compose(process_price), output_processor=TakeFirst())
    cur =  scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field()
    url = scrapy.Field(output_processor=TakeFirst())
   
