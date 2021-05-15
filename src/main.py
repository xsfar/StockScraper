"""
driver to test the stock information scraping using Tesla(TSLA) as a test
last update by Ilyass on 5/14/21
"""
import scrape

#test scraping useing tesla ticker
scrape.Open_Price("TSLA")
scrape.Market_Cap("TSLA")
scrape.Market_Volume("TSLA")
scrape.Price_Earning_Ratio("TSLA")
scrape.One_Year_Estimate("TSLA")
