# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VIDE0.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import  threading
import sys
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import QDir, Qt, QUrl, QSize
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar)
from PyQt5 import QtCore, QtGui, QtWidgets,QtMultimedia
from PyQt5.QtWidgets import QFileDialog
file =""
class Ui_Germes(object):
    def setupUi(self, Germes):
        Germes.setObjectName("Germes")
        Germes.resize(729, 413)
        self.centralwidget = QtWidgets.QWidget(Germes)
        self.centralwidget.setObjectName("centralwidget")
        self.clock = QtWidgets.QPushButton(self.centralwidget)
        self.clock.setGeometry(QtCore.QRect(460, 40, 71, 61))
        self.clock.setAutoFillBackground(False)
        self.clock.setStyleSheet("border:none;\n"
"backgroud:none;")
        self.clock.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("alarm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clock.setIcon(icon)
        self.clock.setIconSize(QtCore.QSize(50, 50))
        self.clock.setObjectName("clock")
        self.video = QVideoWidget(self.centralwidget)
        self.video.setGeometry(QtCore.QRect(20, 10, 691, 321))
        self.video.setObjectName("video")
        self.Play = QtWidgets.QPushButton(self.centralwidget)
        self.Play.setGeometry(QtCore.QRect(70, 350, 75, 23))
        self.Play.setObjectName("Play")
        self.OpenFile = QtWidgets.QPushButton(self.centralwidget)
        self.OpenFile.setGeometry(QtCore.QRect(190, 350, 75, 23))
        self.OpenFile.setObjectName("OpenFile")
        Germes.setCentralWidget(self.centralwidget)

        self.retranslateUi(Germes)
        QtCore.QMetaObject.connectSlotsByName(Germes)

    def retranslateUi(self, Germes):
        _translate = QtCore.QCoreApplication.translate
        Germes.setWindowTitle(_translate("Germes", "Project \"Germes\""))
        self.Play.setText(_translate("Germes", "Play"))
        self.OpenFile.setText(_translate("Germes", "Open File"))
from PyQt5.QtMultimediaWidgets import QVideoWidget
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.ui = Ui_Germes()
        self.ui.setupUi(self)
        self.media= QtMultimedia.QMediaPlayer(self)
        self.media.setVideoOutput(self.ui.video)
        self.ui.Play.clicked.connect(self.Plays)
        self.ui.OpenFile.clicked.connect(self.Open)

    def Open(self):
        file= QFileDialog.getOpenFileName(self, "Выберите видеофайл",
                ".", "Video Files (*.mp4 *.flv *.ts *.mts *.avi)")
        print(file[0])
        if file:
            self.media.setMedia(
                    QMediaContent(QUrl.fromLocalFile(file[0])))
            self.media.play()

    def Plays(self):
        url = QtCore.QUrl(file[0])
        self.media.setMedia(QtMultimedia.QMediaContent(url))
        self.media.play()





app = QtWidgets.QApplication([])
applicatin = Window()
applicatin.show()
sys.exit(app.exec())