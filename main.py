import xlrd

workbook = xlrd.open_workbook("Data.xlsx")
sheet = workbook.sheet_by_name("Sheet1")
rows = sheet.nrows
print(rows)