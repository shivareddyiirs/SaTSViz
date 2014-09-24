# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_gis.ui'
#
# Created: Wed Jun 26 15:13:50 2013
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

class Ui_gis(object):
    def setupUi(self, gis):
        gis.setObjectName(_fromUtf8("gis"))
        gis.resize(462, 404)
        self.buttonBox = QtGui.QDialogButtonBox(gis)
        self.buttonBox.setGeometry(QtCore.QRect(30, 320, 411, 71))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(gis)
        self.label.setGeometry(QtCore.QRect(90, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(gis)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(gis)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(gis)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(gis)
        self.label_5.setGeometry(QtCore.QRect(20, 230, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.comboBox = QtGui.QComboBox(gis)
        self.comboBox.setGeometry(QtCore.QRect(150, 270, 221, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox_2 = QtGui.QComboBox(gis)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 150, 221, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_3 = QtGui.QComboBox(gis)
        self.comboBox_3.setGeometry(QtCore.QRect(150, 190, 221, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.label_6 = QtGui.QLabel(gis)
        self.label_6.setGeometry(QtCore.QRect(20, 270, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.comboBox_5 = QtGui.QComboBox(gis)
        self.comboBox_5.setGeometry(QtCore.QRect(150, 230, 221, 21))
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
	self.comboBox_6 = QtGui.QComboBox(gis)
        self.comboBox_6.setGeometry(QtCore.QRect(150, 60, 221, 25))
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        #self.textBrowser = QtGui.QTextBrowser(gis)
        #self.textBrowser.setGeometry(QtCore.QRect(150, 60, 191, 31))
        #self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.toolButton = QtGui.QToolButton(gis)
        self.toolButton.setGeometry(QtCore.QRect(370, 60, 61, 25))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.label_7 = QtGui.QLabel(gis)
        self.label_7.setGeometry(QtCore.QRect(20, 105, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.comboBox_4 = QtGui.QComboBox(gis)
        self.comboBox_4.setGeometry(QtCore.QRect(150, 110, 221, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
	

        self.retranslateUi(gis)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), gis.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), gis.reject)
        QtCore.QMetaObject.connectSlotsByName(gis)

    def retranslateUi(self, gis):
        gis.setWindowTitle(_translate("gis", "gis", None))
        gis.setToolTip(_translate("gis", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label.setText(_translate("gis", " 	   SaTSViz", None))
        self.label_2.setText(_translate("gis", "  File  ", None))
        self.label_3.setText(_translate("gis", "Case ", None))
        self.label_4.setText(_translate("gis", "Control", None))
        self.label_5.setText(_translate("gis", "Population", None))
        self.label_6.setText(_translate("gis", "Date", None))
        self.toolButton.setText(_translate("gis", "...", None))
        self.label_7.setText(_translate("gis", "Location ID", None))
	

