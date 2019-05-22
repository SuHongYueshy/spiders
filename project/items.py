import scrapy


class Doubantop250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
    score = scrapy.Field()
    people = scrapy.Field()
    words = scrapy.Field()
    pass