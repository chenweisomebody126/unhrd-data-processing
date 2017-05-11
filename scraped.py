
import os
from datetime import datetime
import schedule
import time
from reformated import reformat

def job():
    #ask crawler to do the web scraping and save to stock_sheet.csv
    date = datetime.now().strftime('%Y_%m_%d')
    stock_csv= './output_stock_sheets/%s_stock_sheet.csv'%date
    os.system("scrapy runspider ./unhrd/spiders/unhrd_spider.py -o ./%s" %stock_csv)
    reformat(stock_csv)


schedule.every().day.at("11:57").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
