# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\jagan\plugin\jj\bar.ui'
#
# Created: Tue Jul 16 12:38:16 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_jj(object):
    def setupUi(self, jj):
        jj.setObjectName(_fromUtf8("jj"))
        jj.resize(165, 50)
        self.progressBar = QtGui.QProgressBar(jj)
        self.progressBar.setGeometry(QtCore.QRect(0, 0, 201, 51))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))

        self.retranslateUi(jj)
        QtCore.QMetaObject.connectSlotsByName(jj)

    def retranslateUi(self, jj):
        jj.setWindowTitle(_translate("jj", "jj", None))

