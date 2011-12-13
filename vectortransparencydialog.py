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
import sys 
sys.path.append("/home/timlinux/.eclipse/org.eclipse.platform_3.7.0_155965261/plugins/org.python.pydev.debug_2.2.4.2011110216/pysrc/")
from pydevd import *
# create the dialog for zoom to point
class VectorTransparencyDialog(QtGui.QDialog):
    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_VectorTransparency()
        self.ui.setupUi(self)
        self.getLayers()


    def getLayers(self):
        myLayers = []
        for i in range(len(self.iface.mapCanvas().layers())):
            myLayer = self.iface.mapCanvas().layer(i)
            if myLayer.type() == myLayer.VectorLayer:
                #if myLayer.geometryType() == QGis.Polygon:
                self.ui.comboBox.addItem(myLayer.name(),myLayer.id())
        return myLayers
    
    def accept(self):
        
        settrace()
        if not len(self.iface.mapCanvas().layers()):
            self.close()
            return
        myLayer = QgsMapLayerRegistry.instance().mapLayer(self.ui.comboBox.itemData(self.ui.comboBox.currentIndex()).toString())
        myAlpha = float(self.ui.spinBox.value())  / 100.0
        if myLayer.isUsingRendererV2():
            # new symbology - subclass of QgsFeatureRendererV2 class
            myRenderer = myLayer.rendererV2()
            myType = myRenderer.type()
            if myType == "singleSymbol":
                mySymbol = myRenderer.symbol()
                mySymbol.setAlpha(myAlpha)
            elif myType == "categorizedSymbol":
                for myCategory in myRenderer.categories():
                    mySymbol = myCategory.symbol()
                    mySymbol.setAlpha(myAlpha)
            elif myType == "graduatedSymbol":
                for myRange in myRenderer.ranges():
                    mySymbol = myRange.symbol()
                    mySymbol.setAlpha(myAlpha)
            else:
                #type unknown
                pass
            
                
        else:
            # old symbology - subclass of QgsRenderer class
            myRenderer = myLayer.renderer()
        if hasattr(myLayer, "setCacheImage"): 
            myLayer.setCacheImage(None)
        myLayer.triggerRepaint()
        self.iface.mapCanvas().setDirty(True)
        self.iface.mapCanvas().refresh()
        self.close()
            