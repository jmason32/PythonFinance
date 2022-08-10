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


"""
    TODO: 
      Push code home from home to main branch
      Clean up 
      Branch out!!!
    
    
      Create page for specific stock
        SheetName = Stock Symbol - Company Name (O - Reality Income)
    
      Track dividend buys/earnings 
        Transaction
          Date 
          Price Bought At 
          Current Price 
          * Gain 
          Div Yield
          Div Amount $
    
          Total Row
      
    """

"""
  Function to add a stock sheet to workbook
  @param stockSymbol: Stock to create sheet for
"""
def addStockSheet(book, stockSymbol):
  # Create a sheet with the stock symbol being the name
  fileName = stockSymbol
  book.addSheet(fileName)

  #Header for sheet
  # stockHeader = ["Transaction Date", "Price Bought At",
  #               "# Shares", "Dividend Yield %", "Dividend Amount"]

  stockHeader = ["Transaction Date",	"Amount Sent",	"Dividend	Share Cost",	"Shares",	"Shares via Div",	"Shares Outright"]

  for title in stockHeader:
    pass

class Row:
    def __init__(self, x, y, data):
        self.x = x
        self.y = y
        self.data = data


"""
"""
if "__main__" == __name__:
    main()
