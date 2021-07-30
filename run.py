import sys
import os
import pandas
from scrapy.crawler import CrawlerProcess
from findgigs.spiders import PeoplePerHour, UpWork, Freelancer


def check_for_csv_files():

    if not os.path.isfile('upto.csv'):
        # This means it is first time we running this program

        with open("upto.csv", "w+") as file_is_created:
            pass

        columns = ['PeoplePerHour', 'Freelancer', 'UpWork']
        df = pandas.DataFrame(columns=columns)

        df.to_csv("upto.csv")

        return True

    else:
        return False


if __name__ == "__main__":
    """
    -s <search-term> <search-term> <search-term> 
    This is how user can input the search term they want to get notify about,
    For now this only works for search-terms with single word
    """
    arr = sys.argv
    search = arr[arr.index('-s')+1:]

    peopleperhour = CrawlerProcess()
    upwork = CrawlerProcess()
    freelancer = CrawlerProcess()

    aboutFile = check_for_csv_files()

    # Insted of using "web scraping" use "scraping" only to search
    peopleperhour.crawl(PeoplePerHour.PeoplePerHourSpider,
                        search=search, aboutFile=aboutFile)

    upwork.crawl(UpWork.UpWorkSpider, search=search, aboutFile=aboutFile)

    freelancer.crawl(Freelancer.FreelancerSpider,
                     search=search, aboutFile=aboutFile)

    peopleperhour.start()
    upwork.start()
    freelancer.start()

    print("################ THE END ###################")
