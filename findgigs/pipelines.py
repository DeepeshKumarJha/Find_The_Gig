# useful for handling different item types with a single interface
import pandas
from itemadapter import ItemAdapter


class FindgigsPipeline:

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):

        # item['times'] True means this is the first time this program is running
        if item['times']:

            df = pandas.DataFrame(data=item['title'], columns=spider.name)

        else:
            pass

        return item

    def close_spider(self, spider):
        pass
