# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Project\TestSeq-Oppo\UI\automation.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_automation(object):
    def setupUi(self, automation):
        automation.setObjectName("automation")
        automation.resize(2128, 1173)
        self.gridLayout_3 = QtWidgets.QGridLayout(automation)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lb_title = QtWidgets.QLabel(automation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_title.sizePolicy().hasHeightForWidth())
        self.lb_title.setSizePolicy(sizePolicy)
        self.lb_title.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lb_title.setFont(font)
        self.lb_title.setObjectName("lb_title")
        self.gridLayout_3.addWidget(self.lb_title, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(automation)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame1 = QtWidgets.QFrame(self.tab)
        self.frame1.setObjectName("frame1")
        self.gridLayout = QtWidgets.QGridLayout(self.frame1)
        self.gridLayout.setObjectName("gridLayout")
        self.lb_axis = QtWidgets.QLabel(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_axis.sizePolicy().hasHeightForWidth())
        self.lb_axis.setSizePolicy(sizePolicy)
        self.lb_axis.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lb_axis.setFont(font)
        self.lb_axis.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lb_axis.setObjectName("lb_axis")
        self.gridLayout.addWidget(self.lb_axis, 0, 0, 1, 1)
        self.cb_axis = QtWidgets.QComboBox(self.frame1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cb_axis.setFont(font)
        self.cb_axis.setMaxVisibleItems(10)
        self.cb_axis.setObjectName("cb_axis")
        self.cb_axis.addItem("")
        self.cb_axis.addItem("")
        self.cb_axis.addItem("")
        self.gridLayout.addWidget(self.cb_axis, 0, 1, 1, 1)
        self.lb_rtp = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lb_rtp.setFont(font)
        self.lb_rtp.setObjectName("lb_rtp")
        self.gridLayout.addWidget(self.lb_rtp, 1, 0, 1, 1)
        self.pb_jog1 = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_jog1.sizePolicy().hasHeightForWidth())
        self.pb_jog1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pb_jog1.setFont(font)
        self.pb_jog1.setObjectName("pb_jog1")
        self.gridLayout.addWidget(self.pb_jog1, 1, 2, 1, 1)
        self.lb_rts = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lb_rts.setFont(font)
        self.lb_rts.setObjectName("lb_rts")
        self.gridLayout.addWidget(self.lb_rts, 2, 0, 1, 1)
        self.dsb_rts = QtWidgets.QDoubleSpinBox(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dsb_rts.sizePolicy().hasHeightForWidth())
        self.dsb_rts.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.dsb_rts.setFont(font)
        self.dsb_rts.setReadOnly(True)
        self.dsb_rts.setMaximum(10000.0)
        self.dsb_rts.setObjectName("dsb_rts")
        self.gridLayout.addWidget(self.dsb_rts, 2, 1, 1, 1)
        self.pb_jog2 = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_jog2.sizePolicy().hasHeightForWidth())
        self.pb_jog2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pb_jog2.setFont(font)
        self.pb_jog2.setObjectName("pb_jog2")
        self.gridLayout.addWidget(self.pb_jog2, 2, 2, 1, 1)
        self.lb_manuals = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lb_manuals.setFont(font)
        self.lb_manuals.setObjectName("lb_manuals")
        self.gridLayout.addWidget(self.lb_manuals, 3, 0, 1, 1)
        self.dsb_manuals = QtWidgets.QDoubleSpinBox(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dsb_manuals.sizePolicy().hasHeightForWidth())
        self.dsb_manuals.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.dsb_manuals.setFont(font)
        self.dsb_manuals.setReadOnly(True)
        self.dsb_manuals.setMaximum(10000.0)
        self.dsb_manuals.setObjectName("dsb_manuals")
        self.gridLayout.addWidget(self.dsb_manuals, 3, 1, 1, 1)
        self.pb_reset = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_reset.sizePolicy().hasHeightForWidth())
        self.pb_reset.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pb_reset.setFont(font)
        self.pb_reset.setObjectName("pb_reset")
        self.gridLayout.addWidget(self.pb_reset, 3, 2, 1, 1)
        self.lb_autos = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lb_autos.setFont(font)
        self.lb_autos.setObjectName("lb_autos")
        self.gridLayout.addWidget(self.lb_autos, 4, 0, 1, 1)
        self.dsb_autos = QtWidgets.QDoubleSpinBox(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dsb_autos.sizePolicy().hasHeightForWidth())
        self.dsb_autos.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.dsb_autos.setFont(font)
        self.dsb_autos.setReadOnly(True)
        self.dsb_autos.setMaximum(10000.0)
        self.dsb_autos.setObjectName("dsb_autos")
        self.gridLayout.addWidget(self.dsb_autos, 4, 1, 1, 1)
        self.pb_axis_stop = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_axis_stop.sizePolicy().hasHeightForWidth())
        self.pb_axis_stop.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pb_axis_stop.setFont(font)
        self.pb_axis_stop.setObjectName("pb_axis_stop")
        self.gridLayout.addWidget(self.pb_axis_stop, 4, 2, 1, 1)
        self.lb_limit1 = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lb_limit1.setFont(font)
        self.lb_limit1.setObjectName("lb_limit1")
        self.gridLayout.addWidget(self.lb_limit1, 5, 0, 1, 1)
        self.dsb_limit1 = QtWidgets.QDoubleSpinBox(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dsb_limit1.sizePolicy().hasHeightForWidth())
        self.dsb_limit1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.dsb_limit1.setFont(font)
        self.dsb_limit1.setReadOnly(True)
        self.dsb_limit1.setMaximum(10000.0)
        self.dsb_limit1.setObjectName("dsb_limit1")
        self.gridLayout.addWidget(self.dsb_limit1, 5, 1, 1, 1)
        self.lb_limit2 = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lb_limit2.setFont(font)
        self.lb_limit2.setObjectName("lb_limit2")
        self.gridLayout.addWidget(self.lb_limit2, 6, 0, 1, 1)
        self.dsb_limit2 = QtWidgets.QDoubleSpinBox(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dsb_limit2.sizePolicy().hasHeightForWidth())
        self.dsb_limit2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.dsb_limit2.setFont(font)
        self.dsb_limit2.setReadOnly(True)
        self.dsb_limit2.setMaximum(10000.0)
        self.dsb_limit2.setObjectName("dsb_limit2")
        self.gridLayout.addWidget(self.dsb_limit2, 6, 1, 1, 1)
        self.pb_axis_save = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_axis_save.sizePolicy().hasHeightForWidth())
        self.pb_axis_save.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pb_axis_save.setFont(font)
        self.pb_axis_save.setObjectName("pb_axis_save")
        self.gridLayout.addWidget(self.pb_axis_save, 6, 2, 1, 1)
        self.cb_zero = QtWidgets.QCheckBox(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_zero.sizePolicy().hasHeightForWidth())
        self.cb_zero.setSizePolicy(sizePolicy)
        self.cb_zero.setObjectName("cb_zero")
        self.gridLayout.addWidget(self.cb_zero, 7, 0, 1, 1)
        self.cb_limit1 = QtWidgets.QCheckBox(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_limit1.sizePolicy().hasHeightForWidth())
        self.cb_limit1.setSizePolicy(sizePolicy)
        self.cb_limit1.setObjectName("cb_limit1")
        self.gridLayout.addWidget(self.cb_limit1, 7, 1, 1, 1)
        self.cb_limit2 = QtWidgets.QCheckBox(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_limit2.sizePolicy().hasHeightForWidth())
        self.cb_limit2.setSizePolicy(sizePolicy)
        self.cb_limit2.setObjectName("cb_limit2")
        self.gridLayout.addWidget(self.cb_limit2, 7, 2, 1, 1)
        self.dsb_rtp = QtWidgets.QDoubleSpinBox(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dsb_rtp.sizePolicy().hasHeightForWidth())
        self.dsb_rtp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.dsb_rtp.setFont(font)
        self.dsb_rtp.setReadOnly(True)
        self.dsb_rtp.setMaximum(10000.0)
        self.dsb_rtp.setObjectName("dsb_rtp")
        self.gridLayout.addWidget(self.dsb_rtp, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame1, 0, 0, 1, 1)
        self.frame2 = QtWidgets.QFrame(self.tab)
        self.frame2.setObjectName("frame2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pb_dutout = QtWidgets.QPushButton(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_dutout.sizePolicy().hasHeightForWidth())
        self.pb_dutout.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pb_dutout.setFont(font)
        self.pb_dutout.setObjectName("pb_dutout")
        self.gridLayout_2.addWidget(self.pb_dutout, 4, 1, 1, 1)
        self.pb_initp = QtWidgets.QPushButton(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_initp.sizePolicy().hasHeightForWidth())
        self.pb_initp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pb_initp.setFont(font)
        self.pb_initp.setObjectName("pb_initp")
        self.gridLayout_2.addWidget(self.pb_initp, 5, 0, 1, 1)
        self.pb_pressp = QtWidgets.QPushButton(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_pressp.sizePolicy().hasHeightForWidth())
        self.pb_pressp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pb_pressp.setFont(font)
        self.pb_pressp.setObjectName("pb_pressp")
        self.gridLayout_2.addWidget(self.pb_pressp, 5, 1, 1, 1)
        self.pb_loop = QtWidgets.QPushButton(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_loop.sizePolicy().hasHeightForWidth())
        self.pb_loop.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pb_loop.setFont(font)
        self.pb_loop.setObjectName("pb_loop")
        self.gridLayout_2.addWidget(self.pb_loop, 6, 1, 1, 1)
        self.pb_loopstop = QtWidgets.QPushButton(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_loopstop.sizePolicy().hasHeightForWidth())
        self.pb_loopstop.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pb_loopstop.setFont(font)
        self.pb_loopstop.setObjectName("pb_loopstop")
        self.gridLayout_2.addWidget(self.pb_loopstop, 7, 0, 1, 1)
        self.pb_clear = QtWidgets.QPushButton(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_clear.sizePolicy().hasHeightForWidth())
        self.pb_clear.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pb_clear.setFont(font)
        self.pb_clear.setObjectName("pb_clear")
        self.gridLayout_2.addWidget(self.pb_clear, 7, 1, 1, 1)
        self.pb_cyair1 = QtWidgets.QPushButton(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_cyair1.sizePolicy().hasHeightForWidth())
        self.pb_cyair1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pb_cyair1.setFont(font)
        self.pb_cyair1.setObjectName("pb_cyair1")
        self.gridLayout_2.addWidget(self.pb_cyair1, 0, 1, 1, 1)
        self.pb_cyout = QtWidgets.QPushButton(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_cyout.sizePolicy().hasHeightForWidth())
        self.pb_cyout.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pb_cyout.setFont(font)
        self.pb_cyout.setObjectName("pb_cyout")
        self.gridLayout_2.addWidget(self.pb_cyout, 2, 0, 1, 1)
        self.pb_cyair2 = QtWidgets.QPushButton(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_cyair2.sizePolicy().hasHeightForWidth())
        self.pb_cyair2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pb_cyair2.setFont(font)
        self.pb_cyair2.setObjectName("pb_cyair2")
        self.gridLayout_2.addWidget(self.pb_cyair2, 2, 1, 1, 1)
        self.pb_cypress = QtWidgets.QPushButton(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_cypress.sizePolicy().hasHeightForWidth())
        self.pb_cypress.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pb_cypress.setFont(font)
        self.pb_cypress.setObjectName("pb_cypress")
        self.gridLayout_2.addWidget(self.pb_cypress, 3, 0, 1, 1)
        self.pb_cyin = QtWidgets.QPushButton(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_cyin.sizePolicy().hasHeightForWidth())
        self.pb_cyin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pb_cyin.setFont(font)
        self.pb_cyin.setObjectName("pb_cyin")
        self.gridLayout_2.addWidget(self.pb_cyin, 0, 0, 1, 1)
        self.pb_single = QtWidgets.QPushButton(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_single.sizePolicy().hasHeightForWidth())
        self.pb_single.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pb_single.setFont(font)
        self.pb_single.setObjectName("pb_single")
        self.gridLayout_2.addWidget(self.pb_single, 6, 0, 1, 1)
        self.pb_dutin = QtWidgets.QPushButton(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_dutin.sizePolicy().hasHeightForWidth())
        self.pb_dutin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pb_dutin.setFont(font)
        self.pb_dutin.setObjectName("pb_dutin")
        self.gridLayout_2.addWidget(self.pb_dutin, 4, 0, 1, 1)
        self.pb_cyrelease = QtWidgets.QPushButton(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_cyrelease.sizePolicy().hasHeightForWidth())
        self.pb_cyrelease.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pb_cyrelease.setFont(font)
        self.pb_cyrelease.setObjectName("pb_cyrelease")
        self.gridLayout_2.addWidget(self.pb_cyrelease, 3, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame2, 0, 2, 1, 1)
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.cb_yellow = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_yellow.setFont(font)
        self.cb_yellow.setObjectName("cb_yellow")
        self.gridLayout_6.addWidget(self.cb_yellow, 2, 0, 1, 1)
        self.cb_stop = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_stop.setFont(font)
        self.cb_stop.setObjectName("cb_stop")
        self.gridLayout_6.addWidget(self.cb_stop, 2, 1, 1, 1)
        self.cb_green = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_green.setFont(font)
        self.cb_green.setObjectName("cb_green")
        self.gridLayout_6.addWidget(self.cb_green, 3, 0, 1, 1)
        self.cb_reset = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_reset.setFont(font)
        self.cb_reset.setObjectName("cb_reset")
        self.gridLayout_6.addWidget(self.cb_reset, 3, 1, 1, 1)
        self.cb_buzz = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_buzz.setFont(font)
        self.cb_buzz.setObjectName("cb_buzz")
        self.gridLayout_6.addWidget(self.cb_buzz, 4, 0, 1, 1)
        self.cb_pass = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_pass.setFont(font)
        self.cb_pass.setObjectName("cb_pass")
        self.gridLayout_6.addWidget(self.cb_pass, 4, 1, 1, 1)
        self.cb_fail = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_fail.setFont(font)
        self.cb_fail.setObjectName("cb_fail")
        self.gridLayout_6.addWidget(self.cb_fail, 5, 0, 1, 1)
        self.cb_light = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_light.setFont(font)
        self.cb_light.setObjectName("cb_light")
        self.gridLayout_6.addWidget(self.cb_light, 5, 1, 1, 1)
        self.cb_daq = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_daq.setFont(font)
        self.cb_daq.setObjectName("cb_daq")
        self.gridLayout_6.addWidget(self.cb_daq, 6, 0, 1, 1)
        self.cb_red = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_red.setFont(font)
        self.cb_red.setObjectName("cb_red")
        self.gridLayout_6.addWidget(self.cb_red, 1, 0, 1, 1)
        self.cb_start = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_start.setFont(font)
        self.cb_start.setObjectName("cb_start")
        self.gridLayout_6.addWidget(self.cb_start, 1, 1, 1, 1)
        self.cb_manual = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_manual.setFont(font)
        self.cb_manual.setObjectName("cb_manual")
        self.gridLayout_6.addWidget(self.cb_manual, 0, 0, 1, 1)
        self.cb_door = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_door.setFont(font)
        self.cb_door.setObjectName("cb_door")
        self.gridLayout_6.addWidget(self.cb_door, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 0, 3, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lb_para1 = QtWidgets.QLabel(self.tab_2)
        self.lb_para1.setObjectName("lb_para1")
        self.gridLayout_5.addWidget(self.lb_para1, 0, 0, 1, 1)
        self.pb_save1 = QtWidgets.QPushButton(self.tab_2)
        self.pb_save1.setObjectName("pb_save1")
        self.gridLayout_5.addWidget(self.pb_save1, 0, 1, 1, 1)
        self.lb_para2 = QtWidgets.QLabel(self.tab_2)
        self.lb_para2.setObjectName("lb_para2")
        self.gridLayout_5.addWidget(self.lb_para2, 0, 2, 1, 1)
        self.pb_save2 = QtWidgets.QPushButton(self.tab_2)
        self.pb_save2.setObjectName("pb_save2")
        self.gridLayout_5.addWidget(self.pb_save2, 0, 3, 1, 1)
        self.lb_para3 = QtWidgets.QLabel(self.tab_2)
        self.lb_para3.setObjectName("lb_para3")
        self.gridLayout_5.addWidget(self.lb_para3, 0, 4, 1, 1)
        self.pb_save3 = QtWidgets.QPushButton(self.tab_2)
        self.pb_save3.setObjectName("pb_save3")
        self.gridLayout_5.addWidget(self.pb_save3, 0, 5, 1, 1)
        self.tw_para1 = QtWidgets.QTableWidget(self.tab_2)
        self.tw_para1.setObjectName("tw_para1")
        self.tw_para1.setColumnCount(0)
        self.tw_para1.setRowCount(0)
        self.gridLayout_5.addWidget(self.tw_para1, 1, 0, 1, 2)
        self.tw_para2 = QtWidgets.QTableWidget(self.tab_2)
        self.tw_para2.setObjectName("tw_para2")
        self.tw_para2.setColumnCount(0)
        self.tw_para2.setRowCount(0)
        self.gridLayout_5.addWidget(self.tw_para2, 1, 2, 1, 2)
        self.tw_para3 = QtWidgets.QTableWidget(self.tab_2)
        self.tw_para3.setObjectName("tw_para3")
        self.tw_para3.setColumnCount(0)
        self.tw_para3.setRowCount(0)
        self.gridLayout_5.addWidget(self.tw_para3, 1, 4, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_3.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.retranslateUi(automation)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(automation)

    def retranslateUi(self, automation):
        _translate = QtCore.QCoreApplication.translate
        automation.setWindowTitle(_translate("automation", "Automation"))
        self.lb_title.setText(_translate("automation", "AutoMation"))
        self.lb_axis.setText(_translate("automation", "Axis Name："))
        self.cb_axis.setItemText(0, _translate("automation", "X轴"))
        self.cb_axis.setItemText(1, _translate("automation", "Y轴"))
        self.cb_axis.setItemText(2, _translate("automation", "Z轴"))
        self.lb_rtp.setText(_translate("automation", "实时位置:"))
        self.pb_jog1.setText(_translate("automation", "Jog+"))
        self.lb_rts.setText(_translate("automation", "实时速度:"))
        self.pb_jog2.setText(_translate("automation", "Jog-"))
        self.lb_manuals.setText(_translate("automation", "手动速度:"))
        self.pb_reset.setText(_translate("automation", "Reset"))
        self.lb_autos.setText(_translate("automation", "自动速度:"))
        self.pb_axis_stop.setText(_translate("automation", "Stop"))
        self.lb_limit1.setText(_translate("automation", "正极限:"))
        self.lb_limit2.setText(_translate("automation", "负极限:"))
        self.pb_axis_save.setText(_translate("automation", "Save"))
        self.cb_zero.setText(_translate("automation", "Zero"))
        self.cb_limit1.setText(_translate("automation", "Limit+"))
        self.cb_limit2.setText(_translate("automation", "Limit-"))
        self.pb_dutout.setText(_translate("automation", "手动出料"))
        self.pb_initp.setText(_translate("automation", "Z初始位"))
        self.pb_pressp.setText(_translate("automation", "Z打键位"))
        self.pb_loop.setText(_translate("automation", "循环按压"))
        self.pb_loopstop.setText(_translate("automation", "循环停止"))
        self.pb_clear.setText(_translate("automation", "计数复位"))
        self.pb_cyair1.setText(_translate("automation", "吸真空-吸"))
        self.pb_cyout.setText(_translate("automation", "进出气缸-出"))
        self.pb_cyair2.setText(_translate("automation", "吸真空-松"))
        self.pb_cypress.setText(_translate("automation", "压料气缸-压"))
        self.pb_cyin.setText(_translate("automation", "进出气缸-进"))
        self.pb_single.setText(_translate("automation", "单次按压"))
        self.pb_dutin.setText(_translate("automation", "手动进料"))
        self.pb_cyrelease.setText(_translate("automation", "压料气缸-松"))
        self.cb_yellow.setText(_translate("automation", "黄灯"))
        self.cb_stop.setText(_translate("automation", "停止灯"))
        self.cb_green.setText(_translate("automation", "绿灯"))
        self.cb_reset.setText(_translate("automation", "复位灯"))
        self.cb_buzz.setText(_translate("automation", "蜂鸣器"))
        self.cb_pass.setText(_translate("automation", "Pass灯"))
        self.cb_fail.setText(_translate("automation", "Fail灯"))
        self.cb_light.setText(_translate("automation", "照明灯"))
        self.cb_daq.setText(_translate("automation", "DAQ触发"))
        self.cb_red.setText(_translate("automation", "红灯"))
        self.cb_start.setText(_translate("automation", "启动灯"))
        self.cb_manual.setText(_translate("automation", "手动模式"))
        self.cb_door.setText(_translate("automation", "屏蔽安全门"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("automation", "手动调试"))
        self.lb_para1.setText(_translate("automation", "轴参数："))
        self.pb_save1.setText(_translate("automation", "保存"))
        self.lb_para2.setText(_translate("automation", "按压参数："))
        self.pb_save2.setText(_translate("automation", "保存"))
        self.lb_para3.setText(_translate("automation", "坐标参数："))
        self.pb_save3.setText(_translate("automation", "保存"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("automation", "参数设置"))

