# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(516, 418)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("applymovement-generator2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.Ruby = QtWidgets.QWidget()
        self.Ruby.setObjectName("Ruby")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Ruby)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textRuby = QtWidgets.QTextBrowser(self.Ruby)
        self.textRuby.setObjectName("textRuby")
        self.verticalLayout_2.addWidget(self.textRuby)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bAlertRuby = QtWidgets.QPushButton(self.Ruby)
        self.bAlertRuby.setMaximumSize(QtCore.QSize(60, 16777215))
        self.bAlertRuby.setObjectName("bAlertRuby")
        self.horizontalLayout_3.addWidget(self.bAlertRuby)
        self.bQRuby = QtWidgets.QPushButton(self.Ruby)
        self.bQRuby.setMaximumSize(QtCore.QSize(60, 16777215))
        self.bQRuby.setObjectName("bQRuby")
        self.horizontalLayout_3.addWidget(self.bQRuby)
        self.bLoveRuby = QtWidgets.QPushButton(self.Ruby)
        self.bLoveRuby.setMaximumSize(QtCore.QSize(60, 16777215))
        self.bLoveRuby.setObjectName("bLoveRuby")
        self.horizontalLayout_3.addWidget(self.bLoveRuby)
        self.bEndRuby = QtWidgets.QPushButton(self.Ruby)
        self.bEndRuby.setMaximumSize(QtCore.QSize(60, 16777215))
        self.bEndRuby.setObjectName("bEndRuby")
        self.horizontalLayout_3.addWidget(self.bEndRuby)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Botomirar = QtWidgets.QRadioButton(self.Ruby)
        self.Botomirar.setChecked(True)
        self.Botomirar.setObjectName("Botomirar")
        self.gridLayout_2.addWidget(self.Botomirar, 0, 0, 1, 1)
        self.Botoslow = QtWidgets.QRadioButton(self.Ruby)
        self.Botoslow.setObjectName("Botoslow")
        self.gridLayout_2.addWidget(self.Botoslow, 1, 0, 1, 1)
        self.Botowalk = QtWidgets.QRadioButton(self.Ruby)
        self.Botowalk.setObjectName("Botowalk")
        self.gridLayout_2.addWidget(self.Botowalk, 2, 0, 1, 1)
        self.Botorun = QtWidgets.QRadioButton(self.Ruby)
        self.Botorun.setObjectName("Botorun")
        self.gridLayout_2.addWidget(self.Botorun, 3, 0, 1, 1)
        self.Botojump = QtWidgets.QRadioButton(self.Ruby)
        self.Botojump.setObjectName("Botojump")
        self.gridLayout_2.addWidget(self.Botojump, 4, 0, 1, 1)
        self.bSt1Ruby = QtWidgets.QRadioButton(self.Ruby)
        self.bSt1Ruby.setObjectName("bSt1Ruby")
        self.gridLayout_2.addWidget(self.bSt1Ruby, 0, 1, 1, 1)
        self.bSt3Ruby = QtWidgets.QRadioButton(self.Ruby)
        self.bSt3Ruby.setObjectName("bSt3Ruby")
        self.gridLayout_2.addWidget(self.bSt3Ruby, 2, 1, 1, 1)
        self.bSt4Ruby = QtWidgets.QRadioButton(self.Ruby)
        self.bSt4Ruby.setObjectName("bSt4Ruby")
        self.gridLayout_2.addWidget(self.bSt4Ruby, 3, 1, 1, 1)
        self.bSt2Ruby = QtWidgets.QRadioButton(self.Ruby)
        self.bSt2Ruby.setObjectName("bSt2Ruby")
        self.gridLayout_2.addWidget(self.bSt2Ruby, 1, 1, 1, 1)
        self.bHideRuby = QtWidgets.QCheckBox(self.Ruby)
        self.bHideRuby.setObjectName("bHideRuby")
        self.gridLayout_2.addWidget(self.bHideRuby, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.BotoUp = QtWidgets.QPushButton(self.Ruby)
        self.BotoUp.setMaximumSize(QtCore.QSize(52, 16777215))
        self.BotoUp.setObjectName("BotoUp")
        self.gridLayout.addWidget(self.BotoUp, 0, 1, 1, 1)
        self.BotoLeft = QtWidgets.QPushButton(self.Ruby)
        self.BotoLeft.setMaximumSize(QtCore.QSize(52, 16777215))
        self.BotoLeft.setObjectName("BotoLeft")
        self.gridLayout.addWidget(self.BotoLeft, 1, 0, 1, 1)
        self.BotoRight = QtWidgets.QPushButton(self.Ruby)
        self.BotoRight.setMaximumSize(QtCore.QSize(52, 16777215))
        self.BotoRight.setObjectName("BotoRight")
        self.gridLayout.addWidget(self.BotoRight, 1, 2, 1, 1)
        self.BotoDown = QtWidgets.QPushButton(self.Ruby)
        self.BotoDown.setMaximumSize(QtCore.QSize(52, 16777215))
        self.BotoDown.setObjectName("BotoDown")
        self.gridLayout.addWidget(self.BotoDown, 2, 1, 1, 1)
        self.ClearRuby = QtWidgets.QPushButton(self.Ruby)
        self.ClearRuby.setMaximumSize(QtCore.QSize(52, 16777215))
        self.ClearRuby.setObjectName("ClearRuby")
        self.gridLayout.addWidget(self.ClearRuby, 1, 1, 1, 1)
        self.backspaceRuby = QtWidgets.QPushButton(self.Ruby)
        self.backspaceRuby.setMaximumSize(QtCore.QSize(52, 16777215))
        self.backspaceRuby.setObjectName("backspaceRuby")
        self.gridLayout.addWidget(self.backspaceRuby, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.Ruby, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.TextFR = QtWidgets.QVBoxLayout()
        self.TextFR.setObjectName("TextFR")
        self.textFR = QtWidgets.QTextBrowser(self.tab)
        self.textFR.setObjectName("textFR")
        self.TextFR.addWidget(self.textFR)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.bAlertFR = QtWidgets.QPushButton(self.tab)
        self.bAlertFR.setMaximumSize(QtCore.QSize(40, 16777215))
        self.bAlertFR.setObjectName("bAlertFR")
        self.horizontalLayout_6.addWidget(self.bAlertFR)
        self.bAlert2FR = QtWidgets.QPushButton(self.tab)
        self.bAlert2FR.setMaximumSize(QtCore.QSize(40, 16777215))
        self.bAlert2FR.setObjectName("bAlert2FR")
        self.horizontalLayout_6.addWidget(self.bAlert2FR)
        self.bQFR = QtWidgets.QPushButton(self.tab)
        self.bQFR.setMaximumSize(QtCore.QSize(40, 16777215))
        self.bQFR.setObjectName("bQFR")
        self.horizontalLayout_6.addWidget(self.bQFR)
        self.bXFR = QtWidgets.QPushButton(self.tab)
        self.bXFR.setMaximumSize(QtCore.QSize(40, 16777215))
        self.bXFR.setObjectName("bXFR")
        self.horizontalLayout_6.addWidget(self.bXFR)
        self.bHappyFR = QtWidgets.QPushButton(self.tab)
        self.bHappyFR.setMaximumSize(QtCore.QSize(40, 16777215))
        self.bHappyFR.setObjectName("bHappyFR")
        self.horizontalLayout_6.addWidget(self.bHappyFR)
        self.bEndFR = QtWidgets.QPushButton(self.tab)
        self.bEndFR.setMaximumSize(QtCore.QSize(60, 16777215))
        self.bEndFR.setObjectName("bEndFR")
        self.horizontalLayout_6.addWidget(self.bEndFR)
        self.TextFR.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2.addLayout(self.TextFR)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.bSt1FR = QtWidgets.QRadioButton(self.tab)
        self.bSt1FR.setObjectName("bSt1FR")
        self.gridLayout_3.addWidget(self.bSt1FR, 1, 1, 1, 1)
        self.bSt2FR = QtWidgets.QRadioButton(self.tab)
        self.bSt2FR.setObjectName("bSt2FR")
        self.gridLayout_3.addWidget(self.bSt2FR, 2, 1, 1, 1)
        self.bSt3FR = QtWidgets.QRadioButton(self.tab)
        self.bSt3FR.setObjectName("bSt3FR")
        self.gridLayout_3.addWidget(self.bSt3FR, 3, 1, 1, 1)
        self.BotojumpFR = QtWidgets.QRadioButton(self.tab)
        self.BotojumpFR.setObjectName("BotojumpFR")
        self.gridLayout_3.addWidget(self.BotojumpFR, 0, 1, 1, 1)
        self.BotomirarFR = QtWidgets.QRadioButton(self.tab)
        self.BotomirarFR.setChecked(True)
        self.BotomirarFR.setObjectName("BotomirarFR")
        self.gridLayout_3.addWidget(self.BotomirarFR, 0, 0, 1, 1)
        self.BotoxslowFR = QtWidgets.QRadioButton(self.tab)
        self.BotoxslowFR.setObjectName("BotoxslowFR")
        self.gridLayout_3.addWidget(self.BotoxslowFR, 1, 0, 1, 1)
        self.BotoslowFR = QtWidgets.QRadioButton(self.tab)
        self.BotoslowFR.setObjectName("BotoslowFR")
        self.gridLayout_3.addWidget(self.BotoslowFR, 2, 0, 1, 1)
        self.BotowalkFR = QtWidgets.QRadioButton(self.tab)
        self.BotowalkFR.setObjectName("BotowalkFR")
        self.gridLayout_3.addWidget(self.BotowalkFR, 3, 0, 1, 1)
        self.BotorunFR = QtWidgets.QRadioButton(self.tab)
        self.BotorunFR.setObjectName("BotorunFR")
        self.gridLayout_3.addWidget(self.BotorunFR, 4, 0, 1, 1)
        self.bHideFR = QtWidgets.QCheckBox(self.tab)
        self.bHideFR.setObjectName("bHideFR")
        self.gridLayout_3.addWidget(self.bHideFR, 4, 1, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_3)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.BotoUpFR = QtWidgets.QPushButton(self.tab)
        self.BotoUpFR.setMaximumSize(QtCore.QSize(52, 16777215))
        self.BotoUpFR.setObjectName("BotoUpFR")
        self.gridLayout_6.addWidget(self.BotoUpFR, 0, 1, 1, 1)
        self.BotoLeftFR = QtWidgets.QPushButton(self.tab)
        self.BotoLeftFR.setMaximumSize(QtCore.QSize(52, 16777215))
        self.BotoLeftFR.setObjectName("BotoLeftFR")
        self.gridLayout_6.addWidget(self.BotoLeftFR, 1, 0, 1, 1)
        self.BotoRightFR = QtWidgets.QPushButton(self.tab)
        self.BotoRightFR.setMaximumSize(QtCore.QSize(52, 16777215))
        self.BotoRightFR.setObjectName("BotoRightFR")
        self.gridLayout_6.addWidget(self.BotoRightFR, 1, 2, 1, 1)
        self.BotoDownFR = QtWidgets.QPushButton(self.tab)
        self.BotoDownFR.setMaximumSize(QtCore.QSize(52, 16777215))
        self.BotoDownFR.setObjectName("BotoDownFR")
        self.gridLayout_6.addWidget(self.BotoDownFR, 2, 1, 1, 1)
        self.backspaceFR = QtWidgets.QPushButton(self.tab)
        self.backspaceFR.setMaximumSize(QtCore.QSize(52, 16777215))
        self.backspaceFR.setObjectName("backspaceFR")
        self.gridLayout_6.addWidget(self.backspaceFR, 0, 0, 1, 1)
        self.ClearFR = QtWidgets.QPushButton(self.tab)
        self.ClearFR.setMaximumSize(QtCore.QSize(52, 16777215))
        self.ClearFR.setObjectName("ClearFR")
        self.gridLayout_6.addWidget(self.ClearFR, 1, 1, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_6)
        self.verticalLayout_8.addLayout(self.verticalLayout_9)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout_10.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 516, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionFRList = QtWidgets.QAction(MainWindow)
        self.actionFRList.setObjectName("actionFRList")
        self.actionRubyList = QtWidgets.QAction(MainWindow)
        self.actionRubyList.setObjectName("actionRubyList")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.menuHelp.addAction(self.actionAbout)
        self.menuTools.addAction(self.actionRubyList)
        self.menuTools.addAction(self.actionFRList)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "applymovement-gen"))
        self.textRuby.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans\'; font-size:10pt;\"><br /></p></body></html>"))
        self.bAlertRuby.setText(_translate("MainWindow", "!"))
        self.bQRuby.setText(_translate("MainWindow", "?"))
        self.bLoveRuby.setText(_translate("MainWindow", "<3"))
        self.bEndRuby.setText(_translate("MainWindow", "END"))
        self.Botomirar.setText(_translate("MainWindow", "Face"))
        self.Botoslow.setText(_translate("MainWindow", "Slow"))
        self.Botowalk.setText(_translate("MainWindow", "Walk"))
        self.Botorun.setText(_translate("MainWindow", "Run"))
        self.Botojump.setText(_translate("MainWindow", "Jump"))
        self.bSt1Ruby.setText(_translate("MainWindow", "St1"))
        self.bSt3Ruby.setText(_translate("MainWindow", "St3"))
        self.bSt4Ruby.setText(_translate("MainWindow", "St4"))
        self.bSt2Ruby.setText(_translate("MainWindow", "St2"))
        self.bHideRuby.setText(_translate("MainWindow", "Hide"))
        self.BotoUp.setText(_translate("MainWindow", "Up"))
        self.BotoLeft.setText(_translate("MainWindow", "Left"))
        self.BotoRight.setText(_translate("MainWindow", "Right"))
        self.BotoDown.setText(_translate("MainWindow", "Down"))
        self.ClearRuby.setText(_translate("MainWindow", "Clear"))
        self.backspaceRuby.setText(_translate("MainWindow", "←"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Ruby), _translate("MainWindow", "R/S/E"))
        self.textFR.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans\'; font-size:10pt;\"><br /></p></body></html>"))
        self.bAlertFR.setText(_translate("MainWindow", "!"))
        self.bAlert2FR.setText(_translate("MainWindow", "!!"))
        self.bQFR.setText(_translate("MainWindow", "?"))
        self.bXFR.setText(_translate("MainWindow", "X"))
        self.bHappyFR.setText(_translate("MainWindow", "^^"))
        self.bEndFR.setText(_translate("MainWindow", "END"))
        self.bSt1FR.setText(_translate("MainWindow", "St1"))
        self.bSt2FR.setText(_translate("MainWindow", "St2"))
        self.bSt3FR.setText(_translate("MainWindow", "St3"))
        self.BotojumpFR.setText(_translate("MainWindow", "Jump"))
        self.BotomirarFR.setText(_translate("MainWindow", "Face"))
        self.BotoxslowFR.setText(_translate("MainWindow", "Very Slow"))
        self.BotoslowFR.setText(_translate("MainWindow", "Slow"))
        self.BotowalkFR.setText(_translate("MainWindow", "Walk"))
        self.BotorunFR.setText(_translate("MainWindow", "Run"))
        self.bHideFR.setText(_translate("MainWindow", "Hide"))
        self.BotoUpFR.setText(_translate("MainWindow", "Up"))
        self.BotoLeftFR.setText(_translate("MainWindow", "Left"))
        self.BotoRightFR.setText(_translate("MainWindow", "Right"))
        self.BotoDownFR.setText(_translate("MainWindow", "Down"))
        self.backspaceFR.setText(_translate("MainWindow", "←"))
        self.ClearFR.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "FR/LG"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionFRList.setText(_translate("MainWindow", "FR List"))
        self.actionRubyList.setText(_translate("MainWindow", "Ruby List"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
