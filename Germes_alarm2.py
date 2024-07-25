# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Germes_alarm2.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Germes(object):
    def setupUi(self, Germes):
        Germes.setObjectName("Germes")
        Germes.resize(729, 413)
        self.centralwidget = QtWidgets.QWidget(Germes)
        self.centralwidget.setObjectName("centralwidget")
        self.alarm = QtWidgets.QFrame(self.centralwidget)
        self.alarm.setGeometry(QtCore.QRect(200, 120, 361, 201))
        self.alarm.setAutoFillBackground(False)
        self.alarm.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(220, 211, 227, 255), stop:1 rgba(211, 211, 211, 255));\n"
"border-radius:10px;")
        self.alarm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alarm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.alarm.setObjectName("alarm")
        self.spinBox = QtWidgets.QSpinBox(self.alarm)
        self.spinBox.setGeometry(QtCore.QRect(50, 40, 121, 81))
        font = QtGui.QFont()
        font.setFamily("Oswald Medium")
        font.setPointSize(48)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("")
        self.spinBox.setMaximum(23)
        self.spinBox.setProperty("value", 1)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.alarm)
        self.spinBox_2.setGeometry(QtCore.QRect(200, 40, 121, 81))
        font = QtGui.QFont()
        font.setFamily("Oswald Medium")
        font.setPointSize(48)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setStyleSheet("")
        self.spinBox_2.setMinimum(0)
        self.spinBox_2.setMaximum(59)
        self.spinBox_2.setObjectName("spinBox_2")
        self.acept1 = QtWidgets.QPushButton(self.alarm)
        self.acept1.setGeometry(QtCore.QRect(40, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Oswald Medium")
        font.setPointSize(12)
        self.acept1.setFont(font)
        self.acept1.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.915, y2:0, stop:0 rgba(0, 255, 0, 255), stop:1 rgba(3, 255, 142, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.acept1.setObjectName("acept1")
        self.clear1 = QtWidgets.QPushButton(self.alarm)
        self.clear1.setGeometry(QtCore.QRect(200, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Oswald Medium")
        font.setPointSize(12)
        self.clear1.setFont(font)
        self.clear1.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.960227 rgba(177, 0, 0, 255), stop:0.977273 rgba(207, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.clear1.setObjectName("clear1")
        self.close1 = QtWidgets.QPushButton(self.alarm)
        self.close1.setGeometry(QtCore.QRect(310, 0, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Oswald Medium")
        font.setPointSize(12)
        self.close1.setFont(font)
        self.close1.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.960227 rgba(177, 0, 0, 255), stop:0.977273 rgba(207, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);\n"
"")
        self.close1.setObjectName("close1")
        self.alarm_2 = QtWidgets.QFrame(self.centralwidget)
        self.alarm_2.setGeometry(QtCore.QRect(290, 70, 161, 261))
        self.alarm_2.setAutoFillBackground(False)
        self.alarm_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.alarm_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alarm_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.alarm_2.setObjectName("alarm_2")
        self.listWidget = QtWidgets.QListWidget(self.alarm_2)
        self.listWidget.setGeometry(QtCore.QRect(40, 40, 81, 181))
        font = QtGui.QFont()
        font.setFamily("Oswald Medium")
        font.setPointSize(24)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.Closse = QtWidgets.QPushButton(self.alarm_2)
        self.Closse.setGeometry(QtCore.QRect(110, 0, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Oswald Medium")
        font.setPointSize(12)
        self.Closse.setFont(font)
        self.Closse.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.960227 rgba(177, 0, 0, 255), stop:0.977273 rgba(207, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Closse.setObjectName("Closse")
        self.acept1_2 = QtWidgets.QPushButton(self.alarm_2)
        self.acept1_2.setGeometry(QtCore.QRect(20, 220, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Oswald Medium")
        font.setPointSize(12)
        self.acept1_2.setFont(font)
        self.acept1_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.915, y2:0, stop:0 rgba(0, 255, 0, 255), stop:1 rgba(3, 255, 142, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.acept1_2.setObjectName("acept1_2")
        self.clock = QtWidgets.QPushButton(self.centralwidget)
        self.clock.setGeometry(QtCore.QRect(440, 40, 71, 61))
        self.clock.setAutoFillBackground(False)
        self.clock.setStyleSheet("border:none;\n"
"backgroud:none;")
        self.clock.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/stree/Desktop/Без имени-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clock.setIcon(icon)
        self.clock.setIconSize(QtCore.QSize(50, 50))
        self.clock.setObjectName("clock")
        Germes.setCentralWidget(self.centralwidget)

        self.retranslateUi(Germes)
        QtCore.QMetaObject.connectSlotsByName(Germes)

    def retranslateUi(self, Germes):
        _translate = QtCore.QCoreApplication.translate
        Germes.setWindowTitle(_translate("Germes", "Project \"Germes\""))
        self.acept1.setText(_translate("Germes", "Принять"))
        self.clear1.setText(_translate("Germes", "Сбросить"))
        self.close1.setText(_translate("Germes", "Х"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Germes", "08:30"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.Closse.setText(_translate("Germes", "Х"))
        self.acept1_2.setText(_translate("Germes", "Новый"))
