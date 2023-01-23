from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from spiders.InstaUserFollows import InstagramSpider


if __name__ == '__main__':
    crawler_settings =  get_project_settings()
    runner = CrawlerProcess(settings=crawler_settings)
    runner.crawl(InstagramSpider)
    runner.start()
