# coding=utf-8
# 功能：学生管理系统主窗口
# 作者：lhw
# 文件：Stu_Main.py

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pymysql
from Add_Stu import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(502, 319)
        self.tableWidget =QTableWidget(Form)
        self.tableWidget.setGeometry(QRect(30, 40, 341, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['学号','姓名','性别','年龄','班级'])

        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.splitter = QSplitter(Form)
        self.splitter.setGeometry(QRect(400, 50, 75, 191))
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setObjectName('splitter')
        self.pushButton_Add = QPushButton(self.splitter)
        self.pushButton_Add.setObjectName('pushButton_Add')    #'增加'按钮
        self.pushButton_del = QPushButton(self.splitter)
        self.pushButton_del.setObjectName('pushButton_del')  #'删除'按钮
        self.pushButton_edit = QPushButton(self.splitter)
        self.pushButton_edit.setObjectName('pushButton_edit')  #'编辑'按钮
        self.pushButton_exit = QPushButton(self.splitter)
        self.pushButton_exit.setObjectName('pushButton_exit')  #'退出'按钮
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(100)
        self.retranslateUi(Form)
        self.pushButton_Add.clicked.connect(self.AddStu)
        self.pushButton_del.clicked.connect(self.DelStu)
        self.pushButton_exit.clicked.connect(self.WinExit)
        self.tableWidget.itemClicked.connect(self.GetCurrentRow)

        #打开数据库
        self.conn = pymysql.connect(host='localhost',user='root',passwd='1234',db='student_db',port=3306,charset='utf8')
        #使用cursor()方法获取操作游标
        self.cursor=self.conn.cursor()
        self.showDataBase()#显示学生信息
        # QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self,Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate('Form','学生管理系统'))
        self.pushButton_Add.setText(_translate('Form','增加'))
        self.pushButton_del.setText(_translate('Form', '删除'))
        self.pushButton_edit.setText(_translate('Form', '编辑'))
        self.pushButton_exit.setText(_translate('Form', '退出'))


    def showDataBase(self):
        try:
            # 使用execute方法执行SQL语句
            self.cursor.execute('select * from student')
            results = self.cursor.fetchall()
            i=0
            # 获取所有记录列表
            for row in results:
                newItem = QTableWidgetItem(row[0])
                self.tableWidget.setItem(i,0,newItem)
                newItem = QTableWidgetItem(str(row[1]))
                self.tableWidget.setItem(i,1,newItem)
                newItem = QTableWidgetItem(str(row[2]))
                self.tableWidget.setItem(i, 2, newItem)
                newItem = QTableWidgetItem(str(row[3]))
                self.tableWidget.setItem(i, 3, newItem)
                newItem = QTableWidgetItem(str(row[4]))
                self.tableWidget.setItem(i, 4, newItem)
                i=i+1
                self.cursor.close()
        except:
            print("数据显示错误")

    def AddStu(self):             # 增加学生信息
        Add_Form = QDialog()
        ui_addstu = Ui_Dialog_AddStu()   #增加学生窗体
        ui_addstu.setupUi(Add_Form)
        Add_Form.show()       #显示添加学生窗体
        Add_Form.exec_()

    def GetCurrentRow(self,Item=None):     # 得到当前单击行的行数
        global stu_id,selectrow            # stu_id 当前学生的学号
        selectrow=self.tableWidget.currentRow()
        # 取出当前行的第一列"学号"
        selectitem = self.tableWidget.item(selectrow, 0)
        stu_id = selectitem.text()

    def DelStu(self):
        self.conn=pymysql.connect(host='localhost',user='root',passwd='1234',db='student_db',port=3306,charset='utf8')

        self.cursor=self.conn.cursor()

        sql = "delete from student where id='"+stu_id+"'"
        ok =QMessageBox.question(self,'信息提示窗口','确定删除该记录吗？',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        if ok == QMessageBox.Yes:
            try:
                self.cursor.execute(sql)
                self.conn.commit()
                self.tableWidget.removeRow(selectrow)
            except:
                self.conn.rollback()
                self.conn.close()
        else:
            return


    def WinExit(self):
        self.close()

if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)
    widget=QWidget()
    ui=Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())




