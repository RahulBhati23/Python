import xlrd
file_location="C:/Users/Administrator/Desktop/New Microsoft Office Excel Worksheet.xlsx"
workbook=xlrd.open_workbook(file_location)
sheet=workbook.sheet_by_index(0)

g = sheet.cell(1,1).value
print g

print sheet.nrows
print sheet.ncols
for i in range(sheet.nrows):
 for j in range(sheet.ncols):
     cell_value=sheet.cell(i,j).value
     print cell_value
     
