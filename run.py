import os, sys
from scrapy.crawler import CrawlerProcess
from findgigs.spiders import pph

if __name__ == "__main__":
    """
    -pph <search-term> will used for get the search term 

    For now this only works for if single word is entered after -pph
    """
    pph_search_term = ''
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-pph':
            pph_search_term = sys.argv[i+1].strip()
            break
    
    # print(f" we got : {pph_search_term}")

    peopleperhour = CrawlerProcess()
    peopleperhour.crawl(pph.PphSpider, pph_search = pph_search_term)
    peopleperhour.start()