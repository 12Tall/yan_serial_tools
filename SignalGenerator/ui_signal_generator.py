# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(364, 475)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.grpSignalGenerator = QGroupBox(self.centralwidget)
        self.grpSignalGenerator.setObjectName(u"grpSignalGenerator")
        self.grpSignalGenerator.setGeometry(QRect(20, 20, 321, 191))
        self.layoutWidget_2 = QWidget(self.grpSignalGenerator)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 20, 305, 158))
        self.gridLayout_1 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_1.setObjectName(u"gridLayout_1")
        self.gridLayout_1.setContentsMargins(0, 0, 0, 0)
        self.sg_btn_RefreshCOM = QPushButton(self.layoutWidget_2)
        self.sg_btn_RefreshCOM.setObjectName(u"sg_btn_RefreshCOM")

        self.gridLayout_1.addWidget(self.sg_btn_RefreshCOM, 0, 3, 1, 1)

        self.sg_lbl_COMList = QLabel(self.layoutWidget_2)
        self.sg_lbl_COMList.setObjectName(u"sg_lbl_COMList")

        self.gridLayout_1.addWidget(self.sg_lbl_COMList, 0, 0, 1, 1)

        self.sg_txt_Baudrate = QLineEdit(self.layoutWidget_2)
        self.sg_txt_Baudrate.setObjectName(u"sg_txt_Baudrate")
        self.sg_txt_Baudrate.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_1.addWidget(self.sg_txt_Baudrate, 1, 1, 1, 2)

        self.sg_lbl_Baudrate = QLabel(self.layoutWidget_2)
        self.sg_lbl_Baudrate.setObjectName(u"sg_lbl_Baudrate")

        self.gridLayout_1.addWidget(self.sg_lbl_Baudrate, 1, 0, 1, 1)

        self.sg_lbl_Paritybit = QLabel(self.layoutWidget_2)
        self.sg_lbl_Paritybit.setObjectName(u"sg_lbl_Paritybit")

        self.gridLayout_1.addWidget(self.sg_lbl_Paritybit, 4, 0, 1, 1)

        self.sg_slt_COMList = QComboBox(self.layoutWidget_2)
        self.sg_slt_COMList.setObjectName(u"sg_slt_COMList")

        self.gridLayout_1.addWidget(self.sg_slt_COMList, 0, 1, 1, 2)

        self.sg_lbl_Stopbit = QLabel(self.layoutWidget_2)
        self.sg_lbl_Stopbit.setObjectName(u"sg_lbl_Stopbit")

        self.gridLayout_1.addWidget(self.sg_lbl_Stopbit, 3, 0, 1, 1)

        self.sg_lbl_Databit = QLabel(self.layoutWidget_2)
        self.sg_lbl_Databit.setObjectName(u"sg_lbl_Databit")

        self.gridLayout_1.addWidget(self.sg_lbl_Databit, 2, 0, 1, 1)

        self.sg_slt_Databit = QComboBox(self.layoutWidget_2)
        self.sg_slt_Databit.setObjectName(u"sg_slt_Databit")

        self.gridLayout_1.addWidget(self.sg_slt_Databit, 2, 1, 1, 1)

        self.sg_slt_Stopbit = QComboBox(self.layoutWidget_2)
        self.sg_slt_Stopbit.setObjectName(u"sg_slt_Stopbit")

        self.gridLayout_1.addWidget(self.sg_slt_Stopbit, 3, 1, 1, 1)

        self.sg_slt_Paritybit = QComboBox(self.layoutWidget_2)
        self.sg_slt_Paritybit.setObjectName(u"sg_slt_Paritybit")

        self.gridLayout_1.addWidget(self.sg_slt_Paritybit, 4, 1, 1, 2)

        self.sg_btn_Start = QPushButton(self.layoutWidget_2)
        self.sg_btn_Start.setObjectName(u"sg_btn_Start")

        self.gridLayout_1.addWidget(self.sg_btn_Start, 5, 1, 1, 1)

        self.sg_btn_Stop = QPushButton(self.layoutWidget_2)
        self.sg_btn_Stop.setObjectName(u"sg_btn_Stop")

        self.gridLayout_1.addWidget(self.sg_btn_Stop, 5, 2, 1, 1)

        self.grp_SignalParameters = QGroupBox(self.centralwidget)
        self.grp_SignalParameters.setObjectName(u"grp_SignalParameters")
        self.grp_SignalParameters.setGeometry(QRect(20, 230, 311, 191))
        self.layoutWidget = QWidget(self.grp_SignalParameters)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 281, 152))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbl_signal_A = QLabel(self.layoutWidget)
        self.lbl_signal_A.setObjectName(u"lbl_signal_A")

        self.gridLayout_2.addWidget(self.lbl_signal_A, 0, 1, 1, 1)

        self.lbl_signal_Omega = QLabel(self.layoutWidget)
        self.lbl_signal_Omega.setObjectName(u"lbl_signal_Omega")

        self.gridLayout_2.addWidget(self.lbl_signal_Omega, 1, 1, 1, 1)

        self.txt_signal_Phi = QLineEdit(self.layoutWidget)
        self.txt_signal_Phi.setObjectName(u"txt_signal_Phi")

        self.gridLayout_2.addWidget(self.txt_signal_Phi, 2, 2, 1, 1)

        self.txt_signal_Freq = QLineEdit(self.layoutWidget)
        self.txt_signal_Freq.setObjectName(u"txt_signal_Freq")

        self.gridLayout_2.addWidget(self.txt_signal_Freq, 3, 2, 1, 1)

        self.rad_signal_Cos = QRadioButton(self.layoutWidget)
        self.rad_signal_Cos.setObjectName(u"rad_signal_Cos")
        self.rad_signal_Cos.setChecked(True)

        self.gridLayout_2.addWidget(self.rad_signal_Cos, 0, 0, 1, 1)

        self.rad_signal_Delta = QRadioButton(self.layoutWidget)
        self.rad_signal_Delta.setObjectName(u"rad_signal_Delta")
        self.rad_signal_Delta.setEnabled(False)

        self.gridLayout_2.addWidget(self.rad_signal_Delta, 1, 0, 1, 1)

        self.lbl_signal_Freq = QLabel(self.layoutWidget)
        self.lbl_signal_Freq.setObjectName(u"lbl_signal_Freq")

        self.gridLayout_2.addWidget(self.lbl_signal_Freq, 3, 1, 1, 1)

        self.txt_signal_Omega = QLineEdit(self.layoutWidget)
        self.txt_signal_Omega.setObjectName(u"txt_signal_Omega")

        self.gridLayout_2.addWidget(self.txt_signal_Omega, 1, 2, 1, 1)

        self.rad_signal_Heaviside = QRadioButton(self.layoutWidget)
        self.rad_signal_Heaviside.setObjectName(u"rad_signal_Heaviside")
        self.rad_signal_Heaviside.setEnabled(False)

        self.gridLayout_2.addWidget(self.rad_signal_Heaviside, 2, 0, 1, 1)

        self.lbl_signal_Frequency = QLabel(self.layoutWidget)
        self.lbl_signal_Frequency.setObjectName(u"lbl_signal_Frequency")

        self.gridLayout_2.addWidget(self.lbl_signal_Frequency, 3, 0, 1, 1)

        self.lbl_signal_Phi = QLabel(self.layoutWidget)
        self.lbl_signal_Phi.setObjectName(u"lbl_signal_Phi")

        self.gridLayout_2.addWidget(self.lbl_signal_Phi, 2, 1, 1, 1)

        self.txt_signal_A = QLineEdit(self.layoutWidget)
        self.txt_signal_A.setObjectName(u"txt_signal_A")

        self.gridLayout_2.addWidget(self.txt_signal_A, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 364, 23))
        self.menu_About = QMenu(self.menubar)
        self.menu_About.setObjectName(u"menu_About")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_About.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u4fe1\u53f7\u53d1\u751f\u5668\uff08v0.1\uff09", None))
        self.grpSignalGenerator.setTitle(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u53c2\u6570", None))
        self.sg_btn_RefreshCOM.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.sg_lbl_COMList.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u4e32\u53e3\uff1a", None))
        self.sg_txt_Baudrate.setText(QCoreApplication.translate("MainWindow", u"9600", None))
        self.sg_lbl_Baudrate.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387\uff1a", None))
        self.sg_lbl_Paritybit.setText(QCoreApplication.translate("MainWindow", u"\u6821\u9a8c\u4f4d\uff1a", None))
        self.sg_slt_COMList.setPlaceholderText("")
        self.sg_lbl_Stopbit.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u4f4d\uff1a", None))
        self.sg_lbl_Databit.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u4f4d\uff1a", None))
        self.sg_btn_Start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.sg_btn_Stop.setText(QCoreApplication.translate("MainWindow", u"\u7ec8\u6b62", None))
        self.grp_SignalParameters.setTitle(QCoreApplication.translate("MainWindow", u"\u4fe1\u53f7\u53c2\u6570\uff08\u5f27\u5ea6\u5236\uff09\uff1a", None))
        self.lbl_signal_A.setText(QCoreApplication.translate("MainWindow", u"A =", None))
        self.lbl_signal_Omega.setText(QCoreApplication.translate("MainWindow", u"\u03c9=", None))
        self.txt_signal_Phi.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txt_signal_Freq.setText(QCoreApplication.translate("MainWindow", u"0.001", None))
        self.rad_signal_Cos.setText(QCoreApplication.translate("MainWindow", u"y=A*cos(\u03c9t+\u03c6)", None))
        self.rad_signal_Delta.setText(QCoreApplication.translate("MainWindow", u"y=\u03b4(t) \u5355\u4f4d\u8109\u51b2", None))
        self.lbl_signal_Freq.setText(QCoreApplication.translate("MainWindow", u"f =", None))
        self.txt_signal_Omega.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.rad_signal_Heaviside.setText(QCoreApplication.translate("MainWindow", u"y=H(t) \u5355\u4f4d\u9636\u8dc3\u51fd\u6570", None))
        self.lbl_signal_Frequency.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u6837\u9891\u7387(s)\uff1a", None))
        self.lbl_signal_Phi.setText(QCoreApplication.translate("MainWindow", u"\u03c6=", None))
        self.txt_signal_A.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.menu_About.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

