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
import PyStock
import DivBook as DB
import pandas as pd


def main():
    # Find a finance API and connect
    # Using yahoo for test starter

    # Retrieve from a list of symbols
    """
    Access list of symbols 
    
    """
    # https://pypi.org/project/yfinance/
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

    # Create workbook
    bookName = "DividendWorkBook"

    # #Create Workbook
    mybook = DB.DivBook(bookName)
    # addRoadnHeader(mybook)
    # # # Add stock to profolio
    mybook.addMainHeaderSheet()

    mybook.addStockSheet("O")
    
    # mybook.addStockToMain()

    #save book
    # mybook.saveBook()

    # mybook.read_sheet("RoadTo10")

    # mybook.getMainStockContent()

    # # create a PyStock object
    # myStock = PyStock.PyStock("O")
    # print(myStock.current_price)

def addRoadnHeader(mybook: DB):
  sheetName = "RoadTo10"
  #opn book 
  mybook.open_book(reader = False)

  #try and get sheet
  try:
    mybook.book.get_worksheet_by_name(sheetName)
    print("Sheet exists")
  except KeyError:
    # # Make a sheet
    mybook.addSheet(sheetName)

    # # #add header
    mybook.addMainHeader(sheetName)

  mybook.saveBook()
   

class Row:
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data


"""
"""
if "__main__" == __name__:
    main()
