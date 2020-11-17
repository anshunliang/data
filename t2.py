import openpyxl
from openpyxl import Workbook
wb = Workbook()
# 激活 worksheet
ws = wb.active
# 数据可以直接分配到单元格中
ws['A1'] = 42
# 可以附加行，从第一列开始附加
ws.append([144, 244, 34])
ws.append([114, 124, 341])
# Python 类型会被自动转换


wb.save("sample.xlsx")

data = openpyxl.load_workbook("sample.xlsx")
print(data.get_named_ranges()) # 输出工作页索引范围
print(data.get_sheet_names()) # 输出所有工作页的名称
# 取第一张表
sheetnames = data.get_sheet_names()
table = data.get_sheet_by_name(sheetnames[0])
table = data.active
print(table.title) # 输出表名
nrows = table.max_row # 获得行数
ncolumns = table.max_column # 获得行数
values = ['E','X','C','E','L']
for value in values:
    table.cell(nrows+1,1).value = value
    nrows = nrows + 1
data.save("sample.xlsx")
