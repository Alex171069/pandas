import pandas
import openpyxl

class xlsparse:

 xlsFile_sheet = pandas.read_excel('07_04_2023.xlsx', sheet_name='Лист1') # лист гораздо больше
 print(xlsFile_sheet)

