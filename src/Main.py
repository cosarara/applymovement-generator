#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#    Copyright © 2011 Jaume Delclòs Coll

#    This file is part of applymovement-gen.

#    Applymovement-gen is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    applymovement-gen is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with applymovement-gen.  If not, see <http://www.gnu.org/licenses/>.

import sys

 # Import Qt modules
from PyQt5 import QtCore, QtGui, QtWidgets

 # Import the compiled UI module
from window import Ui_MainWindow

from _listw import Ui_Form

# Import movement lists
import lists


 # Create a class for our main window
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
         # Iniciar main window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Temp's
        self.tempRuby = ""
        self.tempFR = ""

        # Undo
        self.undoRuby = [""]
        self.undoRubyIndex = 0
        self.undoFR = [""]
        self.undoFRIndex = 0

         # Velocitats
        self.velRuby = 0
        self.velFR = 0
        self.velEmerald = ""

         # Hide
        self.vHideRuby = "visible"
        self.vHideFR = "visible"
        self.vLastIsHideRuby = "0"
        self.vLastIsHideFR = "0"

        #conectem coses Ruby
        self.ui.BotoUp.clicked.connect(self.UpRuby)
        self.ui.BotoDown.clicked.connect(self.DownRuby)
        self.ui.BotoRight.clicked.connect(self.RightRuby)
        self.ui.BotoLeft.clicked.connect(self.LeftRuby)
        self.ui.Botomirar.clicked.connect(self.faceRuby)
        self.ui.Botoslow.clicked.connect(self.slowRuby)
        self.ui.Botowalk.clicked.connect(self.walkRuby)
        self.ui.Botorun.clicked.connect(self.runRuby)
        self.ui.Botojump.clicked.connect(self.jumpRuby)

        self.ui.bSt1Ruby.clicked.connect(self.st1Ruby)
        self.ui.bSt2Ruby.clicked.connect(self.st2Ruby)
        self.ui.bSt3Ruby.clicked.connect(self.st3Ruby)
        self.ui.bSt4Ruby.clicked.connect(self.st4Ruby)
        self.ui.bHideRuby.clicked.connect(self.hideRuby)

        self.ui.ClearRuby.clicked.connect(self.RubyC)
        self.ui.backspaceRuby.clicked.connect(self.GomaRuby)
        self.ui.bAlertRuby.clicked.connect(self.alertRuby)
        self.ui.bQRuby.clicked.connect(self.qRuby)
        self.ui.bLoveRuby.clicked.connect(self.loveRuby)
        self.ui.bEndRuby.clicked.connect(self.endRuby)

        #conectem coses FR
        self.ui.BotoUpFR.clicked.connect(self.UpFR)
        self.ui.BotoDownFR.clicked.connect(self.DownFR)
        self.ui.BotoRightFR.clicked.connect(self.RightFR)
        self.ui.BotoLeftFR.clicked.connect(self.LeftFR)
        self.ui.BotomirarFR.clicked.connect(self.faceFR)
        self.ui.BotoxslowFR.clicked.connect(self.xslowFR)
        self.ui.BotoslowFR.clicked.connect(self.slowFR)
        self.ui.BotowalkFR.clicked.connect(self.walkFR)
        self.ui.BotorunFR.clicked.connect(self.runFR)
        self.ui.BotojumpFR.clicked.connect(self.jumpFR)

        self.ui.bSt1FR.clicked.connect(self.st1FR)
        self.ui.bSt2FR.clicked.connect(self.st2FR)
        self.ui.bSt3FR.clicked.connect(self.st3FR)
        self.ui.bHideFR.clicked.connect(self.hideFR)

        self.ui.ClearFR.clicked.connect(self.FRC)
        self.ui.backspaceFR.clicked.connect(self.GomaFR)
        self.ui.bAlertFR.clicked.connect(self.alertFR)
        self.ui.bAlert2FR.clicked.connect(self.alert2FR)
        self.ui.bQFR.clicked.connect(self.qFR)
        self.ui.bXFR.clicked.connect(self.xFR)
        self.ui.bHappyFR.clicked.connect(self.happyFR)
        self.ui.bEndFR.clicked.connect(self.endFR)
        #menu
        self.ui.actionAbout.triggered.connect(self.aboutmsg)
        self.ui.actionRubyList.triggered.connect(self.RList)
        self.ui.actionFRList.triggered.connect(self.FRList)
        self.windowlist123 = None
        self.ui.actionUndo.triggered.connect(self.undo)
        self.ui.actionRedo.triggered.connect(self.redo)

#-------------Up----------------
  #-------------Ruby----------------
    def UpRuby(self):
        self.tempRuby += get_mov("Ruby", self.velRuby, 1)
        self.update()

#-------------Down----------------
  #-------------Ruby----------------
    def DownRuby(self):
        self.tempRuby += get_mov("Ruby", self.velRuby, 0)
        self.update()

#-------------Right----------------
  #-------------Ruby----------------
    def RightRuby(self):
        self.tempRuby += get_mov("Ruby", self.velRuby, 3)
        self.update()

#-------------Left----------------
  #-------------Ruby----------------
    def LeftRuby(self):
        self.tempRuby += get_mov("Ruby", self.velRuby, 2)
        self.update()

#-------------Up----------------
  #-------------FR----------------
    def UpFR(self):
        self.tempFR += get_mov("FR", self.velFR, 1)
        self.update()

#-------------Down----------------
  #-------------FR----------------
    def DownFR(self):
        self.tempFR += get_mov("FR", self.velFR, 0)
        self.update()

#-------------Right----------------
  #-------------FR----------------
    def RightFR(self):
        self.tempFR += get_mov("FR", self.velFR, 3)
        self.update()

#-------------Left----------------
  #-------------FR----------------
    def LeftFR(self):
        self.tempFR += get_mov("FR", self.velFR, 2)
        self.update()

#-------------Update----------------
# Update gui and undo system
    def update(self):
        self.ui.textFR.setPlainText(self.tempFR)
        self.vLastIsHideFR = "0"
        self.redoFR1 = self.tempFR
        self.ui.textRuby.setPlainText(self.tempRuby)
        self.vLastIsHideRuby = "0"
        self.redoRuby1 = self.tempRuby

        if self.undoRuby[self.undoRubyIndex] != self.tempRuby:
            self.undoRubyIndex += 1
        if len(self.undoRuby) == self.undoRubyIndex:
            self.undoRuby.append(self.tempRuby)
        else:
            self.undoRuby[self.undoRubyIndex] = self.tempRuby
        if self.undoFR[self.undoFRIndex] != self.tempFR:
            self.undoFRIndex += 1
        if len(self.undoFR) == self.undoFRIndex:
            self.undoFR.append(self.tempFR)
        else:
            self.undoFR[self.undoFRIndex] = self.tempFR
        self.scroll_down()

    def scroll_down(self):
        bar = self.ui.textRuby.verticalScrollBar()
        bar.setValue(bar.maximum())

#-------------Velocities----------------
  #-------------Ruby----------------
    def faceRuby(self):
        self.velRuby = 0  # "face"

    def slowRuby(self):
        self.velRuby = 1  # "slow"

    def walkRuby(self):
        self.velRuby = 2  # "walk"

    def runRuby(self):
        self.velRuby = 13  # "run"

    def jumpRuby(self):
        self.velRuby = 17  # "jump"

    def st1Ruby(self):
        self.velRuby = 6  # "st1"

    def st2Ruby(self):
        self.velRuby = 7  # "st2"

    def st3Ruby(self):
        self.velRuby = 8  # "st3"

    def st4Ruby(self):
        self.velRuby = 9  # "st4"

  #-------------FR----------------
    def faceFR(self):
        self.velFR = 0  # "face"

    def xslowFR(self):
        self.velFR = 1  # "xslow"

    def slowFR(self):
        self.velFR = 2  # "slow"

    def walkFR(self):
        self.velFR = 3  # "walk"

    def runFR(self):
        self.velFR = 5  # "run"

    def jumpFR(self):
        self.velFR = 16  # "jump"

    def st1FR(self):
        self.velFR = 6  # "st1"

    def st2FR(self):
        self.velFR = 7  # "st2"

    def st3FR(self):
        self.velFR = 8  # "st3"

#-------------Hide----------------
  #-------------Ruby----------------
    def hideRuby(self):
        if self.vHideRuby == "visible":
            self.vHideRuby = "invisible"
            self.tempRuby += "#raw 0x54 'hide\n"
            self.ui.textRuby.setPlainText(self.tempRuby)
        else:
            self.vHideRuby = "visible"
            self.tempRuby += "#raw 0x55 'show\n"
            self.ui.textRuby.setPlainText(self.tempRuby)
        self.vLastIsHideRuby = "1"
        self.scroll_down()

  #-------------FR----------------
    def hideFR(self):
        if self.vHideFR == "visible":
            self.vHideFR = "invisible"
            self.tempFR += "#raw 0x60 'hide\n"
            self.ui.textFR.setPlainText(self.tempFR)
        else:
            self.vHideFR = "visible"
            self.tempFR += "#raw 0x61 'show\n"
            self.ui.textFR.setPlainText(self.tempFR)
        self.vLastIsHideFR = "1"
        self.scroll_down()

#-------------Clear----------------
  #-------------Ruby----------------
    def RubyC(self):
        self.tempRuby = ""
        self.update()
        if self.vHideRuby == "visible":
            self.vHideRuby = "invisible"
            self.ui.bHideRuby.setChecked(1)
        if self.vHideRuby == "invisible":
            self.vHideRuby = "visible"
            self.ui.bHideRuby.setChecked(0)

  #-------------FR----------------
    def FRC(self):
        self.tempFR = ""
        self.update()
        if self.vHideFR == "visible":
            self.vHideFR = "invisible"
            self.ui.bHideFR.setChecked(1)
        if self.vHideFR == "invisible":
            self.vHideFR = "visible"
            self.ui.bHideFR.setChecked(0)

#-------------Goma----------------
  #-------------Ruby----------------
    def GomaRuby(self):
        self.passalinia = "\n"
        self.abc = \
        "qwertyuiopasdfghjklzxcvbnm, QWERTYUIOPASDFGHJKLZXCVBNM1234567890'#-"
        self.tempRuby = self.tempRuby.rstrip(self.passalinia)
        self.tempRuby = self.tempRuby.rstrip(self.abc)
        self.update()
        if self.vLastIsHideRuby == "1":
            if self.vHideRuby == "visible":
                self.vHideRuby = "invisible"
                self.ui.bHideRuby.setChecked(1)
            elif self.vHideRuby == "invisible":
                self.vHideRuby = "visible"
                self.ui.bHideRuby.setChecked(0)

  #-------------FR----------------
    def GomaFR(self):
        self.passalinia = "\n"
        self.abc = \
        "qwertyuiopasdfghjklzxcvbnm, QWERTYUIOPASDFGHJKLZXCVBNM1234567890'#-"
        self.tempFR = self.tempFR.rstrip(self.passalinia)
        self.tempFR = self.tempFR.rstrip(self.abc)
        self.update()
        if self.vLastIsHideFR == "1":
            if self.vHideFR == "visible":
                self.vHideFR = "invisible"
                self.ui.bHideFR.setChecked(1)
            elif self.vHideFR == "invisible":
                self.vHideFR = "visible"
                self.ui.bHideFR.setChecked(0)

#-------------Icons----------------
  #-------------alertRuby----------------
    def alertRuby(self):
        self.tempRuby += get_mov("Ruby", 23, 0)  # "#raw 0x56 '!\n"
        self.update()

  #-------------?Ruby----------------
    def qRuby(self):
        self.tempRuby += get_mov("Ruby", 23, 1)  # "#raw 0x57 '?\n"
        self.update()

  #-------------loveRuby----------------
    def loveRuby(self):
        self.tempRuby += get_mov("Ruby", 23, 2)  # "#raw 0x58 '<3\n"
        self.update()

  #-------------alertFR----------------
    def alertFR(self):
        self.tempFR += get_mov("FR", 19, 0)  # "#raw 0x62 '!\n"
        self.update()

  #-------------alert2FR----------------
    def alert2FR(self):
        self.tempFR += get_mov("FR", 19, 3)  # "#raw 0x65 '!!\n"
        self.update()

  #-------------?FR----------------
    def qFR(self):
        self.tempFR += get_mov("FR", 19, 1)  # "#raw 0x63 '?\n"
        self.update()

  #-------------xFR----------------
    def xFR(self):
        self.tempFR += get_mov("FR", 19, 2)  # "#raw 0x64 'X\n"
        self.update()

  #-------------happyFR----------------
    def happyFR(self):
        self.tempFR += get_mov("FR", 19, 4)  # "#raw 0x66 '^^\n"
        self.update()

  #-------------FE-FR----------------
    def endFR(self):
        self.tempFR += "#raw 0xFE 'End\n"
        self.update()

  #-------------FE-Ruby----------------
    def endRuby(self):
        self.tempRuby += "#raw 0xFE 'End\n"
        self.update()

#-------------Menu----------------
 #-------------Help----------------
  #-------------About----------------
    def aboutmsg(self):
        QtWidgets.QMessageBox.about(self,
                                "About applymovement-gen",
                                "Applymovement-gen v2.0.0 \
                                \nCopyright © Jaume Delclos (cosarara97)")

 #-------------Tools----------------
  #-------------Ruby List----------------
    def RList(self):
        self.ollist = llista()
        self.ollist.show()
        fileName = "./ruby.txt"
        filer = open(fileName).read()
        self.ollist.wlist.textBrowser.setPlainText(filer)

  #-------------FR List----------------
    def FRList(self):
        self.ollist = llista()
        self.ollist.show()
        fileName = "./FR.txt"
        filer = open(fileName).read()
        self.ollist.wlist.textBrowser.setPlainText(filer)

 #----------------Edit----------------
    def undo(self):
        if self.undoRubyIndex != 0:
            self.undoRubyIndex -= 1
            self.tempRuby = self.undoRuby[self.undoRubyIndex]
            self.ui.textRuby.setPlainText(self.tempRuby)
        if self.undoFRIndex != 0:
            self.undoFRIndex -= 1
            self.tempFR = self.undoFR[self.undoFRIndex]
            self.ui.textFR.setPlainText(self.tempFR)
        self.scroll_down()

    def redo(self):
        if self.undoRubyIndex != len(self.undoRuby) - 1:
            self.undoRubyIndex += 1
            self.tempRuby = self.undoRuby[self.undoRubyIndex]
            self.ui.textRuby.setPlainText(self.tempRuby)
        if self.undoFRIndex != len(self.undoFR) - 1:
            self.undoFRIndex += 1
            self.tempFR = self.undoFR[self.undoFRIndex]
            self.ui.textFR.setPlainText(self.tempFR)
        self.scroll_down()


#-------------Get moves----------------
def get_mov(game, vel, direction):
    if game == "Ruby":
        if vel == "":
            return "'(Please select a velocity)\n"
        mov = lists.ruby_list[vel][direction] + "\n"
    elif game == "FR":
        if vel == "":
            return "'(Please select a velocity)\n"
        mov = lists.fr_list[vel][direction] + "\n"
    else:
        print("Error asdf! Please tell cosarara97!")
    return mov


#-------------List Window----------------
class llista(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.wlist = Ui_Form()
        self.wlist.setupUi(self)


# --- Main ---

def main():
    app = QtWidgets.QApplication(sys.argv)
    window123 = Main()
    window123.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
