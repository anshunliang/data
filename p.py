# -*- coding:utf-8 -*-
import sys,_thread,pymysql
import xlwt
import random
import socket
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel,QPushButton,QComboBox
import snap7
from snap7.util import *
from snap7.snap7types import *
from PyQt5.QtGui import QIcon
import time,csv

# 连接database
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    database="testdb"
    )
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
# 得到一个可以执行SQL语句并且将结果作为字典返回的游标
#cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)





#读取函数d
def readd():
    plc=snap7.client.Client()
    plc.connect("192.168.0.1",rack=0,slot=1)
    s=plc.read_area(0x84,1,0,20)
    
    xx=''
    for i in range(5):
        xx=xx+str(get_real(s,i*4))+"  "
    print(xx)
    ex.test.setText(xx)
    #self.test.setText(xx)


##使用TCP向go服务器发送消息，并接收前端消息
def print_time( threadName, delay):

    global tcp_server
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server.bind(("192.168.0.3", 5000))
    tcp_server.listen(20)
    global tcp_client
    global tcp_client_address

    print("wait")
    tcp_client, tcp_client_address= tcp_server.accept()  #程序会在这一步等待客户端连接，有客户端连接后，才会继续运行下去
    _thread.start_new_thread(js, ("Thread-2", 4, ) )     #开启一个线程，用于接收go服务器发来的消息
    count = 0
    while count<5:
        #tcp_client, tcp_client_address= tcp_server.accept()
        send_data1 = "好好的好的，好的，消息已收到的，消息已收到"+str(random.randint(0,10))
        global gdata

        send_data=gdata.encode(encoding = "utf-8")
        print(gdata)
        gdata=""
        print(sys.getsizeof(send_data))
        tcp_client.send(send_data)
        time.sleep(1)

       
               

# 创建两个线程
def js(threadName, delay):
    global tcp_client
    while True:
        if tcp_client:
            while True:
                print("chunjian")
                data= tcp_client.recv(1024).decode('utf-8') 
                print(data)
                time.sleep(1)
                    
           



#class Example(QWidget):
class Example(QMainWindow):
    

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(1000, 650)
        self.setWindowTitle('数据后处理')

        exitAction = QAction(QIcon('exit.png'), '&退出', self)       
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('退出软件')
        exitAction.triggered.connect(self.close)

        bxitAction = QAction(QIcon('exit.png'), '&帮助', self)       
        bxitAction.setShortcut('Ctrl+H')
        bxitAction.setStatusTip('帮助文档')
        bxitAction.triggered.connect(self.close)
 
        #self.statusBar()
        #self.statusBar.setStyleSheet("background-color:gray")
        menubar = self.menuBar()
        aMenu = menubar.addMenu('&菜单')
        aMenu.addAction(exitAction)
        aMenu.addAction(bxitAction)


        
        
        #self.test.setText('测试用')

        #PLC地址
        # 实例化QLabel对象，文本显示
        self.plcip = QLabel(self)
        # 设置文本标签的位置和大小
        self.plcip.setGeometry(0, 70, 200, 20)
        # 通过通道给文本标签赋值
        #self.line_edit.textChanged.connect(self.label.setText)
        str='数据库服务器地址及其端口'
        self.plcip.setText(str)

        # 实例化QLineEdit对象，文本输入框,输入PLC的IP地址
        self.plc_ip = QLineEdit(self)
        self.plc_ip.setGeometry(200, 70, 320, 20)  #位置，大小


        #sql语句
        self.dbnumber=QLabel(self)
        self.dbnumber.setGeometry(5,150,200,20)
        self.dbnumber.setText('sql语句')

        # 实例化QLineEdit对象，文本输入框,输入PLC的IP地址
        self.t99 = QLineEdit(self)
        self.t99.setGeometry(150, 150, 320, 20)  #位置，大小


        #DB号常量
        self.dbnumber=QLabel(self)
        self.dbnumber.setGeometry(5,120,200,20)
        self.dbnumber.setText('工位号')
        #DB号输入框
        self.dblen=QLineEdit(self)
        self.dblen.setGeometry(50, 120, 60, 20)

        #读取的字节数
        self.readlen=QLabel(self)
        self.readlen.setGeometry(150,120,200,20)
        self.readlen.setText("起始时间：")
        #读取长度输入框
        self.read_len=QLineEdit(self)
        self.read_len.setGeometry(250,120,100,20)


        #读取的字节数
        self.readlen=QLabel(self)
        self.readlen.setGeometry(400,120,200,20)
        self.readlen.setText("结束时间：")
        #读取长度输入框
        self.read_len=QLineEdit(self)
        self.read_len.setGeometry(500,120,100,20)
        
        #开始读取按钮
        self.start = QPushButton(self)
        self.start.setText("开始读取")         #按钮文本
        self.start.move(80,250)                   #按钮位s置
        self.start.clicked.connect(self.dq)
 
        #用于展示读取到的数据
        self.test = QLabel(self)
        self.test.setGeometry(0, 300, 800, 200)
        self.test.setStyleSheet("background-color:gray")


        self.dbnumber1=QLabel(self)
        self.dbnumber1.setGeometry(0,550,500,20)
        self.dbnumber1.setText("select id,salary  from db1 where name=zhangsan; zhangsan加冒号")

        self.show()
    
    def dq(self):



        # 定义要执行的SQL语句
        #sql = """select * from db1;"""
        #sql = """select * from db1 where salary=19990300;"""
        # 执行SQL语句
        sql=self.t99.text()
        cursor.execute(sql)
        #print(cursor.fetchall())
        #sex =cursor.fetchall()[0][1]
        #print(type(cursor.fetchall()))
        #self.test.setText(sex)


        workbook = xlwt.Workbook(encoding='utf-8')
        sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)#给excel文件添加sheet
        sheet1.write(0,0,'工位号11')#在1行1列的单元格写入内容
        #sheet1.write_merge(0,3,1,1,'合并')#合并单元格
        sheet1.write(0,1,'时间')#在1行1列的单元格写入内容
        sheet1.write(0,2,'测量值')#在1行1列的单元格写入内容
        a=1
        for i in cursor.fetchall():
            sheet1.write(a,0,i[0])#在1行1列的单元格写入内容
            sheet1.write(a,1,i[1])#在1行1列的单元格写入内容
            #sheet1.write(a,2,i[2])#在1行1列的单元格写入内容
            a=a+1
            print(i)
        print(a)
        workbook.save('test.xls')


    #测试函数
    def seeet(self):
        sex = self.plc_ip.text()
        self.test.setText(sex)




       

   
    


        
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())