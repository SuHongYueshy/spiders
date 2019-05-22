from scrapy.spiders import Spider # 爬虫模块
from scrapy import Request # 请求模块

class booksSpider(Spider):
    name = 'books' # 爬虫名称
    start_urls = ['https://books.toscrape.com/']

    # 爬虫功能
    def parse(self,response):
        print(response.text)
        # 数据提取功能