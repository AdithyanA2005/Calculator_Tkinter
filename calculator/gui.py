from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 689)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.calcDisplay = QtWidgets.QLabel(self.centralwidget)
        self.calcDisplay.setGeometry(QtCore.QRect(10, 20, 431, 91))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.calcDisplay.setFont(font)
        self.calcDisplay.setStyleSheet("background-color: white;\n""font: 20pt \"MS UI Gothic\";\nfont-weight:400; font-style:normal;")
        self.calcDisplay.setObjectName("calcDisplay")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(10, 240, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn7.setFont(font)
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(120, 240, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn8.setFont(font)
        self.btn8.setObjectName("btn8")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(230, 240, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn9.setFont(font)
        self.btn9.setObjectName("btn9")
        self.btnDiv = QtWidgets.QPushButton(self.centralwidget)
        self.btnDiv.setGeometry(QtCore.QRect(340, 240, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnDiv.setFont(font)
        self.btnDiv.setStyleSheet("background-color: rgb(124, 194, 255);")
        self.btnDiv.setObjectName("btnDiv")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(10, 350, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.btnMinus = QtWidgets.QPushButton(self.centralwidget)
        self.btnMinus.setGeometry(QtCore.QRect(340, 350, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnMinus.setFont(font)
        self.btnMinus.setStyleSheet("background-color: rgb(124, 194, 255);")
        self.btnMinus.setObjectName("btnMinus")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(230, 350, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn6.setFont(font)
        self.btn6.setObjectName("btn6")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(120, 350, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn5.setFont(font)
        self.btn5.setObjectName("btn5")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(120, 460, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(10, 460, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(230, 460, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.btnPlus = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlus.setGeometry(QtCore.QRect(340, 460, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnPlus.setFont(font)
        self.btnPlus.setStyleSheet("background-color: rgb(124, 194, 255);")
        self.btnPlus.setObjectName("btnPlus")
        self.btnEqual = QtWidgets.QPushButton(self.centralwidget)
        self.btnEqual.setGeometry(QtCore.QRect(340, 570, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnEqual.setFont(font)
        self.btnEqual.setStyleSheet("background-color: rgb(227, 231, 18);")
        self.btnEqual.setObjectName("btnEqual")
        self.btnSquare = QtWidgets.QPushButton(self.centralwidget)
        self.btnSquare.setGeometry(QtCore.QRect(10, 570, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnSquare.setFont(font)
        self.btnSquare.setStyleSheet("background-color: rgb(227, 231, 18);")
        self.btnSquare.setObjectName("btnSquare")
        self.btn0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn0.setGeometry(QtCore.QRect(120, 570, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn0.setFont(font)
        self.btn0.setObjectName("btn0")
        self.btnDot = QtWidgets.QPushButton(self.centralwidget)
        self.btnDot.setGeometry(QtCore.QRect(230, 570, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnDot.setFont(font)
        self.btnDot.setObjectName("btnDot")
        self.btnClearAll = QtWidgets.QPushButton(self.centralwidget)
        self.btnClearAll.setGeometry(QtCore.QRect(10, 130, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnClearAll.setFont(font)
        self.btnClearAll.setStyleSheet("background-color: rgb(227, 231, 18);")
        self.btnClearAll.setObjectName("btnClearAll")
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(340, 130, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnBack.setFont(font)
        self.btnBack.setStyleSheet("background-color: rgb(124, 194, 255);")
        self.btnBack.setObjectName("btnBack")
        self.btnMult = QtWidgets.QPushButton(self.centralwidget)
        self.btnMult.setGeometry(QtCore.QRect(230, 130, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnMult.setFont(font)
        self.btnMult.setStyleSheet("background-color: rgb(124, 194, 255);")
        self.btnMult.setObjectName("btnMult")
        self.btnPercent = QtWidgets.QPushButton(self.centralwidget)
        self.btnPercent.setGeometry(QtCore.QRect(120, 130, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnPercent.setFont(font)
        self.btnPercent.setStyleSheet("background-color: rgb(227, 231, 18);")
        self.btnPercent.setObjectName("btnPercent")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ADITHYAN\'S CALCULATOR"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btnDiv.setText(_translate("MainWindow", "÷"))
        self.btnMinus.setText(_translate("MainWindow", "-"))
        self.btnPlus.setText(_translate("MainWindow", "+"))
        self.btnEqual.setText(_translate("MainWindow", "="))
        self.btnPercent.setText(_translate("MainWindow", "%"))
        self.btnMult.setText(_translate("MainWindow", "×"))
        self.btnSquare.setText(_translate("MainWindow", "x2"))
        self.btnDot.setText(_translate("MainWindow", "."))
        self.btnClearAll.setText(_translate("MainWindow", "C"))
        self.btnBack.setText(_translate("MainWindow", "←"))
        self.calcDisplay.setText(_translate("MainWindow", "ENTER NUMBERS"))
