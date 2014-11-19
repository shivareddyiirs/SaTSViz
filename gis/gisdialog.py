# -*- coding: utf-8 -*-
"""
/***************************************************************************
 gisDialog
                                 A QGIS plugin
 abcd
                             -------------------
        begin                : 2013-06-20
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
from ui_gis import Ui_gis
from qgis.core import *
from qgis.gui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from shapefile import *
#import shapefile
from final_function import *
import qgis
# create the dialog for zoom to point


class gisDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
    	self.var=qgis.utils.iface.mapCanvas()
    	self.var1=self.var.layers()
    	self.file='\0'
        # Set up the user interface from Designer.
        self.ui = Ui_gis()
        self.ui.setupUi(self)
	self.first()
    	QObject.connect(self.ui.comboBox_6, SIGNAL("currentIndexChanged(QString)"),self.set_value)
    	QObject.connect(self.ui.toolButton, SIGNAL("clicked()"), self.outFile)

    def first(self):
        l=len(self.var1)
    	for i in range(l):
            self.ui.comboBox_6.addItem(str(self.var1[i].source()))
            self.set_value()
            	
    def outFile(self):
		self.outvLayer = QFileDialog.getOpenFileName(self,"Open File",".","ESRI Shapefile (*.shp)")
		if not self.outvLayer :
                    v=self.ui.comboBox_6.findText(self.outvLayer)
                    if v<0:
                        self.ui.comboBox_6.addItem(self.outvLayer)
                        #ind=self.ui.comboBox_6.currentIndex()+1
                        #self.ui.comboBox_6.setCurrentIndex(ind)
		            
    def set_value(self):
                self.allclear()
                self.file=self.ui.comboBox_6.currentText()
		self.sf=Reader(str(self.file))
		self.ui.comboBox.addItem('NONE')
		self.ui.comboBox_3.addItem('NONE')
		self.ui.comboBox_5.addItem('NONE')
		self.fields=self.sf.fields
		a=len(self.fields)
		a=a-1
		#self.apple()
		for i in range(a):
			i=i+1
                        self.ui.comboBox.addItem(self.fields[i][0])
			self.ui.comboBox_5.addItem(self.fields[i][0])
			self.ui.comboBox_2.addItem(self.fields[i][0])
			self.ui.comboBox_3.addItem(self.fields[i][0])
			self.ui.comboBox_4.addItem(self.fields[i][0])

    				
    def allclear(self):
		self.ui.comboBox_5.clear()
		self.ui.comboBox_2.clear()
		self.ui.comboBox_3.clear()
		self.ui.comboBox_4.clear()
		self.ui.comboBox.clear()
			

    def apple(self):
        status = reading(str(self.ui.comboBox_6.currentText()),str(self.ui.comboBox_4.currentText()),str(self.ui.comboBox_2.currentText()),"CASE",str(self.ui.comboBox.currentText()))
        if status == "noFile" :
            return "noFile"
        status = reading(str(self.ui.comboBox_6.currentText()),str(self.ui.comboBox_4.currentText()),str(self.ui.comboBox_3.currentText()),"CONTROL",str(self.ui.comboBox.currentText()))
        if status == "noFile" :
            return "noFile"
        status = reading(str(self.ui.comboBox_6.currentText()),str(self.ui.comboBox_4.currentText()),str(self.ui.comboBox_5.currentText()),"POPULATION",str(self.ui.comboBox.currentText()))
        if status == "noFile":
            return "noFile"
