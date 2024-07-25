import  struct
import  speech_recognition as sr
import  pyaudio
import  os
import  webbrowser
#from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import  win32
import numpy as np
import time
import  pyttsx3
import datetime
import bs4, requests
import html2text
import  math
import  random
import threading
import  wave
import pyaudio
import  datetime
import psutil
from pathlib import *
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout
from  matplotlib.backends.backend_qt5agg import  FigureCanvasQTAgg
from matplotlib.figure import  Figure
import  matplotlib as plt
import  numpy as np
import json
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QDir, Qt, QUrl, QSize
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar)
from PyQt5 import QtCore, QtGui, QtWidgets,QtMultimedia
from PyQt5.QtWidgets import QFileDialog

file =""
json_var=[]










speed = 200
time_count = 3
value = 0
Name = False

#pyaudio
Time  =datetime.datetime.now()
S=str(Time.strftime("%d-%m-%y %H-%M"))
Name = S+".wav"
data_unt=[]
PATH_PROGRAMM = Path.cwd()
F = str(PATH_PROGRAMM)
String=  F.split(":")
DISK =String[0]+":"
free = psutil.disk_usage(DISK).free/(1024)
Minutes= round(free/172/60)
print(Minutes)

#buffer
CHUNK = 1024*2

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = Minutes
WAVE_OUTPUT_FILENAME = Name
frames = []


p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)



def Record():
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        data_int = struct.unpack(str(2 * CHUNK) + 'B', data)
        frames.append(data_int)


class Hozyain:
    def __init__(self, age, name):
        self.age = age
        self.name = name

def Hello():
    global Hoz
    my_file = open('hozyain.txt', 'r')
    text = my_file.read()
    my_file.close()
    if text == "":
                talk("Напишите ваше имя")
    else:
        global  Name
        Name = True
        Hoz = Hozyain(19, text)
        talk("Привет " + text)


def Weather():
    s = requests.get('https://yandex.ru/pogoda')
    b = bs4.BeautifulSoup(s.text, "html.parser")
    m = b.find('div', class_='link__feelings fact__feelings').text
    F = m.split("Ощущается как")
    return  b.find('span', 'temp__value').text +""+ F[0]

def talk(words):
 engine = pyttsx3.init()
 engine.say(words)
 engine.runAndWait()
 print(words)

def Write():
        rec = sr.Recognizer()
        mike = sr.Microphone()

        with mike as source:
            rec.pause_threshold = 1
            rec.adjust_for_ambient_noise(source, duration=1)
            audio = rec.listen(source)
            resu = rec.recognize_google(audio, language="ru_RU")
            resu = resu.lower()
            return  resu

def command():
 rec = sr.Recognizer()
 mike = sr.Microphone()


 with mike as source:
            rec.pause_threshold = 1
            rec.adjust_for_ambient_noise(source, duration=1)
            audio = rec.listen(source)
            try:
               result = rec.recognize_google(audio,language="ru_RU")
               result = result.lower()
               print("Вы сказали " + result)
            except sr.UnknownValueError:
               print("Не понял")
               result = command()
            my_file = open('result.txt', 'w')
            my_file.write(result)
            my_file.close()
            return result


def Make(result):
    if 'время' in result:
        talk(datetime.datetime.now().strftime('%H:%M'))
    elif 'монетк' in result:
        talk("Бросаю" )
        from random import randrange, uniform
        i= randrange(0,2)
        if i ==0:
            talk("Решка")
        if i == 1:
            talk("Орёл")
    elif "пиш"and'заметк' in result:
        talk("Что записать?")
        Text = Write()
        talk("Записал"+Text)
        my_file = open('note.txt', 'w')
        my_file.write(Text)
        my_file.close()
    elif "погод" in result:
        Weather()
        We = Weather()
        talk(We)
    elif "корень" in result:
        talk("Назовите число")
        Num = int(Write())
        talk(math.sqrt(Num))
    elif "сегодня день" in result:
        talk(datetime.datetime.date(datetime.datetime.now()))
        talk(datetime.isoweekday())
    elif "cлучайное" and "число" in result:
        talk("Назовите максимальное число")
        S = str(Write())
        print(S)
        if S.isdigit():
            F = int(S)
            talk(random.randint(0, F))
        else:
            talk("Назови число, кретин")
    elif "найди" and "интернет" in result:
        talk("Что найти?")
        adress ="https://yandex.ru/search/?text="
        request = str(Write())
        webbrowser.open_new(adress+request)
    elif "диктофон"  in result:
        talk("Начинаю запись через 3")
        talk("2")
        talk("1")
        global  p
        print("* recording")
        Record()
    elif "вычис" and "факториал" in result:
        talk("Назовите число")
        Num = int(Write())
        talk(math.factorial(Num))




def Privet():
    t1 = threading.Thread(target=Hello)
    t1.start()

def Voice():
    t1 = threading.Thread(target=command)
    t1.start()

def Audiovisual():
    t1 = threading.Thread(target=Record)
    t1.start()
def Next():
    while True:
        Make(command())


def Makes():
    t1 = threading.Thread(target=Next)
    t1.start()





class Ui_Germes(object):
    def setupUi(self, Germes):
        Germes.setObjectName("Germes")
        Germes.setFixedSize(729, 413)
        Germes.setWindowFlags(QtCore.Qt.Window |
                              QtCore.Qt.FramelessWindowHint |
                              QtCore.Qt.WindowTitleHint)
        self.centralwidget = QtWidgets.QWidget(Germes)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.video = QtWidgets.QLabel(self.centralwidget)
        self.video.setGeometry(QtCore.QRect(-4, -8, 741, 421))
        self.video.setAutoFillBackground(False)
        self.video.setText("")
        self.video.setObjectName("video")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(580, 170, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(32)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 731, 421))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0454545 rgba(52, 70, 102, 255), stop:1 rgba(79, 68, 127, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Name = QtWidgets.QLabel(self.frame)
        self.Name.setGeometry(QtCore.QRect(130, 40, 481, 191))
        self.Name.setAutoFillBackground(False)
        self.Name.setStyleSheet("font: 73pt \"Orbitron\";\n"
"text-shadow: 2px 3px 7px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.Name.setTextFormat(QtCore.Qt.PlainText)
        self.Name.setScaledContents(False)
        self.Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Name.setObjectName("Name")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(170, 270, 411, 31))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-style:none;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"border-radius:10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(63, 63, 255, 255), stop:1 rgba(14, 123, 255, 255));\n"
"}")
        self.progressBar.setProperty("value", value)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.video.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.frame.raise_()
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(170, 70, 461, 251))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("\n"
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0454545 rgba(52, 70, 102, 255), stop:1 rgba(79, 68, 127, 255));\n"
                                   "border-radius: 8px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(80, 140, 311, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.Name_2 = QtWidgets.QLabel(self.frame_2)
        self.Name_2.setGeometry(QtCore.QRect(-10, -30, 481, 191))
        self.Name_2.setAutoFillBackground(False)
        self.Name_2.setStyleSheet("font: 30pt \"Orbitron\";\n"
                                  "text-shadow: 2px 3px 7px;\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color: rgba(255, 255, 255, 0);")
        self.Name_2.setTextFormat(QtCore.Qt.PlainText)
        self.Name_2.setScaledContents(False)
        self.Name_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Name_2.setObjectName("Name_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(100, 190, 121, 31))
        self.pushButton.setStyleSheet("background-color: rgb(96, 198, 41);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "font: 11pt \"Orbitron\";\n"
                                      "border-radius: 8px;\n"
                                      "text-shadow: 2px 3px 7px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 190, 121, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 4);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "font: 11pt \"Orbitron\";\n"
                                        "border-radius: 8px;\n"
                                        "text-shadow: 2px 3px 7px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.Graph = QtWidgets.QWidget(self.centralwidget)
        self.Graph.setGeometry(QtCore.QRect(230, 140, 271, 121))
        self.Graph.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Graph.setObjectName("Graph")
        self.Graph.setVisible(False)
        self.bot = QtWidgets.QFrame(self.centralwidget)
        self.bot.setGeometry(QtCore.QRect(210, 233, 321, 31))
        self.bot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bot.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.bot.setVisible(False)
        self.bot.setObjectName("bot")
        self.left = QtWidgets.QFrame(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(242, 100, 31, 171))
        self.left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left.setObjectName("left")
        self.left.setVisible(False)
        self.left.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(370, 20, 201, 51))
        self.stop.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.stop.setObjectName("stop")
        self.stop.setVisible(False)
        self.video.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.Graph.raise_()
        self.bot.raise_()
        self.left.raise_()
        self.stop.raise_()
        self.alarm = QtWidgets.QFrame(self.centralwidget)
        self.alarm.setGeometry(QtCore.QRect(200, 120, 361, 201))
        self.alarm.setAutoFillBackground(False)
        self.alarm.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(220, 211, 227, 255), stop:1 rgba(211, 211, 211, 255));\n"
            "border-radius:10px;")
        self.alarm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alarm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.alarm.setObjectName("alarm")
        self.alarm.setVisible(False)
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
        self.acept1.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.915, y2:0, stop:0 rgba(0, 255, 0, 255), stop:1 rgba(3, 255, 142, 255));\n"
            "color: rgb(255, 255, 255);\n"
            "border-radius:10px;")
        self.acept1.setObjectName("acept1")
        self.clear1 = QtWidgets.QPushButton(self.alarm)
        self.clear1.setGeometry(QtCore.QRect(200, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Oswald Medium")
        font.setPointSize(12)
        self.clear1.setFont(font)
        self.clear1.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.960227 rgba(177, 0, 0, 255), stop:0.977273 rgba(207, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color: rgb(255, 255, 255);\n"
            "border-radius:10px;")
        self.clear1.setObjectName("clear1")
        self.close1 = QtWidgets.QPushButton(self.alarm)
        self.close1.setGeometry(QtCore.QRect(310, 0, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Oswald Medium")
        font.setPointSize(12)
        self.close1.setFont(font)
        self.close1.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.960227 rgba(177, 0, 0, 255), stop:0.977273 rgba(207, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color: rgb(255, 255, 255);\n"
            "")
        self.close1.setObjectName("close1")
        self.alarm_2 = QtWidgets.QFrame(self.centralwidget)
        self.alarm_2.setVisible(False)
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
        self.Closse.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.960227 rgba(177, 0, 0, 255), stop:0.977273 rgba(207, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color: rgb(255, 255, 255);\n"
            "")
        self.Closse.setObjectName("Closse")
        self.acept1_2 = QtWidgets.QPushButton(self.alarm_2)
        self.acept1_2.setGeometry(QtCore.QRect(20, 220, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Oswald Medium")
        font.setPointSize(12)
        self.acept1_2.setFont(font)
        self.acept1_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.915, y2:0, stop:0 rgba(0, 255, 0, 255), stop:1 rgba(3, 255, 142, 255));\n"
            "color: rgb(255, 255, 255);\n"
            "border-radius:10px;")
        self.acept1_2.setObjectName("acept1_2")
        self.Closse.setFont(font)
        self.Closse.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.960227 rgba(177, 0, 0, 255), stop:0.977273 rgba(207, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "color: rgb(255, 255, 255);\n"
            "")
        self.Closse.setObjectName("Closse")
        self.video = QVideoWidget(self.centralwidget)
        self.video.setGeometry(QtCore.QRect(20, 10, 691, 321))
        self.video.setObjectName("video")
        self.video.setVisible(False)
        self.OpenFile = QtWidgets.QPushButton(self.centralwidget)
        self.OpenFile.setGeometry(QtCore.QRect(190, 350, 75, 23))
        self.OpenFile.setObjectName("OpenFile")
        self.clock = QtWidgets.QPushButton(self.centralwidget)
        self.clock.setGeometry(QtCore.QRect(440, 40, 71, 61))
        self.clock.setAutoFillBackground(False)
        self.clock.setStyleSheet("border:none;\n"
                                 "backgroud:none;")
        self.clock.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("alarm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clock.setIcon(icon)
        self.clock.setIconSize(QtCore.QSize(50, 50))
        self.clock.setObjectName("clock")
        Germes.setCentralWidget(self.centralwidget)

        self.retranslateUi(Germes)
        QtCore.QMetaObject.connectSlotsByName(Germes)




    def retranslateUi(self, Germes):
        _translate = QtCore.QCoreApplication.translate
        Germes.setWindowTitle(_translate("Germes", "Project \"Germes\""))
        self.label_2.setText(_translate("Germes", "TextLabel"))
        self.label_3.setText(_translate("Germes", datetime.datetime.now().strftime('%H:%M')))
        self.Name.setText(_translate("Germes", "Germes"))
        self.label_2.setText(_translate("Germes", "TextLabel"))
        self.label_3.setText(_translate("Germes", "TextLabel"))
        self.Name.setText(_translate("Germes", "Germes"))
        self.Name_2.setText(_translate("Germes", "Введите ваше имя"))
        self.pushButton.setText(_translate("Germes", "Принять"))
        self.pushButton_2.setText(_translate("Germes", "Очистить"))
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
        self.OpenFile.setText(_translate("Germes", "Open File"))

class MatplotlibWidget(QWidget):
    def __init__(self,parent=None):
        super(MatplotlibWidget,self).__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.axis = self.figure.add_subplot(111)
        self.layoutvertical =QVBoxLayout(self)
        self.layoutvertical.addWidget(self.canvas)
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.ui = Ui_Germes()
        self.ui.setupUi(self)
        self.movie = QtGui.QMovie("Back!.gif")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.setSpeed(speed)
        self.movie.start()
        print(self.movie.frameCount())
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.Timer)
        self.timer.start(10)
        self.ui.pushButton_2.clicked.connect(self.Clean)
        self.ui.pushButton.clicked.connect(self.HozName)
        self.ui.stop.clicked.connect(self.Stop)
        self.ui.clock.clicked.connect(self.CloCK)
        self.ui.Closse.clicked.connect(self.Close_alarm)
        self.ui.acept1_2.clicked.connect(self.NewClock)
        self.ui.acept1.clicked.connect(self.AceptClock)
        self.ui.listWidget.itemDoubleClicked.connect(self.Delete)
        self.init_wwidget()
        self.Visual()
        self.Update_Alarm()
        self.media = QtMultimedia.QMediaPlayer(self)
        self.media.setVideoOutput(self.ui.video)
        self.ui.OpenFile.clicked.connect(self.Open)

    def Open(self):
        self.ui.video.setVisible(True)
        file = QFileDialog.getOpenFileName(self, "Open Video",
                                           ".", "Video Files (*.mp4 *.flv *.ts *.mts *.avi)")
        print(file[0])
        if file:
            self.ui.clock.setVisible(False)
            self.media.setMedia(
                QMediaContent(QUrl.fromLocalFile(file[0])))
            self.media.play()

        #self.Plot(hour,tem)
    def init_wwidget(self):
        self.matplotlibwidget = MatplotlibWidget()
        self.layoutvertical =QVBoxLayout(self.ui.Graph)
        self.layoutvertical.addWidget(self.matplotlibwidget)



    def Audiovisual(self):
        x= np.arange(0, 2 * CHUNK, 2)
        y= np.random.rand(CHUNK)
        self.matplotlibwidget.axis.clear()
        line, = self.matplotlibwidget.axis.plot(x,y,'m')
        self.matplotlibwidget.axis.set_facecolor('black')
        self.matplotlibwidget.figure.patch.set_visible(False)
        self.matplotlibwidget.axis.set_ylim(-10000, 10000)
        self.matplotlibwidget.axis.ser_xlim = (0, CHUNK)
        self.matplotlibwidget.canvas.draw()
        while True:
            data = stream.read(CHUNK)
            dataInt = struct.unpack(str(CHUNK) + 'h', data)
            line.set_ydata(dataInt)
            self.matplotlibwidget.figure.canvas.draw()
            self.matplotlibwidget.figure.canvas.flush_events()

    def Visual(self):
        t1 = threading.Thread(target=self.Audiovisual)
        t1.start()


    def Update_Alarm(self):
        with open('alarm.json', 'r') as f:
            json_var = json.load(f)
            for i in range(len(json_var)):
                print(json_var[i])
                self.ui.listWidget.addItem(json_var[i])


    def AceptClock(self):
        Hour=""
        Minutes=""
        if(self.ui.spinBox.value()<10):
            Hour = "0"+str(self.ui.spinBox.value())
        else:
            Hour =str(self.ui.spinBox.value())

        if(self.ui.spinBox_2.value()<10):
            Minutes = "0"+str(self.ui.spinBox.value())
        else:
            Minutes =str(self.ui.spinBox.value())
        self.ui.listWidget.addItem(Hour+":"+Minutes)
        json_var.append(Hour+":"+Minutes)
        print(json_var)
        with open('alarm.json', 'w') as f:
            json.dump(json_var, f)

    def Del(self):
        listItems = self.ui.listWidget.selectedItems()
        if not listItems: return
        for item in listItems:
            self.ui.listWidget.takeItem(self.ui.listWidget.row(item))

    def Delete(self):
        t1 = threading.Thread(target=self.Del)
        t1.start()

    def Stop(self):
        global  frames
        global  stream
        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    def CloCK(self):
        t1 = threading.Thread(target=self.Clock)
        t1.start()
    def Clock(self):
        self.ui.alarm_2.setVisible(True)

    def Close_alarm(self):
        self.ui.alarm_2.setVisible(False)

    def Clean(self):
        self.ui.lineEdit.clear()

    def NewClock(self):
        self.ui.alarm.setVisible(True)


    def HozName(self):
        Hoz = Hozyain(19, self.ui.lineEdit.text())
        my_file = open('hozyain.txt', 'w')
        my_file.write(Hoz.name)
        my_file.close()
        talk("Привет " + Hoz.name)
        self.ui.frame_2.setVisible(False)


    def Timer(self):
        global value
        self.ui.progressBar.setValue(value)
        self.ui.frame_2.setVisible(False)
        self.ui.clock.setVisible(False)
        if value>100:
            self.timer.stop()
            self.ui.frame.setVisible(False)
            self.ui.Graph.setVisible(True)
            self.ui.bot.setVisible(False)
            self.ui.left.setVisible(False)
            self.ui.clock.setVisible(True)
            Privet()

        value+=1


    Voice()
    def Check(self):
        global  Name
        if Name==False:
            self.ui.frame_2.setVisible(True)



    def paintEvent(self, event):

        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QtGui.QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)
#from pyqtgraph import PlotWidget


app = QtWidgets.QApplication([])
applicatin = Window()
applicatin.show()
Makes()
sys.exit(app.exec())



