# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Project\TestSeq\UI\editsequence.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_editsequence(object):
    def setupUi(self, editsequence):
        editsequence.setObjectName("editsequence")
        editsequence.resize(1010, 621)
        self.gridLayout = QtWidgets.QGridLayout(editsequence)
        self.gridLayout.setObjectName("gridLayout")
        self.lb_edit = QtWidgets.QLabel(editsequence)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_edit.sizePolicy().hasHeightForWidth())
        self.lb_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lb_edit.setFont(font)
        self.lb_edit.setObjectName("lb_edit")
        self.gridLayout.addWidget(self.lb_edit, 0, 0, 1, 1)
        self.cb_seq = QtWidgets.QComboBox(editsequence)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_seq.sizePolicy().hasHeightForWidth())
        self.cb_seq.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cb_seq.setFont(font)
        self.cb_seq.setObjectName("cb_seq")
        self.cb_seq.addItem("")
        self.cb_seq.addItem("")
        self.gridLayout.addWidget(self.cb_seq, 0, 1, 1, 1)
        self.splitter = QtWidgets.QSplitter(editsequence)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pb_insertrow = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_insertrow.sizePolicy().hasHeightForWidth())
        self.pb_insertrow.setSizePolicy(sizePolicy)
        self.pb_insertrow.setObjectName("pb_insertrow")
        self.pb_delrow = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_delrow.sizePolicy().hasHeightForWidth())
        self.pb_delrow.setSizePolicy(sizePolicy)
        self.pb_delrow.setObjectName("pb_delrow")
        self.pb_saveseq = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_saveseq.sizePolicy().hasHeightForWidth())
        self.pb_saveseq.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pb_saveseq.setFont(font)
        self.pb_saveseq.setObjectName("pb_saveseq")
        self.gridLayout.addWidget(self.splitter, 0, 2, 1, 1)
        self.tableseq = QtWidgets.QTableWidget(editsequence)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableseq.sizePolicy().hasHeightForWidth())
        self.tableseq.setSizePolicy(sizePolicy)
        self.tableseq.setObjectName("tableseq")
        self.tableseq.setColumnCount(0)
        self.tableseq.setRowCount(0)
        self.gridLayout.addWidget(self.tableseq, 1, 0, 1, 3)

        self.retranslateUi(editsequence)
        QtCore.QMetaObject.connectSlotsByName(editsequence)

    def retranslateUi(self, editsequence):
        _translate = QtCore.QCoreApplication.translate
        editsequence.setWindowTitle(_translate("editsequence", "Edit Sequence"))
        self.lb_edit.setText(_translate("editsequence", "Edit Test Sequence"))
        self.cb_seq.setItemText(0, _translate("editsequence", "Sequence1"))
        self.cb_seq.setItemText(1, _translate("editsequence", "Sequence2"))
        self.pb_insertrow.setText(_translate("editsequence", "Insert Row"))
        self.pb_delrow.setText(_translate("editsequence", "Delete Row"))
        self.pb_saveseq.setText(_translate("editsequence", "Save"))
