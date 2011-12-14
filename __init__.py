"""
/***************************************************************************
 VectorTransparency
                                 A QGIS plugin
 Update transparency of vector symbols in batch mode
                             -------------------
        begin                : 2011-12-12
        copyright            : (C) 2011 by Tim Sutton, Linfiniti Consulting CC.
        email                : tim@linfiniti.com
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
    return "Vector Transparency Manager"
def description():
    return "Update transparency of vector symbols in batch mode"
def version():
    return "Version 0.4"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.7"
def classFactory(iface):
    # load VectorTransparency class from file VectorTransparency
    from vectortransparency import VectorTransparency
    return VectorTransparency(iface)
