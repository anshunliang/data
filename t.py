# 写一个生成excel文件的代码并验证一下是否可用
import xlwt
workbook = xlwt.Workbook(encoding='utf-8')
sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)#给excel文件添加sheet
sheet1.write(0,0,'工位号')#在1行1列的单元格写入内容
#sheet1.write_merge(0,3,1,1,'合并')#合并单元格
sheet1.write(0,1,'时间')#在1行1列的单元格写入内容
sheet1.write(0,2,'测量值')#在1行1列的单元格写入内容
workbook.save('test.xls')