"""
Create a Stock Object class
"""
import yfinance as yf

class PyStock:
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
