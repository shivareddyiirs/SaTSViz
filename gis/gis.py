# -*- coding: utf-8 -*-
"""
/***************************************************************************
 gis
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
# Import the PyQt and QGIS libraries
import os
import urllib
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import qgis.utils

from ui_ff import Ui_ff
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from gisdialog import *
from ffdialog import *
from jjdialog import *
from parameter_file import *
import os.path

class gis:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
##        raise Exception(self.plugin_dir)
		# initialize locale
        localePath = ""
        locale = QSettings().value("locale/userLocale").toString()[0:2]

        if QFileInfo(self.plugin_dir).exists():
            localePath = self.plugin_dir + "/i18n/gis_" + locale + ".qm"

        if QFileInfo(localePath).exists():
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        #initialize progress bar
##        self.barr=Ui_jj()
##        self.barr.setupUi(self)
##        
        # Create the dialog (after translation) and keep reference
        self.dlg = gisDialog()
	self.dlgf=ffDialog()
	self.dlgj=jjDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/gis/icon.png"),u"SaTSViz", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&SaTSViz", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&SaTSViz", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
	QObject.connect(self.dlg.ui.buttonBox, SIGNAL("helpRequested()"), self.show_help)
##	self.dlg.ui.webView.setUrl(QUrl("file:///%s/help.html" % self.plugin_builder_dir))
        # show the dialog
        self.dlg.show()
	# Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            # creating case file ,control file ,geo file and population file
            self.dlg.apple()
            #show the dailog
            self.dlgf.show()
            #run the dialog event loop
            f_result=self.dlgf.exec_()
            # see if ok is pressed
            if f_result == 1:
                # b_param tell us which model we are using and there option
                self.dlgj.show()
                self.dlgj.ui.progressBar.setValue(0)
                self.dlgf.b_param()
                self.dlgj.ui.progressBar.setValue(40)
                # creating parameter file and calling setscanbatch.exe then create the output shape file 
                lis=fill_params(str(self.dlg.file),str(self.dlgf.var3),str(self.dlgf.line1),str(self.dlgf.line2),str(self.dlgf.var),str(self.dlgf.var1),str(self.dlgf.var2),str(self.dlgf.var4),str(self.dlgf.line),str(self.dlgf.fi))
                self.dlgj.ui.progressBar.setValue(60)
##                self.dlgj.ui.progressBar.setRange(0,100)
                call(lis[0],lis[1],lis[2])
                self.dlgj.ui.progressBar.setValue(80)
                make_shape(lis[3],lis[4])
                self.dlgj.ui.progressBar.setValue(100)
                # this call show the output shape file on the mapcanvas of qgis
                qgis.utils.iface.addVectorLayer(lis[5],lis[6],'ogr')  
                self.dlgj.exec_()
                self.dlgj.close()
                pass
            pass
        else:
            qgis.utils.reloadPlugin('gis')


    def show_help(self):
        help_file = "file:///" + self.plugin_dir + "/help/source/index.html"
	
        QDesktopServices.openUrl(QUrl(help_file))
