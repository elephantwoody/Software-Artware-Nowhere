# This Python file uses the following encoding: utf-8
#!/usr/bin/Python
# encoding=utf8
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * #Qt, QDate, QTime, QDateTime
from PyQt5.QtGui import *
from random import randint

class MyMainWindow(QWidget):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        #self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(320, 570)
        self.move(100, 0)
        self.setWindowTitle('Weather Forecast')

        label = QLabel(self)
        background = QPixmap('img/bluesky.jpg')
        label.setPixmap(background)

        now = QDate.currentDate()
        self.nowD = QLabel(now.toString(Qt.DefaultLocaleShortDate), self)
        self.nowD.setFont(QFont('Helvetica', 17, QFont.ExtraLight))
        self.nowD.setStyleSheet('color:white')
        self.nowD.setGeometry(5, 25, 100, 20)

        day = QDateTime.currentDateTime()
        self.nowD1 = QLabel(day.toString("ddd"), self)
        self.nowD1.setFont(QFont('Helvetica', 13, QFont.ExtraLight))
        self.nowD1.setStyleSheet('color:white')
        self.nowD1.setGeometry(80, 26, 35, 20)

        time = QTime.currentTime()
        self.nowT = QLabel(time.toString("hh:mm"), self)
        self.nowT.setFont(QFont('Helvetica', 17, QFont.ExtraLight))
        self.nowT.setStyleSheet('color:white')
        self.nowT.setGeometry(268, 25, 200, 20)

        #Combobox

        self.lct = QComboBox(self)
        self.lct.setEditable(True)
        self.lct.setGeometry(0, 0, 150, 25) #85, 80, 150, 25
        self.lct.addItems(["Hamburg GMT+1" , "Lüneburg GMT+1", "Hong Kong GMT+8", "Tokyo GMT+9"])
        self.lct.setStyleSheet("""
                    QComboBox {
                    font-family: "Helvetica";
                    font-weight: ExtraLight;
                    font-size: 13px;
                    color: white;
                    background-color: transparent;
                    }
                """)
        #self.lct.currentIndexChanged.connect(self.updateLct)

        self.text1 = QLabel("Hamburg", self)
        self.text1.setFont(QFont('Avenir', 35))
        self.text1.setStyleSheet('color:white')
        self.text1.setGeometry(82, 78, 200, 50)

        self.text2 = QLabel("Sunny", self)
        self.text2.setFont(QFont('Avenir', 15, QFont.ExtraLight))
        self.text2.setStyleSheet('color:white')
        self.text2.setGeometry(140, 105, 200, 50)

        self.text3 = QLabel("\n8", self)
        self.text3.setFont(QFont('Helvetica', 100, QFont.ExtraLight))
        self.text3.setStyleSheet('color:white')
        self.text3.setGeometry(130, 35, 200, 250)

        self.text4 = QLabel("°", self)
        self.text4.setFont(QFont('Helvetica', 30))
        self.text4.setStyleSheet('color:white')
        self.text4.setGeometry(190, 0, 200, 365)

        self.text5 = QLabel("1°", self)
        self.text5.setFont(QFont('Helvetica', 13, QFont.ExtraLight))
        self.text5.setStyleSheet('color:white')
        self.text5.setGeometry(203, 217, 20, 20)

        self.text6 = QLabel("8°", self)
        self.text6.setFont(QFont('Helvetica', 13, QFont.ExtraLight))
        self.text6.setStyleSheet('color:white')
        self.text6.setGeometry(225, 217, 20, 20)

        #slider

        self.slider1 = QSlider(self)
        self.slider1.setOrientation(Qt.Horizontal)
        self.slider1.setTickPosition(QSlider.TicksBelow)
        self.slider1.setMinimum(0)
        self.slider1.setMaximum(6)
        self.slider1.setTickInterval(1)
        self.slider1.setSingleStep(1)
        self.slider1.setGeometry(50, 245, 220, 80)

        self.label1 = QLabel(self)
        self.label1.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.label1.setStyleSheet('color:white')
        self.label1.setGeometry(50, 285, 70, 60)

        self.label2 = QLabel(self)
        self.label2.setGeometry(245, 299, 30, 30)

        self.label3 = QLabel(self)
        self.label3.setGeometry(203, 300, 30, 30)
        self.label3.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.label3.setStyleSheet('color:white')

        self.label4 = QLabel(self)
        self.label4.setGeometry(225, 300, 30, 30) #270
        self.label4.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.label4.setStyleSheet('color:white')

        self.slider1.valueChanged.connect(self.changeLabel)
        self.slider1.valueChanged.connect(self.changeSign)
        self.slider1.valueChanged.connect(self.changeTempMin)
        self.slider1.valueChanged.connect(self.changeTempMax)

        #List

        self.list = QListWidget(self)
        self.list.setStyleSheet("""
                    QListWidget {
                    font-family: "Helvetica";
                    font-weight: ExtraLight;
                    font-size: 13px;
                    color: white;
                    background-color: transparent;
                    }
                    QScrollBar: Horizontal{
                    }
                """)

        self.list.setSpacing(6)
        self.list.setFlow(0)
        self.list.resize(230, 40)
        self.list.move(50, 240)

        self.list.addItem(time.addSecs(3600).toString("hh"))
        self.list.addItem("8°")
        self.list.addItem(time.addSecs(3600 * 2).toString("hh"))
        self.list.addItem("8°")
        self.list.addItem(time.addSecs(3600 * 3).toString("hh"))
        self.list.addItem("7°")
        self.list.addItem(time.addSecs(3600 * 3).toString("hh"))
        self.list.addItem("4°")
        self.list.addItem(time.addSecs(3600 * 4).toString("hh"))
        self.list.addItem("5°")
        self.list.addItem(time.addSecs(3600 * 5).toString("hh"))
        self.list.addItem("3°")
        self.list.addItem(time.addSecs(3600 * 6).toString("hh"))
        self.list.addItem("3°")
        self.list.addItem(time.addSecs(3600 * 7).toString("hh"))
        self.list.addItem("2°")
        self.list.addItem(time.addSecs(3600 * 8).toString("hh"))
        self.list.addItem("2°")
        self.list.addItem(time.addSecs(3600 * 9).toString("hh"))
        self.list.addItem("0°")

        #Checkbox

        self.checkBox1 = QCheckBox(self)
        self.checkBox1.setText ("SHOW MORE")
        self.checkBox1.setFont(QFont("Helvetica", 13, QFont.Bold))
        self.checkBox1.setStyleSheet('color:white')
        self.checkBox1.setGeometry(50, 325, 110, 30)
        self.checkBox1.setChecked(False)
        self.checkBox1.stateChanged.connect(lambda:self.btnstate(self.checkBox1))

        self.info1 = QLabel(self)
        self.info1.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.info1.setStyleSheet('color:white')
        self.info1.setGeometry(52, 345, 300, 30)

        self.info1_1 = QLabel(self)
        self.info1_1.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.info1_1.setStyleSheet('color:white')
        self.info1_1.setGeometry(235, 345, 100, 30) #330

        self.info2 = QLabel(self)
        self.info2.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.info2.setStyleSheet('color:white')
        self.info2.setGeometry(52, 365, 500, 30)

        self.info2_1 = QLabel(self)
        self.info2_1.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.info2_1.setStyleSheet('color:white')
        self.info2_1.setGeometry(235, 365, 100, 30) #350

        self.info3 = QLabel(self)
        self.info3.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.info3.setStyleSheet('color:white')
        self.info3.setGeometry(52, 385, 500, 30)

        self.info3_1 = QLabel(self)
        self.info3_1.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.info3_1.setStyleSheet('color:white')
        self.info3_1.setGeometry(242, 385, 500, 30) #370

        self.info4 = QLabel(self)
        self.info4.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.info4.setStyleSheet('color:white')
        self.info4.setGeometry(52, 405, 500, 30)

        self.info4_1 = QLabel(self)
        self.info4_1.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.info4_1.setStyleSheet('color:white')
        self.info4_1.setGeometry(242, 405, 500, 30) #390

        self.info5 = QLabel(self)
        self.info5.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.info5.setStyleSheet('color:white')
        self.info5.setGeometry(52, 425, 500, 30)

        self.info5_1 = QLabel(self)
        self.info5_1.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.info5_1.setStyleSheet('color:white')
        self.info5_1.setGeometry(194, 425, 500, 30) #410

        self.info6 = QLabel(self)
        self.info6.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.info6.setStyleSheet('color:white')
        self.info6.setGeometry(52, 445, 500, 30)

        self.info6_1 = QLabel(self)
        self.info6_1.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.info6_1.setStyleSheet('color:white')
        self.info6_1.setGeometry(255, 445, 500, 30) #430

        self.info7 = QLabel(self)
        self.info7.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.info7.setStyleSheet('color:white')
        self.info7.setGeometry(52, 465, 500, 30)

        self.info7_1 = QLabel(self)
        self.info7_1.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.info7_1.setStyleSheet('color:white')
        self.info7_1.setGeometry(227, 465, 500, 30) #450

        self.info8 = QLabel(self)
        self.info8.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.info8.setStyleSheet('color:white')
        self.info8.setGeometry(52, 485, 500, 30)

        self.info8_1 = QLabel(self)
        self.info8_1.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.info8_1.setStyleSheet('color:white')
        self.info8_1.setGeometry(210, 485, 500, 30) #470

        self.info9 = QLabel(self)
        self.info9.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.info9.setStyleSheet('color:white')
        self.info9.setGeometry(52, 505, 500, 30)

        self.info9_1 = QLabel(self)
        self.info9_1.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.info9_1.setStyleSheet('color:white')
        self.info9_1.setGeometry(220, 505, 500, 30) #490

        self.info10 = QLabel(self)
        self.info10.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.info10.setStyleSheet('color:white')
        self.info10.setGeometry(52, 525, 500, 30)

        self.info10_1 = QLabel(self)
        self.info10_1.setFont(QFont("Helvetica", 13, QFont.ExtraLight))
        self.info10_1.setStyleSheet('color:white')
        self.info10_1.setGeometry(255, 525, 500, 30)  #510

        self.bigIcon = QLabel(self)
        self.bigIcon.setPixmap(QPixmap('img/sun.png'))
        self.bigIcon.setGeometry(82, 380, 150, 150)

    def btnstate(self, b):
        if b.isChecked() == True:
            self.info1.setText ("SUNRISE")
            self.info1_1.setText ("08:07")
            self.info2.setText ("SUNSET")
            self.info2_1.setText ("16:05")
            self.info3.setText ("CHANCE OF RAIN")
            self.info3_1.setText ("10%")
            self.info4.setText ("HUMIDITY")
            self.info4_1.setText ("82%")
            self.info5.setText ("WIND")
            self.info5_1.setText ("SW 19 km/hr")
            self.info6.setText ("FEELS LIKE")
            self.info6_1.setText ("1°")
            self.info7.setText ("PRECIPITATION")
            self.info7_1.setText ("0.1 cm")
            self.info8.setText ("PRESSURE")
            self.info8_1.setText ("1002 hPa")
            self.info9.setText ("SVISIBILITY")
            self.info9_1.setText ("16.1 km")
            self.info10.setText ("UA INDEX")
            self.info10_1.setText ("0")
            self.bigIcon.setPixmap(QPixmap(''))


        else:
            self.info1.setText ("")
            self.info2.setText ("")
            self.info3.setText ("")
            self.info4.setText ("")
            self.info5.setText ("")
            self.info6.setText ("")
            self.info7.setText ("")
            self.info8.setText ("")
            self.info9.setText ("")
            self.info10.setText ("")
            self.info1_1.setText ("")
            self.info2_1.setText ("")
            self.info3_1.setText ("")
            self.info4_1.setText ("")
            self.info5_1.setText ("")
            self.info6_1.setText ("")
            self.info7_1.setText ("")
            self.info8_1.setText ("")
            self.info9_1.setText ("")
            self.info10_1.setText ("")
            self.bigIcon.setPixmap(QPixmap('img/sun.png'))

    def changeLabel(self, string):
        now = QDate.currentDate()
        weekDays = [now.addDays(1).toString(Qt.DefaultLocaleShortDate), now.addDays(2).toString(Qt.DefaultLocaleShortDate),
        now.addDays(3).toString(Qt.DefaultLocaleShortDate), now.addDays(4).toString(Qt.DefaultLocaleShortDate),
        now.addDays(5).toString(Qt.DefaultLocaleShortDate), now.addDays(6).toString(Qt.DefaultLocaleShortDate),
        now.addDays(7).toString(Qt.DefaultLocaleShortDate)]
        self.label1.setText(weekDays[string])

    def changeSign(self, index):
        weekWeather = QPixmap()
        weekWeather = ['img/1.png', 'img/2.png', 'img/3.png', 'img/2.png', 'img/7.png', 'img/10.png', 'img/7.png']
        self.label2.setPixmap(QPixmap(weekWeather[index]))

    def changeTempMin(self, string):
        TempMin = ["0°", "-1°", "-2°", "-3°", "-4°", "-5°", "-6°"]
        self.label3.setText(TempMin[string])

    def changeTempMax(self, string):
        TempMax = ["7°", "6°", "5°", "4°", "3°", "2°", "1°"]
        self.label4.setText(TempMax[string])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())
