"""
Python Finance 

  Aim for App
      To be able to take in a list of symbols ie. (O)
        Return data on stock 
        Save stock data 
        
    - Program can grab info about a specific stocks
    - Symbol
    - Company Name
    - Current stock price
        - Constantly updating

    Extra features to be debated
    
    - “databases” for users
        - Save off stocks
"""

# Imports
import yfinance as yf  # yahoo finance package, used to get stock info
import matplotlib.pyplot as plt  #ploting
import random as random
import xlsxwriter
from xlwt import Workbook

def main():
    # Find a finance API and connect
    # Using yahoo for test starter

    # data = yf.download('SPY', '2015-01-01', '2020-01-01')
    # Plot the close prices
    # data["Adj Close"].plot()
    # plt.show()

    # Retrieve from a list of symbols
    """
    Access list of symbols 
    
  """
    # https://pypi.org/project/yfinance/
    """
  Quick Start
    The Ticker module
      Use the ticker module to get info of stock 

      msft = yf.Ticker("MSFT")
      # get stock info
      msft.info
      
      # get historical market data
      hist = msft.history(period="max")
      
      # show actions (dividends, splits)
      msft.actions
      
      # show dividends
      msft.dividends
      msft.news
  """

    # Gather stock sylbols
    stockList = ["PSX"]

    # choose random from list

    stockSymbol = random.choice(stockList)

    stockSybmol = yf.Ticker(stockSymbol)
    stockInfo = stockSybmol.info

    # print(stockInfo)

    """
      Per access ask user if they want to add stock to excel file 
        Creates page with the stock symbol 
  
      From list of stocks you calulate compond intrest 
      Dividends
        Calulate how much needs to be bought in order to reach a certain dividend return 
      Analsisys 
    """

    """
    Look for excel file 
      create one if not there 
        columns:
          - Symbol 
          - Company Name 
          - Current Price 
          - Dividend 
          - Payout (Monthly/Quarterly/Yearly)
  
          https://xlsxwriter.readthedocs.io/tutorial01.html
    """

  
  
# Workbook is created
    # wb = Workbook()

    # sheet1 = wb.add_sheet('Sheet 1')

    # try:
    #   workbook = xlrd.open_workbook("Road_To_10.xlsx")
    # except FileNotFoundError:
    workbook = xlsxwriter.Workbook('Road_To_10.xlsx')

    #Create main worksheet
    worksheet = workbook.add_worksheet()

  
    # create a PyStock object 
    myStock = PyStock("O")
    print(myStock.current_price)


class PyStock:
  """
  TODO:
    Take in a ticker, 
      parse info for our needs 
        - company name 
        - current_price 
        - dividend

    https://polygon.io/docs/stocks/get_v3_reference_dividends
    Use this rest api to get frequency (monthly, quaterly, yearly)
        
  """
  """
  init 
  @param stockSymbol: stock to convert into class 
  """
  def __init__(self, stockSymbol):

    # Given a stock symbol, return an object with all stock attr.
    stockTicker = yf.Ticker(stockSymbol)

    #info contains lots of useful things 
    stockInfo = stockTicker.info

    #Assign values to class instance
    self.name = stockInfo['longName']
    self.current_price = stockInfo['currentPrice']
    self.symbol = stockInfo['symbol']
    self.dividendYield = stockInfo['dividendYield']
    
    # self.symbol = stockInfo
    # self.name = tCompanyName
    # self.current_price = tPrice
    # self.dividend = tDiv
    
  """
  setPrice
    This function will be used to set stock price
    @param price: updated price of stock to set 
  """
  def setPrice(self, price):
    self.current_price = price

  """
  getPrice
    Function returns stock price
  """
  def getPrice(self):
    return self.price
  


if "__main__" == __name__:
    main()
