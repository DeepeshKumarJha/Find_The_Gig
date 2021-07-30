import scrapy


class FindgigsItem(scrapy.Item):
    # define the fields for your item here like:

    title = scrapy.Field()
    link = scrapy.Field()

    times = scrapy.Field()
