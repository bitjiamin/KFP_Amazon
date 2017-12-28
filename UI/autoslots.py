# -*- coding: UTF-8 -*-
"""
FileName: motioncthread.py
Author: jiaminbit@sina.com
Create date: 2017.6.20
description: 运动控制相关操作
Update date：2017.7.20
version 1.0.0
"""

import csv
import sys
import time
import threading
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import systempath
import sys
import log
from automation import *

sys.path.append(systempath.bundle_dir + '/Scripts')
try:
    import automationscript
except Exception as e:
    log.loginfo.process_log(e)

def reload_scripts():
    try:
        reload(automationscript)
        log.loginfo.process_log('reload auto script ok')
    except Exception as e:
        log.loginfo.process_log(e)

auto = None
class AutoThread(Ui_automation, QDialog, QtCore.QThread):
    def __init__(self, parent=None):
        super(AutoThread, self).__init__(parent)
        self.setupUi(self)
        # 获取屏幕分辨率
        self.screen = QDesktopWidget().screenGeometry()
        self.width = self.screen.width()
        self.height = self.screen.height()
        self.lb_axis.setMaximumHeight(self.height*0.1)
        self.lb_title.setMaximumHeight(self.height*0.1)
        self.io_name = []
        self.io_desc = []
        self.io_value = []
        self.io_index = []
        self.read_axis_config()
        self.writing = False

        self.auto =  automationscript.auto
        self.connect_signals()
        self.init_para_table()
        self.auto.refreshui.connect(self.refresh_para)
        self.auto.syncdata.connect(self.sync_read_write)
        self.d1 = [330, 300, 670, 672, 332, 302, 674, 676, 334,338, 304, 0, 0, 342, 344, 356, 358]
        self.d2 = [510, 512, 408, 394, 518, 390, 392, 400, 402, 408, 42, 40, 44, 46, 48, 50, 52]
        self.d3 = [1000, 3000, 1002, 3002, 1004, 3004, 1006, 3006, 1008, 3008, 1010, 3010, 1012, 3012, 1014, 3014, 1016, 3016, 1018, 3018]

    def  init_para_table(self):
        self.tw_para1.setRowCount(50)
        self.tw_para2.setRowCount(50)
        self.tw_para3.setRowCount(50)
        self.tw_para1.setColumnCount(3)
        self.tw_para2.setColumnCount(3)
        self.tw_para3.setColumnCount(3)
        self.tw_para1.setHorizontalHeaderLabels(['参数', '读取值', '写入值'])
        self.tw_para2.setHorizontalHeaderLabels(['参数', '读取值','写入值'])
        self.tw_para3.setHorizontalHeaderLabels(['参数', '读取值', '写入值'])
        paras1 = ['X轴自动速度','X轴手动速度','X轴正极限','X轴负极限','Y轴自动速度','Y轴手动速度','Y轴正极限','Y轴负极限',
                  'Z轴向下自动速度', 'Z轴向上自动速度', 'Z轴手动速度', 'Z轴正极限', 'Z轴负极限','X轴加速时间','Y轴加速时间','Z向下加速时间','Z向上加速时间']
        paras2 = ['放料位置X','放料位置Y','放料位置Z','进料位置X','进料位置Y','放料位速度X','放料位速度Y','初始位','按压位',
                  '进料抬高位','循环次数','当前次数','上下总时间(s)','XY停顿时间(s)','循环延时(s)','保压时间(s)','触发关断时间(s)']
        paras3 = ['键1测点1-X', '键1测点1-Y', '键1测点2-X', '键1测点2-Y', '键1测点3-X', '键1测点3-Y','键1测点4-X', '键1测点4-Y', '键1测点5-X', '键1测点5-Y',
                  '键2测点1-X', '键2测点1-Y', '键2测点2-X', '键2测点2-Y', '键2测点3-X', '键2测点3-Y','键2测点4-X', '键2测点4-Y', '键2测点5-X', '键2测点5-Y']

        i = 0
        for para1 in paras1:
            newItem1 = QTableWidgetItem(para1)
            self.tw_para1.setItem(i, 0, newItem1)
            i = i + 1
        j = 0
        for para2 in paras2:
            newItem1 = QTableWidgetItem(para2)
            self.tw_para2.setItem(j, 0, newItem1)
            j = j + 1
        k = 0
        for para3 in paras3:
            newItem1 = QTableWidgetItem(para3)
            self.tw_para3.setItem(k, 0, newItem1)
            k = k + 1

    def sync_read_write(self):
        for i in range(len(self.d1)):
            #newItem1 = self.tw_para1.item(i, 1)
            newItem1 = QTableWidgetItem(self.tw_para1.item(i, 1).text())
            self.tw_para1.setItem(i, 2, newItem1)
        for i in range(len(self.d2)):
            newItem1 = QTableWidgetItem(self.tw_para2.item(i, 1).text())
            self.tw_para2.setItem(i, 2, newItem1)

        for i in range(len(self.d3)):
            newItem1 = QTableWidgetItem(self.tw_para3.item(i, 1).text())
            self.tw_para3.setItem(i, 2, newItem1)

    def refresh_para(self):
        # refresh paras
        i = 0
        for d in self.d1:
            if(i<13):
                newItem1 = QTableWidgetItem(str(self.auto.plcD[int(d / 2)]/100))
            else:
                newItem1 = QTableWidgetItem(str(self.auto.plcD[int(d / 2)] / 1000))
            self.tw_para1.setItem(i, 1, newItem1)
            i = i + 1
        j = 0
        for d in self.d2:
            if (j < 9):
                newItem1 = QTableWidgetItem(str(self.auto.plcD[int(d / 2)]/100))
            elif(j<11):
                newItem1 = QTableWidgetItem(str(self.auto.plcD[int(d / 2)]))
            else:
                newItem1 = QTableWidgetItem(str(self.auto.plcD[int(d / 2)]/1000))
            self.tw_para2.setItem(j, 1, newItem1)
            j = j + 1

        k = 0
        # 0,10,1,11,2,12
        for d in self.d3:
            if(k%2 == 0):
                newItem1 = QTableWidgetItem(str(self.auto.plcP[int(k/2)] / 100))
            else:
                newItem1 = QTableWidgetItem(str(self.auto.plcP[int(k/2) + 10] / 100))
            self.tw_para3.setItem(k, 1, newItem1)
            k = k + 1

        # refresh axis paras
        dx = [250, 270, 300, 330, 670, 672]
        dy = [252, 272, 302, 332, 674, 676]
        dz = [254, 274, 304, 334, 0, 0]
        daxis = [dx, dy, dz]
        self.dsb_rtp.setValue(float(self.auto.plcD[int(daxis[automationscript.axis][0] / 2)])/100)
        self.dsb_rts.setValue(float(self.auto.plcD[int(daxis[automationscript.axis][1] / 2)])/100)
        self.dsb_manuals.setValue(float(self.auto.plcD[int(daxis[automationscript.axis][2] / 2)])/100)
        self.dsb_autos.setValue(float(self.auto.plcD[int(daxis[automationscript.axis][3] / 2)])/100)
        self.dsb_limit1.setValue(float(self.auto.plcD[int(daxis[automationscript.axis][4] / 2)])/100)
        self.dsb_limit2.setValue(float(self.auto.plcD[int(daxis[automationscript.axis][5] / 2)])/100)

        sensorx = [665, 660, 661]
        sensory = [685, 680, 681]
        sensorz = [705, 700, 701]
        sensor = [sensorx, sensory, sensorz]

        if(self.auto.plcM[sensor[automationscript.axis][0]-660] == '1'):
            self.cb_zero.setChecked(True)
        else:
            self.cb_zero.setChecked(False)

        if (self.auto.plcM[sensor[automationscript.axis][1]-660] == '1'):
            self.cb_limit1.setChecked(True)
        else:
            self.cb_limit1.setChecked(False)

        if (self.auto.plcM[sensor[automationscript.axis][2]-660] == '1'):
            self.cb_limit2.setChecked(True)
        else:
            self.cb_limit2.setChecked(False)

    def showEvent(self, e):
        self.tabWidget.setCurrentIndex(0)
        automationscript.read_thread = True

    def closeEvent(self, e):
        print('close.....')

    def connect_signals(self):
        self.pb_cyin.clicked.connect(self.auto.dut_in)
        self.pb_cyout.clicked.connect(self.auto.dut_out)
        self.pb_cypress.clicked.connect(self.auto.dut_press)
        self.pb_cyrelease.clicked.connect(self.auto.dut_release)
        self.pb_cyair1.clicked.connect(self.auto.air_in)
        self.pb_cyair2.clicked.connect(self.auto.air_out)
        self.pb_dutin.clicked.connect(self.auto.dut_in)
        self.pb_dutout.clicked.connect(self.auto.dut_out)
        self.pb_initp.clicked.connect(self.auto.z_init_pos)
        self.pb_pressp.clicked.connect(self.auto.z_press_pos)
        self.pb_single.clicked.connect(self.auto.single_press)
        self.pb_loop.clicked.connect(self.auto.loop_press)
        self.pb_loopstop.clicked.connect(self.auto.loop_stop)
        self.pb_clear.clicked.connect(self.auto.clear_loop_count)

        self.pb_jog1.pressed.connect(self.auto.axis_jog1_run)
        self.pb_jog1.released.connect(self.auto.axis_jog1_stop)
        self.pb_jog2.pressed.connect(self.auto.axis_jog2_run)
        self.pb_jog2.released.connect(self.auto.axis_jog2_stop)
        self.pb_reset.released.connect(self.auto.axis_reset)
        self.pb_axis_stop.released.connect(self.auto.axis_stop)

        self.cb_axis.currentIndexChanged.connect(self.change_axis)
        self.cb_red.stateChanged.connect(self.auto.switch_red)
        self.cb_yellow.stateChanged.connect(self.auto.switch_yellow)
        self.cb_green.stateChanged.connect(self.auto.switch_green)
        self.cb_buzz.stateChanged.connect(self.auto.switch_buzz)
        self.cb_fail.stateChanged.connect(self.auto.switch_fail)
        self.cb_daq.stateChanged.connect(self.auto.switch_daq)
        self.cb_start.stateChanged.connect(self.auto.switch_start)
        self.cb_stop.stateChanged.connect(self.auto.switch_stop)
        self.cb_reset.stateChanged.connect(self.auto.switch_reset)
        self.cb_pass.stateChanged.connect(self.auto.switch_pass)
        self.cb_light.stateChanged.connect(self.auto.switch_light)
        self.cb_manual.stateChanged.connect(self.auto.switch_manual)
        self.cb_door.stateChanged.connect(self.auto.switch_door)

        self.pb_save1.clicked.connect(self.save_para1)
        self.pb_save2.clicked.connect(self.save_para2)
        self.pb_save3.clicked.connect(self.save_para3)

    def change_axis(self):
        automationscript.axis = self.cb_axis.currentIndex()

    # 初始化IO表，从配置文件中读取信息
    def initialize_motion_ui(self):
        self.tw_io.setMaximumWidth(self.width * 0.4)
        self.read_io_config()
        self.read_axis_config()
        self.tw_io.setColumnCount(2)
        self.tw_io.setRowCount(len(self.io_name) + 10)
        self.tw_io.setHorizontalHeaderLabels(['IO', 'Description'])
        self.mapper = QtCore.QSignalMapper(self)
        i = 0
        for seq in self.io_name:
            if(i != 0):
                self.MyCheck = QCheckBox()
                self.MyCheck.setText('--- ' + seq)
                self.tw_io.setCellWidget(i-1, 0, self.MyCheck)
                newItem = QTableWidgetItem(self.io_desc[i])
                self.tw_io.setItem(i - 1, 1, newItem)
                # 原始信号（表格中checkbox的鼠标点击信号）传递给map
                self.tw_io.cellWidget(i - 1, 0).clicked.connect(self.mapper.map)
                # 设置map信号的转发规则, 转发为参数为int类型的信号
                self.mapper.setMapping(self.tw_io.cellWidget(i - 1, 0), i - 1)
            i = i+1

        # map信号连接到自定义的槽函数，参数类型为int
        self.mapper.mapped[int].connect(self.write_io)

        self.tw_io.horizontalHeader().setStretchLastSection(True)
        j = 0
        self.cb_axis.clear()
        for seq in self.axis_name:
            if(j != 0):
                self.cb_axis.addItem(seq)
            j = j+1

    def English_ui(self):
        # 序列编辑
        self.lb_edit.setText('Edit Test Sequence')
        self.pb_insertrow.setText('Insert Row')
        self.pb_delrow.setText('Delete Row')
        self.pb_saveseq.setText('Save')
        self.tableseq.setHorizontalHeaderLabels(
            ['TestItem', 'Function', 'Mode', 'Low Limit', 'Up Limit', 'Next Step', 'Level'])

    def Chinese_ui(self):
        # 序列编辑
        self.lb_edit.setText('序列编辑')
        self.pb_insertrow.setText('插入行')
        self.pb_delrow.setText('删除选定行')
        self.pb_saveseq.setText('保存序列')
        self.tableseq.setHorizontalHeaderLabels(['测试项', '函数', '模式', '下限', '上限', '失败后跳转', '等级'])

    def change_language(self):
        if(self.language.currentIndex() == 0):
            self.English_ui()
        else:
            self.Chinese_ui()

    def read_axis_config(self):
        self.path = systempath.bundle_dir + '/CSV Files/' + 'Axis Config.csv'
        csvfile = open(self.path, 'r')
        reader = csv.reader(csvfile)
        self.axis_name = []
        self.axis_desc = []
        for seq in reader:
            self.axis_name.append(seq[0])
            self.axis_desc.append(seq[1])

    def save_para1(self):
        for i in range(len(self.d1)):
            if (i < 13):
                data = int(float(self.tw_para1.item(i, 2).text()) * 100)
            else:
                data = int(float(self.tw_para1.item(i, 2).text()) * 1000)
            self.auto.plc.write_intD(str(self.d1[i]), data)

    def save_para2(self):
        for i in range(len(self.d2)):
            if (i < 9):
                data = int(float(self.tw_para2.item(i, 2).text()) * 100)
            elif(i<11):
                data = int(float(self.tw_para2.item(i, 2).text()))
            else:
                data = int(float(self.tw_para2.item(i, 2).text()) * 1000)
            self.auto.plc.write_intD(str(self.d2[i]), data)

    def save_para3(self):
        for i in range(len(self.d3)):
            data = int(float(self.tw_para3.item(i, 2).text()) * 100)
            self.auto.plc.write_intD(str(self.d3[i]), data)