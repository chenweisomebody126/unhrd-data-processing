
# coding: utf-8

import pandas as pd
import numpy as np
import os
# if stock_sheet.csv exist, remove it first
try:
    os.remove("./stock_sheet.csv")
except OSError:
    pass
#ask crawler to do the web scraping and save to stock_sheet.csv
os.system("scrapy runspider ./unhrd/spiders/unhrd_spider.py -o ./stock_sheet.csv")
#load scraped stock_sheet and two reference sheets called multiplier_sheet and location_sheet
stock_csv= './stock_sheet.csv'
multiplier_csv= './multiplier_sheet.csv'
location_csv = './location_sheet.csv'

stock_df = pd.read_csv(stock_csv)
multiplier_df = pd.read_csv(multiplier_csv)
location_df= pd.read_csv(location_csv)

#join stock df with multiplier df on the Item Code
stock_multiplier_df = pd.merge(stock_df, multiplier_df,on='Item_Code', how='outer')
#drop the items only appear in the stock report but not appear in the multiplier
stock_multiplier_df.dropna(subset=['Critical_Item'], inplace=True)
#In order to display items that only appear in the multiplier in the item_location table, repalce NaN with arbitrary location
stock_multiplier_df['Location'].fillna('Dubai', inplace=True)

#In order to avoid missing any location, join current table with full list of location
stock_multiplier_df = pd.merge(stock_multiplier_df, location_df,on='Location', how='outer')
#Similarily, replace Nan with arbitrary critical item
stock_multiplier_df['Critical_Item'].fillna('Bed nets', inplace=True)

#Now current table is guaranteed not missing any location, not missing any critical item and not including unnessary critical item
stock_multiplier_df['Multiplied_Quantity']= stock_multiplier_df['Quantity']* stock_multiplier_df['Multiplier']
stock_multiplier_df['Multiplied_Quantity'].fillna(0, inplace=True)

#aggregate number of item by Critical_Item and Location and pivot table
item_location_df= pd.pivot_table(stock_multiplier_df,index=["Critical_Item"],values=["Multiplied_Quantity"],
               columns=["Location"],aggfunc=[np.sum],fill_value=0,dropna= False)
#remove the first two level of indexs to match the format
item_location_df.columns = item_location_df.columns.droplevel([0,1])
#
item_location_df.columns.name=None
item_location_df.reset_index(inplace=True)
#save output table in csv format
item_location_df.to_csv("./output.csv")
