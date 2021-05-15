"""
use selenium to vist Yahoo finance and scrape request stock information
last update by Ilyass on 5/14/21
"""
from selenium import webdriver

geckodriver = '..\drive\geckodriver'
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
driver = webdriver.Firefox(executable_path=geckodriver, options=options)

#to cut down on code reuse a
def get_element(urlType, ticker, xpathLocation):
    #wait for page to load
    driver.implicitly_wait(5)
    #set the appropriate website url
    if urlType==Set_Stock:
        Set_Stock(ticker)
    elif urlType==Set_Stock_Adavanced:
        Set_Stock_Adavanced(ticker)
    #get request element from webpage
    current_Element = driver.find_element_by_xpath(xpathLocation).text
    print(current_Element)

def Set_Stock(ticker):
    driver.get('https://finance.yahoo.com/quote/'+ticker+'/')

def Set_Stock_Adavanced(ticker):
    driver.get('https://finance.yahoo.com/quote/'+ticker+'/key-statistics')

def Open_Price(Ticker):
    get_element(Set_Stock, Ticker , '//*[@id="quote-summary"]/div[1]/table/tbody/tr[2]/td[2]/span')

def Market_Cap(Ticker):
    get_element(Set_Stock, Ticker , '//*[@id="quote-summary"]/div[2]/table/tbody/tr[1]/td[2]/span')

def Market_Volume(Ticker):
    get_element(Set_Stock, Ticker , '//*[@id="quote-summary"]/div[1]/table/tbody/tr[7]/td[2]/span')

def Average_Market_Volume(Ticker):
    get_element(Set_Stock, Ticker , '//*[@id="quote-summary"]/div[1]/table/tbody/tr[8]/td[2]/span')

def Price_Earning_Ratio(Ticker):
    get_element(Set_Stock, Ticker , '//*[@id="quote-summary"]/div[2]/table/tbody/tr[3]/td[2]/span')

def One_Year_Estimate(Ticker):
    get_element(Set_Stock, Ticker , '//*[@id="quote-summary"]/div[2]/table/tbody/tr[8]/td[2]/span')

def FiftyTwo_Week_Low(Ticker):
    get_element(Set_Stock_Adavanced, Ticker , '//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[2]/div/div[1]/div/div/table/tbody/tr[5]/td[2]')

def FiftyTwo_Week_High(Ticker):
    get_element(Set_Stock_Adavanced, Ticker , '//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[3]/div[2]/div/div[1]/div/div/table/tbody/tr[6]/td[2]')



