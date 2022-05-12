from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_demoWindow(object):
    def setupUi(self, demoWindow):
        demoWindow.setObjectName("demoWindow")
        demoWindow.resize(800, 600)
        demoWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Polish, QtCore.QLocale.Poland))
        self.centralwidget = QtWidgets.QWidget(demoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nazwaU = QtWidgets.QTextEdit(self.centralwidget)
        self.nazwaU.setGeometry(QtCore.QRect(590, 20, 201, 21))
        self.nazwaU.setObjectName("nazwaU")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(600, 0, 151, 21))
        self.label.setObjectName("label")
        self.adresA = QtWidgets.QTextEdit(self.centralwidget)
        self.adresA.setGeometry(QtCore.QRect(10, 20, 181, 21))
        self.adresA.setObjectName("adresA")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 131, 16))
        self.label_2.setObjectName("label_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 50, 781, 321))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 779, 319))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.wiadomosci = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.wiadomosci.setGeometry(QtCore.QRect(0, 0, 781, 321))
        self.wiadomosci.setObjectName("wiadomosci")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.wiadomosc = QtWidgets.QTextEdit(self.centralwidget)
        self.wiadomosc.setGeometry(QtCore.QRect(10, 380, 631, 161))
        self.wiadomosc.setObjectName("wiadomosc")
        self.wyslijWiadomosc = QtWidgets.QPushButton(self.centralwidget)
        self.wyslijWiadomosc.setGeometry(QtCore.QRect(650, 410, 131, 91))
        self.wyslijWiadomosc.setObjectName("wyslijWiadomosc")
        demoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(demoWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        demoWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(demoWindow)
        self.statusbar.setObjectName("statusbar")
        demoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(demoWindow)
        QtCore.QMetaObject.connectSlotsByName(demoWindow)

    def retranslateUi(self, demoWindow):
        _translate = QtCore.QCoreApplication.translate
        demoWindow.setWindowTitle(_translate("demoWindow", "GRE Demo Messenger"))
        self.label.setText(_translate("demoWindow", "Nazwa użytkownika"))
        self.label_2.setText(_translate("demoWindow", "Adres IP adresata"))
        self.wyslijWiadomosc.setText(_translate("demoWindow", "Wyślij wiadomość"))

class Ui_komunikator(object):
    def setupUi(self, komunikator):
        komunikator.setObjectName("komunikator")
        komunikator.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(komunikator)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(-1, -1, 801, 521))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 799, 519))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.monitorOut = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.monitorOut.setGeometry(QtCore.QRect(-5, 1, 811, 521))
        self.monitorOut.setObjectName("monitorOut")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.bledyCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.bledyCheck.setGeometry(QtCore.QRect(0, 530, 92, 23))
        self.bledyCheck.setObjectName("bledyCheck")
        self.komCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.komCheck.setGeometry(QtCore.QRect(90, 530, 171, 23))
        self.komCheck.setObjectName("komCheck")
        self.archiwizuj = QtWidgets.QPushButton(self.centralwidget)
        self.archiwizuj.setGeometry(QtCore.QRect(680, 530, 89, 25))
        self.archiwizuj.setLocale(QtCore.QLocale(QtCore.QLocale.Polish, QtCore.QLocale.Poland))
        self.archiwizuj.setObjectName("archiwizuj")
        komunikator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(komunikator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        komunikator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(komunikator)
        self.statusbar.setObjectName("statusbar")
        komunikator.setStatusBar(self.statusbar)

        self.retranslateUi(komunikator)
        QtCore.QMetaObject.connectSlotsByName(komunikator)

    def retranslateUi(self, komunikator):
        _translate = QtCore.QCoreApplication.translate
        komunikator.setWindowTitle(_translate("komunikator", "Monitor"))
        self.bledyCheck.setText(_translate("komunikator", "Błędy"))
        self.komCheck.setText(_translate("komunikator", "Raporty z komunikacji"))
        self.archiwizuj.setText(_translate("komunikator", "Archiwizuj"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    MainWindow2 = QtWidgets.QMainWindow()

    ui1 = Ui_demoWindow()
    ui1.setupUi(MainWindow1)

    ui2 = Ui_komunikator()
    ui2.setupUi(MainWindow2)

    MainWindow1.show()
    MainWindow2.show()

    sys.exit(app.exec_())