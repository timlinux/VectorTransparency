# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_vectortransparency.ui'
#
# Created: Tue Dec 13 14:31:41 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_VectorTransparency(object):
    def setupUi(self, VectorTransparency):
        VectorTransparency.setObjectName(_fromUtf8("VectorTransparency"))
        VectorTransparency.resize(387, 220)
        VectorTransparency.setWindowTitle(QtGui.QApplication.translate("VectorTransparency", "Vector Transparency", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VectorTransparency.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(VectorTransparency)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(VectorTransparency)
        self.label.setText(QtGui.QApplication.translate("VectorTransparency", "Select vector layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(VectorTransparency)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(VectorTransparency)
        self.label_2.setText(QtGui.QApplication.translate("VectorTransparency", "Transparency level (affects all symbols in layer)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(VectorTransparency)
        self.label_3.setText(QtGui.QApplication.translate("VectorTransparency", "Transparent", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.horizontalSlider = QtGui.QSlider(VectorTransparency)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setProperty("value", 100)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.spinBox = QtGui.QSpinBox(VectorTransparency)
        self.spinBox.setMaximum(100)
        self.spinBox.setProperty("value", 100)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout.addWidget(self.spinBox)
        self.label_4 = QtGui.QLabel(VectorTransparency)
        self.label_4.setText(QtGui.QApplication.translate("VectorTransparency", "Opaque", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(VectorTransparency)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 1)

        self.retranslateUi(VectorTransparency)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), VectorTransparency.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), VectorTransparency.reject)
        QtCore.QObject.connect(self.spinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.horizontalSlider.setValue)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.spinBox.setValue)
        QtCore.QMetaObject.connectSlotsByName(VectorTransparency)

    def retranslateUi(self, VectorTransparency):
        pass

