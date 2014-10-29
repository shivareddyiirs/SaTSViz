# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ffDialog
                                 A QGIS plugin
 ff
                             -------------------
        begin                : 2013-06-25
        copyright            : (C) 2013 by Jolly Singh and Jagandeep Singh
        email                : jagandeep28 and jolly.nitgoa@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_ff import Ui_ff
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from shapefile import *
# create the dialog for zoom to point


class ffDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_ff()
        self.ui.setupUi(self)
        self.fcheck()
        self.var=999
        self.var2=999
        self.var1=999
        self.var3=999
        self.var4=999
        self.line='\0'
        self.line1='\0'
        self.line2='\0'
        self.ui.radioButton_14.setDisabled(True)
        QObject.connect(self.ui.toolButton_2,SIGNAL("clicked()"),self.sscan)
        QObject.connect(self.ui.radioButton,SIGNAL("clicked()"),self.enb_g2)
        QObject.connect(self.ui.radioButton_5,SIGNAL("clicked()"),self.enb_g2)
        QObject.connect(self.ui.radioButton_2,SIGNAL("clicked()"),self.enb_g2)
        QObject.connect(self.ui.radioButton_3,SIGNAL("clicked()"),self.enb_g2)
        QObject.connect(self.ui.radioButton_4,SIGNAL("clicked()"),self.enb_g2)
        QObject.connect(self.ui.radioButton_6,SIGNAL("clicked()"),self.enb_g2)
        QObject.connect(self.ui.radioButton_21,SIGNAL("clicked()"),self.enb_g1)
        QObject.connect(self.ui.radioButton_22,SIGNAL("clicked()"),self.enb_gg1)
        QObject.connect(self.ui.radioButton_23,SIGNAL("clicked()"),self.enb_gg1)
        QObject.connect(self.ui.radioButton_24,SIGNAL("clicked()"),self.enb_gg1)
        QObject.connect(self.ui.radioButton_25,SIGNAL("clicked()"),self.enb_gg1)
        

    def fcheck(self):
        self.ui.radioButton.setChecked(True)
        self.ui.radioButton_7.setChecked(True)
        self.ui.radioButton_15.setChecked(True)
        self.ui.radioButton_18.setChecked(True)
        self.ui.radioButton_24.setChecked(True)
        self.ana_mod()

    def enb_gg1(self):
##        self.ui.radioButton.setEnabled(True)
##        self.ui.radioButton_.setDisabled(True)
        self.ui.radioButton_2.setEnabled(True)
        self.ui.radioButton_3.setEnabled(True)
        self.ui.radioButton_4.setEnabled(True)
        self.ui.radioButton_5.setEnabled(True)
        self.ui.radioButton_6.setEnabled(True)

    def enb_g1(self):
        self.ui.radioButton.setChecked(True)
##        self.ui.radioButton_.setDisabled(True)
        self.ui.radioButton_2.setDisabled(True)
        self.ui.radioButton_3.setDisabled(True)
        self.ui.radioButton_4.setDisabled(True)
        self.ui.radioButton_5.setDisabled(True)
        self.ui.radioButton_6.setDisabled(True)

    def sscan(self):
        self.fi= QFileDialog.getOpenFileName(self, "Output map",".", "ESRI Shapefile (*.exe)")
	self.ui.lineEdit_4.setText(str(self.fi))		

    def ana_mod(self):
        if self.ui.radioButton_2.isChecked() or self.ui.radioButton_5.isChecked():
            self.ui.radioButton_9.setDisabled(True)
            self.ui.radioButton_14.setDisabled(True)
        if self.ui.radioButton_3.isChecked()or self.ui.radioButton_6.isChecked():
            self.ui.radioButton_14.setDisabled(True)
        if self.ui.radioButton.isChecked():
            self.ui.radioButton_9.setDisabled(True)
        if self.ui.radioButton_4.isChecked():
            self.ui.radioButton_8.setDisabled(True)
            self.ui.radioButton_9.setDisabled(True)
            self.ui.radioButton_10.setDisabled(True)
            self.ui.radioButton_11.setDisabled(True)
            self.ui.radioButton_12.setDisabled(True)
            self.ui.radioButton_13.setDisabled(True)
            self.ui.radioButton_14.setDisabled(True)            

    def enb_g2(self):
        self.ui.radioButton_7.setEnabled(True)
        self.ui.radioButton_8.setEnabled(True)
        self.ui.radioButton_9.setEnabled(True)
        self.ui.radioButton_10.setEnabled(True)
        self.ui.radioButton_11.setEnabled(True)
        self.ui.radioButton_12.setEnabled(True)
        self.ui.radioButton_13.setEnabled(True)
        self.ui.radioButton_7.setChecked(True)
        self.ana_mod()
        
      
    def b_param(self):
        if self.ui.radioButton.isChecked():
            self.var=1
        elif self.ui.radioButton_2.isChecked():
            self.var=2
        elif self.ui.radioButton_3.isChecked():
            self.var=3
        elif self.ui.radioButton_4.isChecked():
            self.var=5
        elif self.ui.radioButton_5.isChecked():
            self.var=6
        elif self.ui.radioButton_6.isChecked():
            self.var=4
            
        if self.ui.radioButton_7.isChecked():
            self.var1=0
        elif self.ui.radioButton_8.isChecked():
            self.var1=1
        elif self.ui.radioButton_9.isChecked():
            self.var1=2
        elif self.ui.radioButton_10.isChecked():
            self.var1=7
        elif self.ui.radioButton_11.isChecked():
            self.var1=3
        elif self.ui.radioButton_12.isChecked():
            self.var1=4        
        elif self.ui.radioButton_13.isChecked():
            self.var1=5
        elif self.ui.radioButton_14.isChecked():
            self.var1=6
				
	if self.ui.radioButton_15.isChecked():
            self.var2=1
        elif self.ui.radioButton_16.isChecked():
            self.var2=2
        elif self.ui.radioButton_17.isChecked():
            self.var2=3
            
        if self.ui.radioButton_21.isChecked():
            self.var3=0
        elif self.ui.radioButton_22.isChecked():
            self.var3=2
        elif self.ui.radioButton_23.isChecked():
            self.var3=4
        elif self.ui.radioButton_24.isChecked():
            self.var3=2
        elif self.ui.radioButton_25.isChecked():
            self.var3=3
            
        if self.ui.radioButton_18.isChecked():
            self.var4=1
        elif self.ui.radioButton_19.isChecked():
            self.var4=2
        elif self.ui.radioButton_20.isChecked():
            self.var4=3

        self.line=self.ui.lineEdit.text()
        self.line1=self.ui.lineEdit_2.text()
        self.line2=self.ui.lineEdit_3.text()
