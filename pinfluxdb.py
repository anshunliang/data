from influxdb import InfluxDBClient
import pandas as pd
from datetime import datetime,timedelta
'''
# 初始化（指定要操作的数据库）
client = InfluxDBClient('localhost', 8086, 'root', '123456', 't') 
print(client.get_list_database()) # 显示所有数据库名称
client.create_database('testdb') # 创建数据库
print(client.get_list_database()) # 显示所有数据库名称
client.drop_database('testdb') # 删除数据库
print(client.get_list_database()) # 显示所有数据库名称
'''
#连接指定数据库
client = InfluxDBClient('localhost', 8086, 'root', '123456', 't') 

#result = client.query('select * from results;')

#s=client.query('select "hostname" from results;').get_points()
#temp=pd.DataFrame(client.query('select * from results where value=1;').get_points())
temp=pd.DataFrame(client.query("select * from results where time>'2020-11-12T12:47:56.439917Z' and time<'2020-11-12T13:30:04.072731Z';").get_points())
x=temp.values.tolist()
print(x)
'''
print("Result: {0}".format(result))
print(result)
'''
for i in x:
    print(i)
