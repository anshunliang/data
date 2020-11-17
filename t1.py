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