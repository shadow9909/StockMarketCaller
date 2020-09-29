import xlwt

DATA = (("Shares", "QTY", "Purchared Value", "Current Value", "NET" ))

wb = xlwt.Workbook()
ws = wb.add_sheet("My Sheet")
for i, row in enumerate(DATA):
    for j, col in enumerate(row):
        ws.write(i, j, col)
ws.col(0).width = 256 * max([len(row[0]) for row in DATA])
wb.save("Downloads/myworkbook.xls")
