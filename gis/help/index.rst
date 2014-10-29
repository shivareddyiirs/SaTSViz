.. evolve documentation master file, created by
   sphinx-quickstart on Sat Jul 27 00:38:38 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

SaTSViz
==================================

.. toctree::
   :maxdepth: 2
   

About SaTSViz
=================   
As of now QGIS has not been incorporated with any analysis tools.
This plugin aims to provide QGIS an additional feature of analysis by utilising SaTScan.
All input files needed for SaTScan are created by the plugin and the output files from it are read by the plugin
and fed in to QGIS to visualise the analysis results.
The plugin provides benefit to both the software – an analysis tools for QGIS and a way to visualize the results given out by SaTScan.

Pre-requisite
==========================
Before using SaTSViz, the user is required to install SaTScan on the system. SaTScan can be downloaded, for free, from http://www.satscan.org/

Files
=================

Input files
-------------------

The plugin takes a shapefile file, specifically and preferably a point shapefile, which has the coordinates in Lat/Long form, as input.

After filing in the required fields in the LOCATION ID, CASE, CONTROL, POPULATION and DATE (these are chosen from the field names in the shapefile), plugin produces four files:

* .cas file (CASE file) - This file contains two columns, one has the Location ID of all the points in the file and second has the values of the field selected as case.
* .pop file (POPULATION file) - This file contains two columns, one has the Location ID of all the points in the file and second has the values of the field selected as population.
* .ctl file (CONTROL file)-This file contains two columns, one has the Location ID of all the points in the file and second has the values of the field selected as control.
* .geo file (COORDINATES file)-This file contains the coordinates of all the points in the shapefile

These files are the inputs for SaTScan. 
All the files may not be used by SaTScan; Depending upon the analysis model, selected by the user, few or all of the files can be used by SaTScan.

.. note::
	User is requested to go through the SaTScan user manual (provided with the plugin), before using AVP, to get familiar with functioning, input and output of the plugin.

Intermediate Result
------------------------

SaTScan, in addition to the files mentioned above, needs one more file, PARAMETER file which has all the parameter values that SaTScan will use for analysis.
The user chooses the type of analysis, probability model to be used etc. by clicking on the radio buttons present in the plugin. 
After this the plugin produces the parameter file (.prm file).	

Output
---------------------

The plugin calls SaTScan and gives all the above files as input.
After analysis, three files are created by SaTScan:

* .gis file(Location Information file) - This file is created describing the various clusters in a way that is easy to incorporate into a geographical information system (GIS).  
* .col file (Cluster Information file)-This file contains, for each cluster, information about the location and size of the cluster, its log likelihood ratio and the p-value.
* .out.txt file-This file contains the full report of the analysis. All the results of the analysis are written by SaTScan into this file.

.gis file and .col file is read by the plugin and required fields are taken and are converted to two shapefiles:

* filename_cluster.shp 
* filename_col_cluster.shp 

Description of these two files is provided in coming sections.

The GUI
==================

The consists of two main dialogs. 
The first dialog asks the user to enter the input (path of the shapefile to be analysed)and choose the fields of the shapefile, which they want to use for making the input files (.cas, .pop, .ctl).

.. image:: Untitled1.png

After clicking OK on the dialog box, another dialog opens that asks the user to choose the type of analysis, probability model, time aggregation etc.
It also asks the user to browse and specify the path of SaTScanBatch.exe, which is the SaTScan executable file, for analysing the input file.

.. image:: Untitled.png

After clicking OK on it, intermediate files are formed and SaTScan opens command prompt for analysis. 

.. image:: Untitled2.png

After that, a window to choose Coordinate Reference System  appears in QGIS.  
Click OK on this window.

.. image:: Untitled3.png

On clicking OK, the results (points in the clusters formed by SaTScan) are displayed in QGIS.

.. image:: Untitled4.png

Core Functions
==================

There are four core functions that work behind the plugin:

* final_function()
* parameter_file ()
* call_sat()
* make_shape()

final_function()
--------------------

This function takes path of the shapefile to be analysed, expects user to specify the fields that are to be used to make case, control, population files and gives .cas, .ctl, .pop, .geo files as output.

parameter_file()
-----------------------

This function takes the values chosen by the user, in the second dialog box, as arguments and creates a  .prm file, which will be used by SaTScan for analysis.

call_sat()
----------------------

This function takes the path of the parameter file and SaTScanBatch.exe and calls SaTScan to start the analysis.

make_shape()
------------------------

After the analysis is done and output files are created by SaTScan, this function reads the .gis, .col, .geo files. It makes two shape files and its supporting files :

* filename_cluster.shp -  This shape file displays the clusters formed and all the points that come in the clusters formed.
* filename_col_cluster.shp-This shape file displays the cluster centres of all the clusters formed. This file is not automatically called by the plugin but can be manually displayed by the user by using the add vector layer option from QGIS user interface. This file is created in the same folder as the input shapefile.
