import xlrd
loc = "D:/PyhtonProject/TestData_Login.xlsx"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
#rows = sheet.get_rows(1)
print(sheet.cell_value(1,0))
print(sheet.nrows)
print(sheet.ncols)
print(sheet.row_values(3))
for i in range(sheet.nrows):
    print(sheet.cell_value(i,0))
    print(sheet.cell_value(i, 1))
    print(sheet.cell_value(i, 2))



