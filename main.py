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
from multiprocessing.pool import INIT
from typing import List
import yfinance as yf  # yahoo finance package, used to get stock info
import matplotlib.pyplot as plt  #ploting
import random as random
import xlsxwriter
from xlwt import Workbook

import pandas as pd
from xlrd import open_workbook

import xlwt
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

    #   # Workbook is created
    # wb = Workbook()

    # # add_sheet is used to create sheet.
    # sheet1 = wb.add_sheet('RoadTo10')

    # addRow(x,y,'')

    # sheet1.write(0, 0, 'Symbol')
    # sheet1.write(0, 1, 'Company Name')
    # sheet1.write(0, 2, '% Dividend Yeild')
    # sheet1.write(0, 3, 'Current Price')
    # sheet1.write(0, 4, 'Payout Per Stock')
    # sheet1.write(0, 5, 'Road to 10')
    # sheet1.write(0, 6, 'Shares')
    # sheet1.write(0, 7, 'Amount')
    # sheet1.write(0, 8, 'Dividend Return')

    # # 'Total Row'
    # # Has to move dynamically as you add stocks

    # sheet1.write(26, 0, 'Total')

    # wb.save('DividendWorkBook.xls')

    # Workbook is created
    # wb = Workbook()

    # sheet1 = wb.add_sheet('Sheet 1')

    # try:
    #   workbook = xlrd.open_workbook("Road_To_10.xlsx")
    # except FileNotFoundError:

    # Create workbook
    bookName = "DividendWorkBook"
    sheetName = "RoadTo10"

    #Create Workbook
    mybook = DivBook(bookName)

    # Make a sheet
    mybook.addSheet(sheetName)

    #add header
    mybook.addMainHeader(sheetName)

    #save book
    mybook.saveBook()

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


class Row:
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data


"""
Create a Workbook class
"""


class DivBook:

    bookName = ""

    def __init__(self, name):
        self.divBook = Workbook()
        self.bookName = name

    """
  setActiveSheet
  """

    def setActiveSheet(self, sheet):
        return self.divBook.set_active_sheet(sheet)

    """
  addData
  """

    def addData(self, sheet, rows):
        for row in rows:
            sheet.write(row.x, row.y, row.data)

    """
  addSheet 
    @param sheetTitle: title of sheet to be added
  """

    def addSheet(self, sheetTitle):
        sheet = self.divBook.add_sheet(sheetTitle)

    """
  saveBook
    @param fileName: fileName to save book as 
  """

    def saveBook(self):
        return self.divBook.save(self.bookName + ".xls")

    """
  addMainHeader
  """

    def addMainHeader(self, sheetName):
        sheet = self.divBook.get_sheet(sheetName)

        headerTitle = [
            "Symbol", "Company Name", "% Dividend Yeild", "Current Price",
            "Payout Per Stock", "", "Road to 10", "Shares #", "Amount $",
            "Dividend Return $"
        ]

        for i, title in enumerate(headerTitle):
            print("Prining out {}".format(title))
            # self.addData(sheet, (x : 0, y: i, data : title))


if "__main__" == __name__:
    main()
