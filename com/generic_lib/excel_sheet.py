import xlrd
import sys, traceback

class ExcelSheet():

    def __init__(self):
        # self.rowNum = rowNum
        # self.colNum = colNum
        # self.sheetName = sheetName
        self.excelPath = "E:\Automation\BackUp\Git\Jabong\TestData.xlsx"

    def readExcelData(self,sheetName, rowNum, colNum):
        workbook = xlrd.open_workbook(self.excelPath)
        worksheet = workbook.sheet_by_name(sheetName)
#       for current_Row in range(worksheet.nrows):
        cellValue = worksheet.cell_value(rowNum, colNum)
        return cellValue

    def readData(self,testCaseId,sheetName):
            data = []
    #    try:
            workbook = xlrd.open_workbook("D:\Work_Space\Framework_Jabong\TestData.xlsx")
            worksheet = workbook.sheet_by_name(sheetName)
            print('Inside read data')
            for current_Row in range(worksheet.nrows):
                print ('Inside for loop')
                current_Id = str(worksheet.row(current_Row)[0])[7:16]
                print (current_Id)
                if current_Id == testCaseId:
                    print ('below curent id')
                    for current_cell in range(worksheet.ncols):
                        data.append(worksheet.cell_value(current_Row, current_cell))
                        print ('Data has been appended')
                    break
            return data

        #except:
            traceback.print_exception("there is some exception.")




