from PyQt5 import QtCore, QtGui, QtWidgets
import math

system = {
    "kerbol": {
        "radius": 261600000,
        "atmosphere": 600000,
        "soi": float('inf'),
        "mass": 1.757e28
    },
    "moho": {
        "radius": 250000,
        "atmosphere": 0,
        "soi": 9646663,
        "mass": 2.526e21,
        "parent": "kerbol"
    },
    "eve": {
        "radius": 700000,
        "atmosphere": 90000,
        "soi": 85109365,
        "mass": 1.224e23,
        "parent": "kerbol"
    },
    "gilly": {
        "radius": 13000,
        "atmosphere": 0,
        "soi": 126123.27,
        "mass": 1.242e17,
        "parent": "eve"
    },
    "kerbin": {
        "radius": 600000,
        "atmosphere": 70000,
        "soi": 	84159286,
        "mass": 5.292e22,
        "parent": "kerbol"
    },
    "mun": {
        "radius": 200000,
        "atmosphere": 0,
        "soi": 2429559.1,
        "mass": 9.760e20,
        "parent": "kerbin"
    },
    "minmus": {
        "radius": 60000,
        "atmosphere": 0,
        "soi": 	2247428.4,
        "mass": 2.646e19,
        "parent": "kerbin"
    },
    "duna": {
        "radius": 320000,
        "atmosphere": 50000,
        "soi": 47921949,
        "mass": 4.515e21,
        "parent": "kerbol"
    },
    "ike": {
        "radius": 130000,
        "atmosphere": 0,
        "soi": 1049598.9,
        "mass": 2.782e20,
        "parent": "duna"
    },
    "dres": {
        "radius": 138000,
        "atmosphere": 0,
        "soi": 32832840,
        "mass": 3.219e20,
        "parent": "kerbol"
    },
    "jool": {
        "radius": 6000000,
        "atmosphere": 200000,
        "soi": 	2455985200,
        "mass": 4.233e24,
        "parent": "kerbol"
    },
    "laythe": {
        "radius": 500000,
        "atmosphere": 50000,
        "soi": 3723645.8,
        "mass": 2.940e22,
        "parent": "jool"
    },
    "vall": {
        "radius": 300000,
        "atmosphere": 0,
        "soi": 	2406401.4,
        "mass": 3.109e21,
        "parent": "jool"
    },
    "tylo": {
        "radius": 600000,
        "atmosphere": 0,
        "soi": 	10856518,
        "mass": 4.233e22,
        "parent": "jool"
    },
    "bop": {
        "radius": 65000,
        "atmosphere": 0,
        "soi": 	1221060.9,
        "mass": 3.726e19,
        "parent": "jool"
    },
    "pol": {
        "radius": 44000,
        "atmosphere": 0,
        "soi": 1042138.9,
        "mass": 1.081e19,
        "parent": "jool"
    },
    "eeloo": {
        "radius": 210000,
        "atmosphere": 0,
        "soi": 119082940,
        "mass": 1.115e21,
        "parent": "kerbol"
    }
}
    
class Ui_MainWindow(object):    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(400, 350)
        MainWindow.setMinimumSize(QtCore.QSize(400, 350))
        MainWindow.setMaximumSize(QtCore.QSize(400, 350))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        MainWindow.setWindowTitle("KSP Konstellations")
        MainWindow.setWindowIcon((QtGui.QIcon('logo.png')))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.parameters = QtWidgets.QFrame(self.centralwidget)
        self.parameters.setGeometry(QtCore.QRect(0, 60, 400, 210))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.parameters.setFont(font)
        self.parameters.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.parameters.setFrameShadow(QtWidgets.QFrame.Raised)
        self.parameters.setObjectName("parameters")
        self.body_select = QtWidgets.QComboBox(self.parameters)
        self.body_select.setGeometry(QtCore.QRect(70, 30, 240, 25))
        self.body_select.setObjectName("body_select")
        self.body_select.addItem("")
        self.body_select.addItem("")
        self.body_select.addItem("")
        self.body_select.addItem("")
        self.body_select.addItem("")
        self.body_select.addItem("")
        self.body_select.addItem("")
        self.body_select.addItem("")
        self.body_select.addItem("")
        self.body_select.addItem("")
        self.body_select.addItem("")
        self.body_select.addItem("")
        self.body_select.addItem("")
        self.body_select.addItem("")
        self.body_select.addItem("")
        self.body_select.addItem("")
        self.body_select.addItem("")
        self.body_select.currentIndexChanged.connect(self.body_change)
        self.body_title = QtWidgets.QLabel(self.parameters)
        self.body_title.setGeometry(QtCore.QRect(70, 0, 240, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.body_title.setFont(font)
        self.body_title.setObjectName("body_title")
        self.finalorbit_title = QtWidgets.QLabel(self.parameters)
        self.finalorbit_title.setGeometry(QtCore.QRect(70, 50, 240, 31))
        self.finalorbit_title.setObjectName("finalorbit_title")
        self.finalorbit_select = QtWidgets.QDoubleSpinBox(self.parameters)
        self.finalorbit_select.setDecimals(0)
        self.finalorbit_select.setGeometry(QtCore.QRect(70, 80, 240, 22))
        self.finalorbit_select.setMaximum(0)
        self.finalorbit_select.setObjectName("finalorbit_select")
        self.amount_title = QtWidgets.QLabel(self.parameters)
        self.amount_title.setGeometry(QtCore.QRect(70, 100, 240, 31))
        self.amount_title.setObjectName("amount_title")
        self.amount_select = QtWidgets.QSpinBox(self.parameters)
        self.amount_select.setGeometry(QtCore.QRect(70, 130, 240, 22))
        self.amount_select.setMinimum(2)
        self.amount_select.setMaximum(1000)
        self.amount_select.setObjectName("amount_select")
        self.periodLimit_title = QtWidgets.QLabel(self.parameters)
        self.periodLimit_title.setGeometry(QtCore.QRect(70, 150, 240, 31))
        self.periodLimit_title.setObjectName("periodLimit_title")
        self.periodLimit_select = QtWidgets.QSpinBox(self.parameters)
        self.periodLimit_select.setGeometry(QtCore.QRect(70, 180, 240, 22))
        self.periodLimit_select.setMinimum(1)
        self.periodLimit_select.setMaximum(1000)
        self.periodLimit_select.setObjectName("periodLimit_select")
        self.periodLimit_select.setValue(10)
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 0, 400, 75))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.execute_button = QtWidgets.QPushButton(self.centralwidget)
        self.execute_button.setGeometry(QtCore.QRect(125, 280, 150, 50))
        self.execute_button.clicked.connect(self.doTheMaths)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.execute_button.setFont(font)
        self.execute_button.setObjectName("execute_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.body_change()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.body_select.setItemText(0, _translate("MainWindow", "Kerbol"))
        self.body_select.setItemText(1, _translate("MainWindow", "Moho"))
        self.body_select.setItemText(2, _translate("MainWindow", "Eve"))
        self.body_select.setItemText(3, _translate("MainWindow", "Gilly"))
        self.body_select.setItemText(4, _translate("MainWindow", "Kerbin"))
        self.body_select.setItemText(5, _translate("MainWindow", "Mun"))
        self.body_select.setItemText(6, _translate("MainWindow", "Minmus"))
        self.body_select.setItemText(7, _translate("MainWindow", "Duna"))
        self.body_select.setItemText(8, _translate("MainWindow", "Ike"))
        self.body_select.setItemText(9, _translate("MainWindow", "Dres"))
        self.body_select.setItemText(10, _translate("MainWindow", "Jool"))
        self.body_select.setItemText(11, _translate("MainWindow", "Laythe"))
        self.body_select.setItemText(12, _translate("MainWindow", "Vall"))
        self.body_select.setItemText(13, _translate("MainWindow", "Tylo"))
        self.body_select.setItemText(14, _translate("MainWindow", "Bop"))
        self.body_select.setItemText(15, _translate("MainWindow", "Pol"))
        self.body_select.setItemText(16, _translate("MainWindow", "Eeloo"))
        self.body_title.setText(_translate("MainWindow", "BODY"))
        self.finalorbit_title.setText(_translate("MainWindow", "FINAL ORBIT"))
        self.amount_title.setText(_translate("MainWindow", "AMOUNT OF SATELLITES"))
        self.periodLimit_title.setText(_translate("MainWindow", "PERIOD LIMIT (at your own risk)"))
        self.title.setText(_translate("MainWindow", "KSP KONSTELLATIONS"))
        self.execute_button.setText(_translate("MainWindow", "Do the maths !"))

    def body_change(self): 
        celestial_body = self.body_select.currentText().lower()
        high_limit = system[celestial_body]["soi"]
        low_limit = system[celestial_body]["atmosphere"]

        if math.isinf(high_limit):
            low_limit /= 1000
            low_limit += 1
            self.finalorbit_select.setMaximum(sys.maxsize)
            self.finalorbit_title.setText(f"FINAL ORBIT (At least {int(low_limit):,}km)")
        else:
            high_limit /= 1000
            low_limit /= 1000
            high_limit -= 1
            low_limit += 1
            self.finalorbit_select.setMaximum(int(high_limit))
            self.finalorbit_title.setText(f"FINAL ORBIT ({int(low_limit):,} - {int(high_limit):,}km)")
        self.finalorbit_select.setMinimum(int(low_limit))
        self.finalorbit_select.setValue(int(low_limit))
        
    def convert_seconds_to_DHMS(self, seconds):
        KSP_DAY_LENGTH = 6 * 60 * 60
        days = seconds // KSP_DAY_LENGTH
        seconds %= KSP_DAY_LENGTH
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return int(days), int(hours), int(minutes), int(seconds)
    
    def err(self, reason):
        self.errDialog = QtWidgets.QDialog()
        self.errDialog.setWindowTitle("KSP Konstellations - ERROR")
        self.resultsLayout = QtWidgets.QVBoxLayout(self.errDialog)

        # Results
        self.errMsg = QtWidgets.QLabel(reason, self.errDialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.errMsg.setFont(font)
        self.errMsg.setStyleSheet('color: red')
        self.errMsg.adjustSize()

        # Remove question mark
        self.errDialog.setWindowFlags(self.errDialog.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
            
        # Add spacing
        self.resultsLayout.addWidget(self.errMsg, alignment=QtCore.Qt.AlignCenter)
        self.resultsLayout.setContentsMargins(15, 15, 15, 15)
        self.errDialog.adjustSize()
        self.errDialog.setFixedSize(self.errMsg.size() + QtCore.QSize(30, 30))

        self.errDialog.setWindowIcon(QtGui.QIcon('logo.png'))
        self.errDialog.setModal(True)
        self.errDialog.exec_()

    
    def doTheMaths(self):
        celestial_body = self.body_select.currentText().lower()

        main_orbit_alt = self.finalorbit_select.value() * 1000
        amount = self.amount_select.value()

        G = 6.6743e-11
        result = f""

        final_period = 2 * math.pi * math.sqrt(((main_orbit_alt + system[celestial_body]["radius"]) ** 3) / (G * system[celestial_body]["mass"]))
        transfer_period = final_period * (1 - (1/amount))
        final_orbit = (G * system[celestial_body]["mass"] * (final_period ** 2) / (4 * math.pi ** 2)) ** (1/3) - system[celestial_body]["radius"]
        semiMajorAxis = ((G * system[celestial_body]["mass"] * (transfer_period / (2 * math.pi)) ** 2) ** (1/3))
        transfer_orbit_periapsis = (2 * semiMajorAxis - final_orbit - system[celestial_body]["radius"]) - system[celestial_body]["radius"]
            
        # Checks
        number = ""
        times = 1
        while transfer_orbit_periapsis + system[celestial_body]["radius"] < system[celestial_body]["radius"] + system[celestial_body]["atmosphere"]:
            transfer_period = final_period * (1 - (1 / (amount * times)))
            semiMajorAxis = ((G * system[celestial_body]["mass"] * (transfer_period / (2 * math.pi)) ** 2) ** (1/3))
            transfer_orbit_periapsis = (2 * semiMajorAxis - final_orbit - system[celestial_body]["radius"]) - system[celestial_body]["radius"]
            times += 1
            number = "s"
            periodLimit = self.periodLimit_select.value()
            if times == periodLimit: return self.err("Too many satellites or orbit is too low (Period limit exceeded)")
            print(transfer_orbit_periapsis, "AND", system[celestial_body]["radius"] + system[celestial_body]["atmosphere"], "AND", transfer_orbit_periapsis < system[celestial_body]["radius"] + system[celestial_body]["atmosphere"])
        
        if times == 1: times = "" 
        else: times = str(times) + " "
        
        result += f"Final orbit: {round(final_orbit / 1000):,}km\n"

        days, hours, minutes, seconds = self.convert_seconds_to_DHMS(transfer_period)
        result += f"Transfer period: {days}d, {hours}h, {minutes}m, {(seconds)}s ({int(transfer_period):,} seconds)\n"

        days, hours, minutes, seconds = self.convert_seconds_to_DHMS(final_period)
        result += f"Final period: {days}d, {hours}h, {minutes}m, {(seconds)}s ({int(final_period):,} seconds)\n"

        result += f"Transfer orbit periapsis: {int(transfer_orbit_periapsis / 1000):,}km\n"

        result += f"Stage every {str(times)}period{number}"

        self.resultsDialog = QtWidgets.QDialog()
        self.resultsDialog.setWindowTitle("KSP Konstellations - Calculations results")
        self.resultsLayout = QtWidgets.QVBoxLayout(self.resultsDialog)

        # Results
        self.results = QtWidgets.QLabel(result, self.resultsDialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.results.setFont(font)
        self.results.adjustSize()

        # Remove question mark
        self.resultsDialog.setWindowFlags(self.resultsDialog.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
            
        # Add spacing
        self.resultsLayout.addWidget(self.results, alignment=QtCore.Qt.AlignCenter)
        self.resultsLayout.setContentsMargins(15, 15, 15, 15)
        self.resultsDialog.adjustSize()
        self.resultsDialog.setFixedSize(self.results.size() + QtCore.QSize(30, 30))

        self.resultsDialog.setWindowIcon(QtGui.QIcon('logo.png'))
        self.resultsDialog.setModal(True)
        self.resultsDialog.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
