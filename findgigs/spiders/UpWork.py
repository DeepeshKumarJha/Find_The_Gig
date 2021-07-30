import scrapy
from findgigs.items import FindgigsItem


class UpWorkSpider(scrapy.Spider):
    name = "UpWork"

# When I'm Requesting with headears it's not working but without it it's working fine
    # headers = {
    #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #     'accept-encoding': 'gzip, deflate, br',
    #     'accept-language': 'en-GB,en;q=0.9',
    #     'cache-control': 'no-cache',
    #     'pragma': 'no-cache',
    #     'referer': 'https://www.peopleperhour.com/',
    #     'sec-fetch-dest': 'document',
    #     'sec-fetch-mode': 'navigate',
    #     'sec-fetch-site': 'same-origin',
    #     'sec-fetch-user': '?1',
    #     'sec-gpc': '1',
    #     'upgrade-insecure-requests': '1'
    # }

    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'USER_AGENT': USER_AGENT,
    }

    def start_requests(self):

        for link in self.search:

            yield scrapy.Request(
                url=f"https://www.upwork.com/search/jobs/?q={link}",
                callback=self.parse,
                # headers=self.headers,
            )

    def parse(self, response):

        obj = FindgigsItem()

        gigs = response.xpath(
            "//div[@class='js-search-results m-0 p-0-top-bottom']/section")

        for gig in gigs:
            gig_title = gig.xpath(".//up-c-line-clamp/text()").extract_first()
            gig_time = ""
            gig_link = gig.xpath(
                ".//*[@class='p-sm-top-bottom']//a/@href").extract_first()
