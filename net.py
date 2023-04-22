import pandas
import openpyxl

class xlsparse:
    
 def __init__(self, fileXls, sheet, ucols):
     self.fileXls = fileXls   # файл .xls для обработки 
     self.sheet = sheet       # лист который читается 
     self.ucols = ucols       # взять перечисленные калонки строкой
     
 def pars(self):    
  xlsFile_sheet = pandas.read_excel(self.fileXls, sheet_name=self.sheet, usecols=self.ucols) # лист гораздо больше
  FileDataF = xlsFile_sheet.head()
  print(FileDataF)


Xfile=xlsparse('07_04_2023.xlsx','Лист1','A:G')
Xfile.pars()