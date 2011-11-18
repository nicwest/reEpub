# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri Nov 18 19:22:35 2011
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(354, 168)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAcceptDrops(True)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "reEpub", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/logo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAcceptDrops(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelIntro = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelIntro.sizePolicy().hasHeightForWidth())
        self.labelIntro.setSizePolicy(sizePolicy)
        self.labelIntro.setAcceptDrops(False)
        self.labelIntro.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelIntro.setText(QtGui.QApplication.translate("MainWindow", "Drag folders here to reEpub them", None, QtGui.QApplication.UnicodeUTF8))
        self.labelIntro.setAlignment(QtCore.Qt.AlignCenter)
        self.labelIntro.setObjectName(_fromUtf8("labelIntro"))
        self.verticalLayout.addWidget(self.labelIntro)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText(QtGui.QApplication.translate("MainWindow", "existing files:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.radioButtonOverwrite = QtGui.QRadioButton(self.centralwidget)
        self.radioButtonOverwrite.setAcceptDrops(True)
        self.radioButtonOverwrite.setText(QtGui.QApplication.translate("MainWindow", "Overwrite", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonOverwrite.setObjectName(_fromUtf8("radioButtonOverwrite"))
        self.horizontalLayout.addWidget(self.radioButtonOverwrite)
        self.radioButtonArchive = QtGui.QRadioButton(self.centralwidget)
        self.radioButtonArchive.setText(QtGui.QApplication.translate("MainWindow", "Archive", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonArchive.setChecked(True)
        self.radioButtonArchive.setObjectName(_fromUtf8("radioButtonArchive"))
        self.horizontalLayout.addWidget(self.radioButtonArchive)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.progressBarRunning = QtGui.QProgressBar(self.centralwidget)
        self.progressBarRunning.setEnabled(True)
        self.progressBarRunning.setProperty("value", 0)
        self.progressBarRunning.setTextVisible(True)
        self.progressBarRunning.setObjectName(_fromUtf8("progressBarRunning"))
        self.verticalLayout.addWidget(self.progressBarRunning)
        self.labelProgress = QtGui.QLabel(self.centralwidget)
        self.labelProgress.setEnabled(False)
        self.labelProgress.setText(QtGui.QApplication.translate("MainWindow", "moo", None, QtGui.QApplication.UnicodeUTF8))
        self.labelProgress.setObjectName(_fromUtf8("labelProgress"))
        self.verticalLayout.addWidget(self.labelProgress)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

import res_rc
