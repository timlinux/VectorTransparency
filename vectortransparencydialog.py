"""
/***************************************************************************
 VectorTransparencyDialog
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
"""

from PyQt4 import QtCore, QtGui
from qgis.core import *
from qgis.gui import *
from ui_vectortransparency import Ui_VectorTransparency
# create the dialog for zoom to point
class VectorTransparencyDialog(QtGui.QDialog):
    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        import sys 
        sys.path.append("/home/timlinux/.eclipse/org.eclipse.platform_3.7.0_155965261/plugins/org.python.pydev.debug_2.2.4.2011110216/pysrc/")
        from pydevd import *
        settrace()
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_VectorTransparency()
        self.ui.setupUi(self)
        self.getLayers()


    def getLayers(self):
        layers = []
        for i in range(len(self.iface.mapCanvas().layers())):
            layer = self.iface.mapCanvas().layer(i)
            if layer.type() == layer.VectorLayer:
                #if layer.geometryType() == QGis.Polygon:
                self.ui.comboBox.insertItem(0,layer.name())
        return layers