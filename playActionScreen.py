# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playActionScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PlayActionWindow(object):
    def setupUi(self, PlayActionWindow):
        PlayActionWindow.setObjectName("PlayActionWindow")
        PlayActionWindow.resize(708, 500)
        self.centralwidget = QtWidgets.QWidget(PlayActionWindow)
        self.centralwidget.setObjectName("centralwidget")
        PlayActionWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PlayActionWindow)
        self.statusbar.setObjectName("statusbar")
        PlayActionWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PlayActionWindow)
        QtCore.QMetaObject.connectSlotsByName(PlayActionWindow)

    def retranslateUi(self, PlayActionWindow):
        _translate = QtCore.QCoreApplication.translate
        PlayActionWindow.setWindowTitle(_translate("PlayActionWindow", "Play Action Window"))
