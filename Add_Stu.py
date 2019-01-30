# coding=utf-8
# 功能：增加学生信息主窗体
# 作者：lhw
# 文件：Add_Stu.py


from PyQt5 import QtCore,QtGui,QtWidgets
import pymysql

class Ui_Dialog_AddStu(object):
    def setupUi(self,Dialog_AddStu):
        Dialog_AddStu.setObjectName('Dialog_AddStu')
        Dialog_AddStu.resize(400, 300)
        self.form = Dialog_AddStu
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog_AddStu)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 40, 210, 253))
        self.gridLayoutWidget.setObjectName('gridLayoutWidget')
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName('gridLayout')
        self.label_sex = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_sex.setObjectName('label_sex')
        self.gridLayout.addWidget(self.label_sex, 3, 0, 1, 1)
        self.label_name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_name.setObjectName('label_name')
        self.gridLayout.addWidget(self.label_name, 2, 0, 1, 1)
        self.lineEdit_id = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_id.setObjectName('lineEdit_id')
        self.gridLayout.addWidget(self.lineEdit_id, 1, 1, 1, 1)
        self.label_age = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_age.setObjectName('label_age')
        self.gridLayout.addWidget(self.label_age, 4, 0, 1, 1)
        self.lineEdit_age = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_age.setObjectName('lineEdit_age')
        self.gridLayout.addWidget(self.lineEdit_age, 4, 1, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_name.setObjectName('lineEdit_name')
        self.gridLayout.addWidget(self.lineEdit_name, 2, 1, 1, 1)
        self.label_id = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_id.setObjectName('label_id')
        self.gridLayout.addWidget(self.label_id, 1, 0, 1, 1)
        self.label_class = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_class.setObjectName('label_class')
        self.gridLayout.addWidget(self.label_class, 5, 0, 1, 1)
        self.lineEdit_class = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_class.setObjectName('lineEdit_class')
        self.gridLayout.addWidget(self.lineEdit_class, 5, 1, 1, 1)
        self.comboBox_sex = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_sex.setObjectName('comboBox_sex')
        self.comboBox_sex.addItem('')
        self.comboBox_sex.addItem('')
        self.gridLayout.addWidget(self.comboBox_sex, 3, 1, 1, 1)
        self.pushButton_OK = QtWidgets.QPushButton(Dialog_AddStu)
        self.pushButton_OK.setGeometry(QtCore.QRect(290, 50, 75, 41))
        self.pushButton_OK.setObjectName('pushButton_OK')
        self.pushButton_exit = QtWidgets.QPushButton(Dialog_AddStu)
        self.pushButton_exit.setGeometry(QtCore.QRect(290, 100, 75, 41))
        self.pushButton_exit.setObjectName('pushButton_exit')
        self.pushButton_OK.clicked.connect(self.InsertStu)
        self.pushButton_exit.clicked.connect(self.AddWinExit)
        #self.pushButton_OK.clicked.connect(self.close)
        self.retranslateUi(Dialog_AddStu)
        QtCore.QMetaObject.connectSlotsByName(Dialog_AddStu)

    def retranslateUi(self, Dialog_AddStu):
        _translate = QtCore.QCoreApplication.translate
        Dialog_AddStu.setWindowTitle(_translate('Dialog_AddStu', '增加学生信息'))
        self.label_sex.setText(_translate('Dialog_AddStu', '性别：'))
        self.label_name.setText(_translate('Dialog_AddStu', '姓名：'))
        self.label_age.setText(_translate('Dialog_AddStu', '年龄：'))
        self.label_id.setText(_translate('Dialog_AddStu', '学号：'))
        self.label_class.setText(_translate('Dialog_AddStu', '班级：'))
        self.comboBox_sex.setItemText(0, _translate('Dialog_AddStu', '男'))
        self.comboBox_sex.setItemText(1, _translate('Dialog_AddStu', '女'))
        self.pushButton_OK.setText(_translate('Dialog_AddStu', '确定'))
        self.pushButton_exit.setText(_translate('Dialog_AddStu', '退出'))

    def InsertStu(self):

        self.conn=pymysql.connect(host='localhost',user='root',passwd='1234',db='student_db',port=3306,charset='utf8')

        self.cursor=self.conn.cursor()

        stu_id = self.lineEdit_id.text()
        stu_name = self.lineEdit_name.text()
        stu_sex = self.comboBox_sex.currentText()
        stu_age = self.lineEdit_age.text()
        stu_class = self.lineEdit_class.text()

        sql = "INSERT INTO student VALUES ('"+stu_id+"','"+stu_name+"','"+stu_sex+"','"+stu_age+"','"+stu_class+"')"
        print(sql)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
        self.conn.close()

    def AddWinExit(self):
        self.close()













