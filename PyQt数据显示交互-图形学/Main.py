import os
import sys

import pandas as pd
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QMainWindow,
                             QPushButton)
import untitled
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'
#设置正常显示字符
plt.rcParams['axes.unicode_minus'] = False

def Window1():
    row1=int(ui.lineEdit.text())
    print(row1)
    list1=int(ui.lineEdit_2.text())
    print(list1)
    #显示图像
    print("文件为",ui.textEdit.toPlainText())
    file_path=ui.textEdit.toPlainText()
    data=pd.read_csv(file_path,header=None,sep='\t')
    # ui.graphicsView.showNormal(data.iloc[:20,:1].plot())
    ui.graphicsView.clearMask()
    data.iloc[row1:list1,:1].plot()
    plt.title('第一列数据')
    plt.show()
def Window2():
    row2=int(ui.lineEdit_3.text())
    print(row2)
    list2=int(ui.lineEdit_4.text())
    print(list2)
    file_path=ui.textEdit.toPlainText()
    data=pd.read_csv(file_path,header=None,sep='\t')
    ui.graphicsView.clearMask()
    data.iloc[row2:list2,1:2].plot()
    plt.title('第二列数据')
    plt.show()
def Window3():
    row3=int(ui.lineEdit_5.text())
    print(row3)
    list3=int(ui.lineEdit_6.text())
    print(list3)
    file_path=ui.textEdit.toPlainText()
    data=pd.read_csv(file_path,header=None,sep='\t')
    ui.graphicsView.clearMask()
    data.iloc[row3:list3,2:3].plot()
    plt.title('第三列数据')
    plt.show()
def Window4():
    row4=int(ui.lineEdit_7.text())
    print(row4)
    list4=int(ui.lineEdit_8.text())
    print(list4)
    file_path=ui.textEdit.toPlainText()
    data=pd.read_csv(file_path,header=None,sep='\t')
    ui.graphicsView.clearMask()
    data.iloc[row4:list4,3:4].plot()
    plt.title('第四列数据')
    plt.show()
def read_file():
    pass
def showDialog(self):
    getfile=QFileDialog.getOpenFileName() 
    data=getfile[0]
    ui.textEdit.setText(data)
def click_button():
    ui.pushButton_6.clicked.connect(showDialog)
    ui.pushButton_2.clicked.connect(Window1)
    ui.pushButton_3.clicked.connect(Window2)
    ui.pushButton_4.clicked.connect(Window3)
    ui.pushButton_5.clicked.connect(Window4)
if __name__ == "__main__":
    app=QApplication(sys.argv)
    mainwindow=QMainWindow()
    ui=untitled.Ui_Dialog()
    ui.setupUi(mainwindow)
    mainwindow.show()
    click_button()
    print(ui.textEdit.toPlainText())
    sys.exit(app.exec_())
