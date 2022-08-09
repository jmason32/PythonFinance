"""
Create a Workbook class
"""
from xlwt import Workbook


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
