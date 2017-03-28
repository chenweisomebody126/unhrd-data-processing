# unhrd-data-processing
Run the program:              
Just run command `python output.py`.      

Explanation of program:           
1) Scraped information:     
stock_sheet.csv is scraped from unhrd by scrapy package and it records item storage information such as how many boxes of gloves in which place.            
2) Reference information:     
multipliers_sheet is the data multiplication rule such as for each row in stock_sheet, how many pairs of gloves in the box in this row.
location_sheet is the location checking table to avoid missing any location even though there is no item, preserve the rows and show 0 instead.
3) Output information:      
output.csv is the item-location information such as how many pairs of gloves (specific item) in which place (specific location).             

Note:     
Debug file contains a jupyter notebook for debugging which could be deleted in production environment.
