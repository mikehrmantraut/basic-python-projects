#!/bin/python3
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainForm(QMainWindow):
    
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(200,200,500,500)
        self.initUI()
        
    def initUI(self):
        self.lbl_num1 = QtWidgets.QLabel(self)
        self.lbl_num1.setText("Number 1: ")
        self.lbl_num1.move(50,30)
        
        self.le_num1 = QtWidgets.QLineEdit(self)
        self.le_num1.move(120,30)
        self.le_num1.resize(200,32)

        self.lbl_num2 = QtWidgets.QLabel(self)
        self.lbl_num2.setText("Number 2: ")
        self.lbl_num2.move(50,80)

        self.le_num2 = QtWidgets.QLineEdit(self)
        self.le_num2.move(120,80)
        self.le_num2.resize(200,32)

        self.btn_sum = QtWidgets.QPushButton(self)
        self.btn_sum.setText("Sum")
        self.btn_sum.move(150,130)
        self.btn_sum.clicked.connect(self.sum)
        
        self.btn_extr = QtWidgets.QPushButton(self)
        self.btn_extr.setText("Extraction")
        self.btn_extr.move(50,130)
        self.btn_extr.clicked.connect(self.extr)

        self.btn_div = QtWidgets.QPushButton(self)
        self.btn_div.setText("Divide")
        self.btn_div.move(250,130)
        self.btn_div.clicked.connect(self.divide)

        self.btn_mp = QtWidgets.QPushButton(self)
        self.btn_mp.setText("Multiply")
        self.btn_mp.move(350,130)
        self.btn_mp.clicked.connect(self.multiply)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText("Result: ")
        self.lbl_result.move(50,200)
    
    def sum(self):
        result = int(self.le_num1.text()) + int(self.le_num2.text())
        self.lbl_result.setText("Result: " + str(result))

    def extr(self):
        result = int(self.le_num1.text()) - int(self.le_num2.text())
        self.lbl_result.setText("Result: " + str(result))
    
    def divide(self):
        result = int(self.le_num1.text()) / int(self.le_num2.text())
        self.lbl_result.setText("Result: " + str(result))

    def multiply(self):
        result = int(self.le_num1.text()) * int(self.le_num2.text())
        self.lbl_result.setText("Result: " + str(result))
    
def app():
    app = QApplication(sys.argv)
    window = MainForm()
    window.show()
    sys.exit(app.exec_())
app()
