
from influxdb import InfluxDBClient
import time



w_json = [{
    "measurement": 'ta00',
    "time":171771 ,
    "tags": {
        'name': '名',
        'categories': '类'
        },
    "fields": {
        'price': "价",
        'unit': "单",
        }
    }]
# 写入数据库
client = InfluxDBClient('192.168.1.104', 8086,'root','123456',database='t')
print("start")

a=0
while True:
    
    client.write_points(w_json)
    a+=1
    if a>10000000:
        break
   
  
    print(a)
    w_json = [{
    "measurement": 'ta01',
    "time":a ,
    "tags": {
        'name': '名',
        'categories': '类'
        },
    "fields": {
        'price': "价",
        'unit': "单",
        }
    }]
print(over)
client.close()

