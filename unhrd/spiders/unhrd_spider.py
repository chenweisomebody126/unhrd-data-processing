import scrapy
from scrapy.shell import inspect_response


class UNHRDSpider(scrapy.Spider):
    name = 'UNHRD'
    handle_httpstatus_list = [500]
    #allowed_domains= ["www.who.int/entity/mediacentre/news/releases"]
    allowed_domains= ["unhrd.org"]
    start_urls = ['http://unhrd.org/page/real-time-stock-report-results?hub%5B%5D=GHHD&hub%5B%5D=ITHD&hub%5B%5D=DJHD&hub%5B%5D=AEHD&hub%5B%5D=ESHD&hub%5B%5D=PAHD&hub%5B%5D=MYHD']

    def parse(self, response):
        #inspect_response(response,self)
        #print "search"
        for tr in response.xpath('//table[@class="table table-responsive table-striped"]//tbody/tr'):
            row= tr.xpath('td//text()').extract()
            #inspect_response(response,self)

            if len(row)==5:
                print row[0], row[1]

                yield {
                    'Item_Code': row[0],
                    'Description': row[1],
                    'Quantity': int(row[2].replace(',', '')),
                    'Owner': row[3],
                    'Location': row[4],
                }
