# -*- coding: utf-8 -*-
"""
/***************************************************************************
 jjDialog
                                 A QGIS plugin
 jj
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
from ui_jj import Ui_jj
# create the dialog for zoom to point


class jjDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_jj()
        self.ui.setupUi(self)
