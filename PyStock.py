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
        print(stockInfo)

        #Assign values to class instance
        self.name = stockInfo['longName']
        self.current_price = stockInfo['currentPrice']
        self.symbol = stockInfo['symbol']
        self.dividendYield = stockInfo['dividendYield']

        self.saveStockInfo()

        # self.symbol = stockInfo
        # self.name = tCompanyName
        # self.current_price = tPrice
        # self.dividend = tDiv
      
    # def __repr__(self):
    #     return f'Person(name={self.name}, age={self.age})'

    def saveStockInfo(self):
      # Open file 
      try:
        f = open("test.txt", encoding = 'utf-8')
        # perform file operations
      except:
        print("Not found")

    def getMainInfo(self):
      print(f'PyStock("symbol":{self.symbol}, "name":{self.name}, "current_price":{self.current_price}, "dy":{self.dividendYield})')
    

    def setPrice(self, price):
        self.current_price = price

    """
    getPrice
      Function returns stock price
    """

    def getPrice(self):
        return self.price
