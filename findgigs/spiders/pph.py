import scrapy
from scrapy.http import headers

class PphSpider(scrapy.Spider):
    name = "PeoplePerHour"

    headers = {
        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding' : 'gzip, deflate, br',
        'accept-language' : 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control' : 'no-cache',
        'cookie' : 'mid=1622229132099837900419604; PHPSESSID=d01a54e3420968ec4678e67852af7cb3',
        'pragma' : 'no-cache',
        'referer' : 'https://www.peopleperhour.com/',
        'sec-fetch-dest' : 'document',
        'sec-fetch-mode' : 'navigate',
        'sec-fetch-site' : 'same-origin',
        'sec-fetch-user' : '?1',
        'sec-gpc' : '1',
        'upgrade-insecure-requests' : '1'
    }

    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'


    custom_settings ={
        'ROBOTSTXT_OBEY':False,
        'USER_AGENT': USER_AGENT,
    }

    def start_requests(self):
        yield scrapy.Request(
            url=f'https://peopleperhour.com/freelance-{self.pph_search}-jobs',
            callback=self.parse,
            headers = self.headers
        )
    
    def parse(self, response):
        self.logger.info(f'################ First Gig : {response.xpath("//h6/a/text()").extract_first()}')