# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Project\TestSeq-Amazon\UI\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2099, 1186)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1181, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lb_ia = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_ia.sizePolicy().hasHeightForWidth())
        self.lb_ia.setSizePolicy(sizePolicy)
        self.lb_ia.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(88, 160, 250, 200), stop:1 rgba(0, 0, 0, 0));\n"
"background-image: url(:/JPG/Res/IA.png);")
        self.lb_ia.setText("")
        self.lb_ia.setObjectName("lb_ia")
        self.gridLayout_7.addWidget(self.lb_ia, 1, 1, 1, 1)
        self.lb_title = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_title.sizePolicy().hasHeightForWidth())
        self.lb_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lb_title.setFont(font)
        self.lb_title.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(88, 160, 250, 200), stop:1 rgba(0, 0, 0, 0));\n"
"")
        self.lb_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_title.setObjectName("lb_title")
        self.gridLayout_7.addWidget(self.lb_title, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.groupstate = QtWidgets.QFrame(self.centralWidget)
        self.groupstate.setObjectName("groupstate")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupstate)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.tabWidget = QtWidgets.QTabWidget(self.groupstate)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.main = QtWidgets.QWidget()
        self.main.setObjectName("main")
        self.gridLayout = QtWidgets.QGridLayout(self.main)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.te_log = QtWidgets.QTextEdit(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.te_log.sizePolicy().hasHeightForWidth())
        self.te_log.setSizePolicy(sizePolicy)
        self.te_log.setObjectName("te_log")
        self.gridLayout.addWidget(self.te_log, 2, 0, 1, 4)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.testlist1 = QtWidgets.QTreeWidget(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testlist1.sizePolicy().hasHeightForWidth())
        self.testlist1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.testlist1.setFont(font)
        self.testlist1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.testlist1.setObjectName("testlist1")
        self.testlist1.headerItem().setText(0, "1")
        self.testlist1.header().setHighlightSections(True)
        self.gridLayout_6.addWidget(self.testlist1, 0, 0, 1, 1)
        self.pbar1 = QtWidgets.QProgressBar(self.main)
        self.pbar1.setProperty("value", 24)
        self.pbar1.setObjectName("pbar1")
        self.gridLayout_6.addWidget(self.pbar1, 1, 0, 1, 1)
        self.systeminfo1 = QtWidgets.QTableWidget(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.systeminfo1.sizePolicy().hasHeightForWidth())
        self.systeminfo1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.systeminfo1.setFont(font)
        self.systeminfo1.setStyleSheet("QTableWidget::item{\n"
"vertical-align: middle;\n"
"text-align: center;\n"
"}")
        self.systeminfo1.setProperty("showDropIndicator", False)
        self.systeminfo1.setObjectName("systeminfo1")
        self.systeminfo1.setColumnCount(0)
        self.systeminfo1.setRowCount(0)
        self.gridLayout_6.addWidget(self.systeminfo1, 0, 1, 1, 1)
        self.pb_snap = QtWidgets.QPushButton(self.main)
        self.pb_snap.setObjectName("pb_snap")
        self.gridLayout_6.addWidget(self.pb_snap, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_6, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lb_image = QtWidgets.QLabel(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_image.sizePolicy().hasHeightForWidth())
        self.lb_image.setSizePolicy(sizePolicy)
        self.lb_image.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lb_image.setText("")
        self.lb_image.setObjectName("lb_image")
        self.gridLayout_4.addWidget(self.lb_image, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 1, 2, 1, 1)
        self.lb_seq = QtWidgets.QLabel(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_seq.sizePolicy().hasHeightForWidth())
        self.lb_seq.setSizePolicy(sizePolicy)
        self.lb_seq.setObjectName("lb_seq")
        self.gridLayout.addWidget(self.lb_seq, 0, 0, 1, 1)
        self.lb_imagetitle = QtWidgets.QLabel(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_imagetitle.sizePolicy().hasHeightForWidth())
        self.lb_imagetitle.setSizePolicy(sizePolicy)
        self.lb_imagetitle.setObjectName("lb_imagetitle")
        self.gridLayout.addWidget(self.lb_imagetitle, 0, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(2, 2)
        self.tabWidget.addTab(self.main, "")
        self.log = QtWidgets.QWidget()
        self.log.setObjectName("log")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.log)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget.addTab(self.log, "")
        self.gridLayout_10.addWidget(self.tabWidget, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupstate, 1, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lb_user_title = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lb_user_title.setFont(font)
        self.lb_user_title.setStyleSheet("")
        self.lb_user_title.setObjectName("lb_user_title")
        self.gridLayout_5.addWidget(self.lb_user_title, 0, 1, 1, 1)
        self.lb_main_user = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lb_main_user.setFont(font)
        self.lb_main_user.setObjectName("lb_main_user")
        self.gridLayout_5.addWidget(self.lb_main_user, 0, 2, 1, 1)
        self.lb_ver = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_ver.sizePolicy().hasHeightForWidth())
        self.lb_ver.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lb_ver.setFont(font)
        self.lb_ver.setObjectName("lb_ver")
        self.gridLayout_5.addWidget(self.lb_ver, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_5, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 2099, 34))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuUser = QtWidgets.QMenu(self.menuBar)
        self.menuUser.setObjectName("menuUser")
        self.menuWindow = QtWidgets.QMenu(self.menuBar)
        self.menuWindow.setObjectName("menuWindow")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.toolBar.setFont(font)
        self.toolBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setStyleSheet("border-style: flat")
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(16, 16))
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionReload_CSV = QtWidgets.QAction(MainWindow)
        self.actionReload_CSV.setObjectName("actionReload_CSV")
        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.actionLoop_Test = QtWidgets.QAction(MainWindow)
        self.actionLoop_Test.setObjectName("actionLoop_Test")
        self.actionMain_Window = QtWidgets.QAction(MainWindow)
        self.actionMain_Window.setCheckable(False)
        self.actionMain_Window.setObjectName("actionMain_Window")
        self.actionEdit_Window = QtWidgets.QAction(MainWindow)
        self.actionEdit_Window.setObjectName("actionEdit_Window")
        self.actionZmq_Debug = QtWidgets.QAction(MainWindow)
        self.actionZmq_Debug.setObjectName("actionZmq_Debug")
        self.actionTcp_Debug = QtWidgets.QAction(MainWindow)
        self.actionTcp_Debug.setObjectName("actionTcp_Debug")
        self.actionSerial_Debug = QtWidgets.QAction(MainWindow)
        self.actionSerial_Debug.setObjectName("actionSerial_Debug")
        self.actionStart = QtWidgets.QAction(MainWindow)
        self.actionStart.setCheckable(False)
        self.actionStart.setEnabled(True)
        font = QtGui.QFont()
        self.actionStart.setFont(font)
        self.actionStart.setVisible(True)
        self.actionStart.setObjectName("actionStart")
        self.actionStop = QtWidgets.QAction(MainWindow)
        self.actionStop.setObjectName("actionStop")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        self.actionEdit.setFont(font)
        self.actionEdit.setObjectName("actionEdit")
        self.actionLoginTool = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        self.actionLoginTool.setFont(font)
        self.actionLoginTool.setObjectName("actionLoginTool")
        self.actionAutomation = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        self.actionAutomation.setFont(font)
        self.actionAutomation.setObjectName("actionAutomation")
        self.actionMainwindow = QtWidgets.QAction(MainWindow)
        self.actionMainwindow.setObjectName("actionMainwindow")
        self.actionPause = QtWidgets.QAction(MainWindow)
        self.actionPause.setObjectName("actionPause")
        self.actionContinue = QtWidgets.QAction(MainWindow)
        self.actionContinue.setObjectName("actionContinue")
        self.actionToolBar = QtWidgets.QAction(MainWindow)
        self.actionToolBar.setCheckable(True)
        self.actionToolBar.setChecked(True)
        self.actionToolBar.setObjectName("actionToolBar")
        self.actionReload_Scripts = QtWidgets.QAction(MainWindow)
        self.actionReload_Scripts.setObjectName("actionReload_Scripts")
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionVision_Window = QtWidgets.QAction(MainWindow)
        self.actionVision_Window.setObjectName("actionVision_Window")
        self.actionLog = QtWidgets.QAction(MainWindow)
        self.actionLog.setObjectName("actionLog")
        self.actionMotion_Window = QtWidgets.QAction(MainWindow)
        self.actionMotion_Window.setObjectName("actionMotion_Window")
        self.actionOpen_CSV = QtWidgets.QAction(MainWindow)
        self.actionOpen_CSV.setObjectName("actionOpen_CSV")
        self.actionOpen_Config = QtWidgets.QAction(MainWindow)
        self.actionOpen_Config.setObjectName("actionOpen_Config")
        self.actionOpen_Log = QtWidgets.QAction(MainWindow)
        self.actionOpen_Log.setObjectName("actionOpen_Log")
        self.actionOpen_Result = QtWidgets.QAction(MainWindow)
        self.actionOpen_Result.setObjectName("actionOpen_Result")
        self.actionClose_System = QtWidgets.QAction(MainWindow)
        self.actionClose_System.setObjectName("actionClose_System")
        self.actionUser_Manage = QtWidgets.QAction(MainWindow)
        self.actionUser_Manage.setObjectName("actionUser_Manage")
        self.actionWaveform = QtWidgets.QAction(MainWindow)
        self.actionWaveform.setObjectName("actionWaveform")
        self.menuFile.addAction(self.actionOpen_CSV)
        self.menuFile.addAction(self.actionOpen_Result)
        self.menuFile.addAction(self.actionOpen_Log)
        self.menuFile.addAction(self.actionReload_Scripts)
        self.menuFile.addAction(self.actionReload_CSV)
        self.menuFile.addAction(self.actionClose_System)
        self.menuUser.addAction(self.actionLogin)
        self.menuUser.addAction(self.actionUser_Manage)
        self.menuWindow.addAction(self.actionMain_Window)
        self.menuWindow.addAction(self.actionEdit_Window)
        self.menuWindow.addAction(self.actionMotion_Window)
        self.menuWindow.addAction(self.actionVision_Window)
        self.menuWindow.addAction(self.actionWaveform)
        self.menuWindow.addAction(self.actionToolBar)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuUser.menuAction())
        self.menuBar.addAction(self.menuWindow.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionStart)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionStop)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionMainwindow)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRefresh)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPause)
        self.toolBar.addAction(self.actionContinue)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionLoginTool)
        self.toolBar.addAction(self.actionEdit)
        self.toolBar.addAction(self.actionAutomation)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionLog)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PlatForm"))
        self.lb_title.setText(_translate("MainWindow", "PyQt Software Platform Project"))
        self.pb_snap.setText(_translate("MainWindow", "Snap"))
        self.lb_seq.setText(_translate("MainWindow", "系统状态："))
        self.lb_imagetitle.setText(_translate("MainWindow", "图像："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), _translate("MainWindow", "main"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.log), _translate("MainWindow", "log"))
        self.lb_user_title.setText(_translate("MainWindow", "User:"))
        self.lb_main_user.setText(_translate("MainWindow", "User"))
        self.lb_ver.setText(_translate("MainWindow", "V 1.0.0"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuUser.setTitle(_translate("MainWindow", "User"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionReload_CSV.setText(_translate("MainWindow", "Reload Sequence"))
        self.actionReload_CSV.setToolTip(_translate("MainWindow", "Reload sequence"))
        self.actionLogin.setText(_translate("MainWindow", "Login System"))
        self.actionLogin.setToolTip(_translate("MainWindow", "Login system"))
        self.actionLoop_Test.setText(_translate("MainWindow", "Loop Test"))
        self.actionLoop_Test.setToolTip(_translate("MainWindow", "Loop test"))
        self.actionMain_Window.setText(_translate("MainWindow", "Main Window"))
        self.actionMain_Window.setToolTip(_translate("MainWindow", "Switch to main window"))
        self.actionEdit_Window.setText(_translate("MainWindow", "Sequence Window"))
        self.actionEdit_Window.setToolTip(_translate("MainWindow", "Switch to edit window"))
        self.actionZmq_Debug.setText(_translate("MainWindow", "Zmq Debug"))
        self.actionZmq_Debug.setToolTip(_translate("MainWindow", "Zmq debug"))
        self.actionTcp_Debug.setText(_translate("MainWindow", "Tcp Debug"))
        self.actionTcp_Debug.setToolTip(_translate("MainWindow", "Tcp debug"))
        self.actionSerial_Debug.setText(_translate("MainWindow", "Serial Debug"))
        self.actionStart.setText(_translate("MainWindow", "Start"))
        self.actionStart.setToolTip(_translate("MainWindow", "Start test"))
        self.actionStop.setText(_translate("MainWindow", "Stop"))
        self.actionStop.setToolTip(_translate("MainWindow", "Stop test"))
        self.actionEdit.setText(_translate("MainWindow", "Edit"))
        self.actionEdit.setToolTip(_translate("MainWindow", "Edit sequence"))
        self.actionLoginTool.setText(_translate("MainWindow", "Login"))
        self.actionLoginTool.setToolTip(_translate("MainWindow", "Login system"))
        self.actionAutomation.setText(_translate("MainWindow", "Automation"))
        self.actionAutomation.setToolTip(_translate("MainWindow", "Automation debug"))
        self.actionMainwindow.setText(_translate("MainWindow", "Mainwindow"))
        self.actionMainwindow.setToolTip(_translate("MainWindow", "Switch to main window"))
        self.actionPause.setText(_translate("MainWindow", "Pause"))
        self.actionPause.setToolTip(_translate("MainWindow", "Pause test"))
        self.actionContinue.setText(_translate("MainWindow", "Continue"))
        self.actionContinue.setToolTip(_translate("MainWindow", "Continue test"))
        self.actionToolBar.setText(_translate("MainWindow", "ToolBar"))
        self.actionReload_Scripts.setText(_translate("MainWindow", "Reload Scripts"))
        self.actionReload_Scripts.setToolTip(_translate("MainWindow", "Reload scripts"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh"))
        self.actionRefresh.setToolTip(_translate("MainWindow", "Refresh scripts"))
        self.actionVision_Window.setText(_translate("MainWindow", "Vision Window"))
        self.actionLog.setText(_translate("MainWindow", "Log"))
        self.actionLog.setToolTip(_translate("MainWindow", "log"))
        self.actionMotion_Window.setText(_translate("MainWindow", "Motion Window"))
        self.actionOpen_CSV.setText(_translate("MainWindow", "Open Sequence"))
        self.actionOpen_Config.setText(_translate("MainWindow", "Open Config"))
        self.actionOpen_Log.setText(_translate("MainWindow", "Open Log"))
        self.actionOpen_Result.setText(_translate("MainWindow", "Open Result"))
        self.actionClose_System.setText(_translate("MainWindow", "Close System"))
        self.actionUser_Manage.setText(_translate("MainWindow", "User Manage"))
        self.actionWaveform.setText(_translate("MainWindow", "Waveform"))
