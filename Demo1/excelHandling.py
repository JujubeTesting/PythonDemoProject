import xlrd
loc = "D:/PyhtonProject/TestData_Login.xlsx"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
rows = sheet.get_rows()
for i in range(rows):
    print(sheet.cell_value(i, 0))



