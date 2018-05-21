import xlrd, xlwt
from xlutils import copy
book= xlwt.Workbook()
sh= book.add_sheet("Rahul")

for i in range (3):
  for j in range(3):
    data=raw_input("Enter Data:")
    v= sh.write(i,j,data)
book.save("new.xls")
print "Reading Value:"
book=xlrd.open_workbook("new.xls")
sheet= book.sheet_by_index(0)
for i in range(3):
    for j in range(3):
        v=sheet.cell(i,j).value
        print v," "
row= int(raw_input("Enter row to update:"))
col=raw_input("Col:")
data=raw_input("data:")
book1=copy.book
sh=book1.get_sheet(0)
sh.write(row,int(col),data)
book1.save("new.xls")
