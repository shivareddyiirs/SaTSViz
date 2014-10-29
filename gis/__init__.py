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
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "SaTSViz"


def description():
    return "Plugin for analysis in QGIS with Visualization of result"


def version():
    return "Version 1.0"


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "1.8"

def author():
    return "Jolly Singh and Jagandeep Singh"

def email():
    return "jolly.nitgoa@gmail.com"

def classFactory(iface):
    # load gis class from file gis
    from gis import gis
    return gis(iface)
