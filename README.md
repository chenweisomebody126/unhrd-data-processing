# unhrd-data-processing
Run the program:              
Just run command `python output.py`.      

Explanation of program:           
1) Scraped information:     
`stock_sheet.csv` is scraped from unhrd by scrapy package and it records stockpile information such as how many boxes of gloves in which place.            
2) Reference information:     
`multipliers_sheet` contains the data multiplication rule such as how many pairs of gloves in each box for this row.               
`location_sheet` contains all desired locations in order to avoid missing any location. Even though there is no item in this location, preserve the rows and show 0 instead there.
3) Output information:      
`output.csv` is the item-location information such as how many pairs of gloves (specific item) in which place (specific location).             

Note:     
Debug file contains a jupyter notebook for debugging which could be deleted in production environment.
