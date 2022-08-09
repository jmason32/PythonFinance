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
import DivBook

def main():
    # Find a finance API and connect
    # Using yahoo for test starter

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
    mybook = DivBook.DivBook(bookName)

    # Make a sheet
    mybook.addSheet(sheetName)

    #add header
    mybook.addMainHeader(sheetName)

    #save book
    mybook.saveBook()

    # create a PyStock object
    myStock = PyStock.PyStock("O")
    print(myStock.current_price)


class Row:
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data


"""
"""
if "__main__" == __name__:
    main()
