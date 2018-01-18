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
from imp import reload
import threading
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import systempath
import inihelper
import log
from automation import *
import dataexchange
import daqcomm
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from visionscript import *

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
        self.lb_title.setMaximumHeight(self.height*0.1)
        self.io_name = []
        self.io_desc = []
        self.io_value = []
        self.io_index = []
        self.read_axis_config()
        self.writing = False
        self.auto =  automationscript.auto
        self.init_wave()
        try:
            self.connect_signals()
            self.init_para_table()
            self.auto.refreshui.connect(self.refresh_para)
            self.auto.syncdata.connect(self.sync_read_write)
        except Exception as e:
            print(e)
        self.d1 = [330, 300, 670, 672, 332, 302, 674, 676, 334,338, 304, 0, 0, 356, 358]
        self.d2 = [510, 512, 408, 390, 392, 394, 518, 400, 402, 366, 526, 528, 530, 42, 40, 48, 50, 58, 46]
        self.d3 = [1000, 3000, 1002, 3002, 1004, 3004, 1006, 3006, 1008, 3008, 1010, 3010, 1012, 3012, 1014, 3014, 1016, 3016, 1018, 3018]

    def  init_para_table(self):
        self.tw_para1.setRowCount(50)
        self.tw_para2.setRowCount(50)
        self.tw_para3.setRowCount(50)
        self.tw_para1.setColumnCount(2)
        self.tw_para2.setColumnCount(2)
        self.tw_para3.setColumnCount(2)
        self.tw_para1.horizontalHeader().setStretchLastSection(True)
        self.tw_para2.horizontalHeader().setStretchLastSection(True)
        self.tw_para3.horizontalHeader().setStretchLastSection(True)
        self.tw_para1.setHorizontalHeaderLabels(['参数', '读取值'])
        self.tw_para2.setHorizontalHeaderLabels(['参数', '读取值'])
        self.tw_para3.setHorizontalHeaderLabels(['参数', '读取值'])
        paras1 = ['X轴自动速度','X轴手动速度','X轴正极限','X轴负极限','Y轴自动速度','Y轴手动速度','Y轴正极限','Y轴负极限',
                  'Z轴向下自动速度', 'Z轴向上自动速度', 'Z轴手动速度', 'Z轴正极限', 'Z轴负极限','Z向下加速时间','Z向上加速时间']

        paras2 = ['放料位置X','放料位置Y','放料位置Z','放料位速度X','放料位速度Y','进料位置X','进料位置Y','初始位','按压位', '键高',
                  '探针标定X：','探针标定Y：','探针标定Z：','循环次数','当前次数','循环延时(s)','保压时间(s)','触发关断时间(s)', 'XY停顿时间(s)']

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
                if (j < 13):
                    newItem1 = QTableWidgetItem(str(self.auto.plcD[int(d / 2)]/100))
                elif(j<15):
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

            if (self.auto.switch[0] == '1'):
                self.cb_manual.setChecked(True)
            else:
                self.cb_manual.setChecked(False)

            if (self.auto.switch[1] == '1'):
                self.cb_door.setChecked(True)
            else:
                self.cb_door.setChecked(False)

            if (self.auto.switch[2] == '1'):
                self.cb_light.setChecked(True)
            else:
                self.cb_light.setChecked(False)

            if (self.auto.switch[3] == '1'):
                self.cb_daq.setChecked(True)
            else:
                self.cb_daq.setChecked(False)
            try:
                self.dsb_xpos.setValue(float(self.auto.plcD[int(450 / 2)]) / 100)
                self.dsb_ypos.setValue(float(self.auto.plcD[int(452 / 2)]) / 100)
                self.dsb_zpos.setValue(float(self.auto.plcD[int(454 / 2)]) / 100)
            except Exception as e:
                print(e)

    def refresh_para(self):
        try:
            # refresh axis paras
            dx = [250, 270, 300, 330, 450]  #当前位置，当前速度，手动速度，自动速度, 绝对位置
            dy = [252, 272, 302, 332, 452]
            dz = [254, 274, 304, 334, 454]
            self.dsb_rtpx.setValue(float(self.auto.plcD[int(dx[0] / 2)])/100)
            self.dsb_rtsx.setValue(float(self.auto.plcD[int(dx[1] / 2)])/100)
            self.dsb_manualsx.setValue(float(self.auto.plcD[int(dx[2] / 2)]) / 100)
            self.dsb_autosx.setValue(float(self.auto.plcD[int(dx[3] / 2)]) / 100)

            self.dsb_rtpy.setValue(float(self.auto.plcD[int(dy[0] / 2)]) / 100)
            self.dsb_rtsy.setValue(float(self.auto.plcD[int(dy[1] / 2)]) / 100)
            self.dsb_manualsy.setValue(float(self.auto.plcD[int(dy[2] / 2)]) / 100)
            self.dsb_autosy.setValue(float(self.auto.plcD[int(dy[3] / 2)]) / 100)

            self.dsb_rtpz.setValue(float(self.auto.plcD[int(dz[0] / 2)]) / 100)
            self.dsb_rtsz.setValue(float(self.auto.plcD[int(dz[1] / 2)]) / 100)
            self.dsb_manualsz.setValue(float(self.auto.plcD[int(dz[2] / 2)]) / 100)
            self.dsb_autosz.setValue(float(self.auto.plcD[int(dz[3] / 2)]) / 100)

            sensorx = [665, 660, 661]
            sensory = [685, 680, 681]
            sensorz = [705, 700, 701]
            switch = [227, 236, 118, 300]
            sensor = [sensorx, sensory, sensorz]

            if(self.auto.plcM[sensorx[0]-660] == '0'):
                self.cb_zerox.setChecked(True)
            else:
                self.cb_zerox.setChecked(False)

            if (self.auto.plcM[sensorx[1]-660] == '0'):
                self.cb_limit1x.setChecked(True)
            else:
                self.cb_limit1x.setChecked(False)

            if (self.auto.plcM[sensorx[2]-660] == '0'):
                self.cb_limit2x.setChecked(True)
            else:
                self.cb_limit2x.setChecked(False)

            if (self.auto.plcM[sensory[0] - 660] == '0'):
                self.cb_zeroy.setChecked(True)
            else:
                self.cb_zeroy.setChecked(False)

            if (self.auto.plcM[sensory[1] - 660] == '0'):
                self.cb_limit1y.setChecked(True)
            else:
                self.cb_limit1y.setChecked(False)

            if (self.auto.plcM[sensory[2] - 660] == '0'):
                self.cb_limit2y.setChecked(True)
            else:
                self.cb_limit2y.setChecked(False)

            if (self.auto.plcM[sensorz[0] - 660] == '0'):
                self.cb_zeroz.setChecked(True)
            else:
                self.cb_zeroz.setChecked(False)

            if (self.auto.plcM[sensorz[1] - 660] == '0'):
                self.cb_limit1z.setChecked(True)
            else:
                self.cb_limit1z.setChecked(False)

            if (self.auto.plcM[sensorz[2] - 660] == '0'):
                self.cb_limit2z.setChecked(True)
            else:
                self.cb_limit2z.setChecked(False)
        except Exception as e:
            print(e)

    def showEvent(self, e):
        self.tabWidget.setCurrentIndex(0)
        automationscript.read_thread = True
        try:
            self.calpos1X.setValue(float(inihelper.read_ini(systempath.bundle_dir + '/Config/Calibration.ini', 'Calibration', 'pos1x')))
            self.calpos1Y.setValue(float(inihelper.read_ini(systempath.bundle_dir + '/Config/Calibration.ini', 'Calibration', 'pos1y')))
            self.calpos2X.setValue(float(inihelper.read_ini(systempath.bundle_dir + '/Config/Calibration.ini', 'Calibration', 'pos2x')))
            self.calpos2Y.setValue(float(inihelper.read_ini(systempath.bundle_dir + '/Config/Calibration.ini', 'Calibration', 'pos2y')))
            self.calpos3X.setValue(float(inihelper.read_ini(systempath.bundle_dir + '/Config/Calibration.ini', 'Calibration', 'pos3x')))
            self.calpos3Y.setValue(float(inihelper.read_ini(systempath.bundle_dir + '/Config/Calibration.ini', 'Calibration', 'pos3y')))

            self.cameraposX.setValue(float(inihelper.read_ini(systempath.bundle_dir + '/Config/Calibration.ini', 'Calibration', 'markcapx')))
            self.cameraposY.setValue(float(inihelper.read_ini(systempath.bundle_dir + '/Config/Calibration.ini', 'Calibration', 'markcapy')))
            self.markX.setValue(float(inihelper.read_ini(systempath.bundle_dir + '/Config/Calibration.ini', 'Calibration', 'markx')))
            self.markY.setValue(float(inihelper.read_ini(systempath.bundle_dir + '/Config/Calibration.ini', 'Calibration', 'marky')))
            self.headX.setValue(float(inihelper.read_ini(systempath.bundle_dir + '/Config/Calibration.ini', 'Calibration', 'loadcellx')))
            self.headY.setValue(float(inihelper.read_ini(systempath.bundle_dir + '/Config/Calibration.ini', 'Calibration', 'loadcelly')))

        except Exception as e:
            print(e)

    def closeEvent(self, e):
        automationscript.read_thread = False

    def connect_signals(self):
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

        self.pb_x1.pressed.connect(self.auto.axisx_jog1_run)
        self.pb_x1.released.connect(self.auto.axisx_jog1_stop)
        self.pb_x2.pressed.connect(self.auto.axisx_jog2_run)
        self.pb_x2.released.connect(self.auto.axisx_jog2_stop)
        self.pb_xhome.clicked.connect(self.auto.x_home)
        self.pb_xrun.clicked.connect(self.x_absolute)

        self.pb_y1.pressed.connect(self.auto.axisy_jog1_run)
        self.pb_y1.released.connect(self.auto.axisy_jog1_stop)
        self.pb_y2.pressed.connect(self.auto.axisy_jog2_run)
        self.pb_y2.released.connect(self.auto.axisy_jog2_stop)
        self.pb_yhome.clicked.connect(self.auto.y_home)
        self.pb_yrun.clicked.connect(self.y_absolute)

        self.pb_z1.pressed.connect(self.auto.axisz_jog1_run)
        self.pb_z1.released.connect(self.auto.axisz_jog1_stop)
        self.pb_z2.pressed.connect(self.auto.axisz_jog2_run)
        self.pb_z2.released.connect(self.auto.axisz_jog2_stop)
        self.pb_zhome.clicked.connect(self.auto.z_home)
        self.pb_zrun.clicked.connect(self.z_absolute)

        self.cb_daq.stateChanged.connect(self.auto.switch_daq)
        self.cb_light.stateChanged.connect(self.auto.switch_light)
        self.cb_manual.stateChanged.connect(self.auto.switch_manual)
        self.cb_door.stateChanged.connect(self.auto.switch_door)

        self.pb_save1.clicked.connect(self.save_para1)
        self.pb_save2.clicked.connect(self.save_para2)
        self.pb_save3.clicked.connect(self.save_para3)

        self.pb_clearerror.clicked.connect(self.auto.clear_error)

        self.pb_sensorcal.clicked.connect(self.sensor_calibration_thread)
        self.pb_cameracal.clicked.connect(self.camera_calibration_thread)
        self.pb_probe.clicked.connect(self.probe_calibration_thread)

    def x_absolute(self):
        data = int(self.dsb_xpos.value()*100)
        self.auto.plc.write_intD("450", data)
        self.auto.plc.write_M('903', "1")

    def y_absolute(self):
        data = int(self.dsb_ypos.value() * 100)
        self.auto.plc.write_intD("452", data)
        self.auto.plc.write_M('904', "1")

    def z_absolute(self):
        data = int(self.dsb_zpos.value() * 100)
        self.auto.plc.write_intD("454", data)
        self.auto.plc.write_M('905', "1")

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
                data = int(float(self.tw_para1.item(i, 1).text()) * 100)
            else:
                data = int(float(self.tw_para1.item(i, 1).text()) * 1000)
            self.auto.plc.write_intD(str(self.d1[i]), data)

    def save_para2(self):
        for i in range(len(self.d2)):
            if (i < 13):
                data = int(float(self.tw_para2.item(i, 1).text()) * 100)
            elif(i<15):
                data = int(float(self.tw_para2.item(i, 1).text()))
            else:
                data = int(float(self.tw_para2.item(i, 1).text()) * 1000)
            self.auto.plc.write_intD(str(self.d2[i]), data)

    def save_para3(self):
        for i in range(len(self.d3)):
            data = int(float(self.tw_para3.item(i, 1).text()) * 100)
            self.auto.plc.write_intD(str(self.d3[i]), data)

    def sensor_calibration_thread(self):
        self.zpos = [62, 62.03, 62.06, 62.09, 62.12, 62.15, 50]
        self.zpos[0] = float(inihelper.read_ini(systempath.bundle_dir + '/Config/Calibration.ini', 'Calibration', 'posz1'))
        self.zpos[1] = float(inihelper.read_ini(systempath.bundle_dir + '/Config/Calibration.ini', 'Calibration', 'posz2'))
        self.zpos[2] = float(inihelper.read_ini(systempath.bundle_dir + '/Config/Calibration.ini', 'Calibration', 'posz3'))
        self.zpos[3] = float(inihelper.read_ini(systempath.bundle_dir + '/Config/Calibration.ini', 'Calibration', 'posz4'))
        self.zpos[4] = float(inihelper.read_ini(systempath.bundle_dir + '/Config/Calibration.ini', 'Calibration', 'posz5'))
        self.zpos[5] = float(inihelper.read_ini(systempath.bundle_dir + '/Config/Calibration.ini', 'Calibration', 'posz6'))
        sensorthread = threading.Thread(target=self.sensor_calibration)
        sensorthread.setDaemon(True)
        sensorthread.start()

    def absoluteX(self, pos):
        self.auto.plc.write_intD("450", int(pos * 100))
        self.auto.plc.write_M('903', "1")
        i = 0
        while (True):
            if (self.auto.plc.read_M("840")[0] == '1' or i > 200):
                if (i > 200):
                    jump = True
                else:
                    jump = False
                break  # X轴绝对运动完成
            time.sleep(0.05)
            i = i + 1
        return jump

    def absoluteY(self, pos):
        self.auto.plc.write_intD("452", int(pos * 100))
        self.auto.plc.write_M('904', "1")
        i = 0
        while (True):
            if (self.auto.plc.read_M("841")[0] == '1' or i > 200):
                if (i > 200):
                    jump = True
                else:
                    jump = False
                break  # Y轴绝对运动完成
            time.sleep(0.05)
            i = i + 1
        return jump

    def absoluteZ(self, pos):
        self.auto.plc.write_intD("454", int(pos * 100))
        self.auto.plc.write_M('905', "1")
        i = 0
        while (True):
            if (self.auto.plc.read_M("842")[0] == '1' or i > 200):
                if (i > 200):
                    jump = True
                else:
                    jump = False
                break  # Y轴绝对运动完成
            time.sleep(0.05)
            i = i + 1
        return jump

    def init_wave(self):
        # a figure instance to plot on
        self.figure = Figure()
        self.figure.subplots_adjust(left=0.14, bottom=0.2, right=0.9, top=0.9)
        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        self.grid_wave.addWidget(self.canvas)
        self.grid_wave.setRowStretch(0, 1)
        self.grid_wave.setRowStretch(1, 1)
        ''' plot some random stuff '''
        # create an axis
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlabel('Voltage(v)')
        self.ax.set_ylabel('Force(g)')

    def sensor_calibration(self):
        log.loginfo.process_log('Start sensor calibration!')
        self.pb_sensorcal.setEnabled(False)
        try:
            # x轴到指定位置
            xpos = [self.calpos1X.value(), self.calpos2X.value(), self.calpos3X.value()]
            ypos = [self.calpos1Y.value(), self.calpos2Y.value(), self.calpos3Y.value()]
            jump = False
            for j in range(3):
                log.loginfo.process_log('Calibration point: ' + str(j+1))
                print('loop time: '+ str(j))
                # x轴到指定位置
                ret = self.absoluteX(xpos[j])
                if(ret):
                    break
                # y轴到指定位置
                ret = self.absoluteY(ypos[j])
                if (ret):
                    break
                # z轴到指定位置
                for k in range(6):
                    ret = self.absoluteZ(self.zpos[k])
                    if (ret):
                        break
                    time.sleep(2)
                    daqcomm.daq.send_cal_cmd()
                    time.sleep(0.5)
                #log.loginfo.process_log(str(dataexchange.daqcal1))
                # z轴到起始位置
                ret = self.absoluteZ(self.zpos[6])
            datax = dataexchange.daqcal1
            log.loginfo.process_log(str(datax))
            datay = [x*251.1160045527 -125.1905129219 for x in dataexchange.daqcal2]
            log.loginfo.process_log(str(datay))
            line = np.polyfit(datax, datay, 1)
            liney = [x * line[0] + line[1] for x in datax]
            self.ax.plot(datax, liney, '-')
            self.ax.plot(datax, datay, '.r')
            self.ax.text(4, 180, 'Min Slope: 59, Max Slope: 61', fontsize=20)
            self.ax.text(4, 200, 'Slope: ' + str(line[0]), fontsize=20)
            self.canvas.draw()
            # 校准完成，复位系统
            self.auto.system_reset()
            # 校准完成，复位系统
            log.loginfo.process_log('Slope: ' + str(line[0]))
            if(line[0]<60.5 and line[0]>60):
                daqcomm.daq.write_calibration(line[0])
                log.loginfo.process_log('Calibration Success!')
            else:
                log.loginfo.process_log('Calibration Fail!')
            self.pb_sensorcal.setEnabled(True)
        except Exception as e:
            print(e)
            self.pb_sensorcal.setEnabled(True)


    def camera_calibration_thread(self):
        camerathread = threading.Thread(target=self.camera_calibration)
        camerathread.setDaemon(True)
        camerathread.start()

    def camera_calibration(self):
        try:
            self.pb_cameracal.setEnabled(False)
            log.loginfo.process_log('Start camera calibration!')
            # x轴到指定位置
            markcapx = float(
                inihelper.read_ini(systempath.bundle_dir + '/Config/Calibration.ini', 'Calibration', 'markcapx'))
            markcapy = float(
                inihelper.read_ini(systempath.bundle_dir + '/Config/Calibration.ini', 'Calibration', 'markcapy'))

            ret = self.absoluteX(markcapx)

            # y轴到指定位置
            if(ret == False):
                ret = self.absoluteY(markcapy)
            if(ret == False):
                self.vision = Vision()
                self.auto.plc.write_M('300', '1')
                self.vision.kfpv.set_extime(50000.0)
                self.vision.snap()
                self.auto.plc.write_M('300', '0')
                self.vision.kfpv.set_extime(180000.0)
                retxy = self.vision.find_mark_point()
            # 校准完成，复位系统
            self.auto.system_reset()
            self.pb_cameracal.setEnabled(True)
        except Exception as e:
            print(e)
            self.pb_cameracal.setEnabled(True)

    def probe_calibration_thread(self):
        probethread = threading.Thread(target=self.probe_calibration)
        probethread.setDaemon(True)
        probethread.start()

    def probe_calibration(self):
        self.auto.plc.write_M('284', '1')
        i = 0
        while(True):
            if(self.auto.plc.read_blockM('286',1)=='1' or i>100):
                break
            time.sleep(0.1)
            i = i + 1
        # read XY
        time.sleep(2)
        x = self.dsb_rtpx.value()
        print('xxxxxxxxxxxxxxxxxx')
        print(x)
        # get XY ok
        self.auto.plc.write_M('287', '1')

        while (True):
            if (self.auto.plc.read_blockM('291', 1) == '1' or i > 100):
                break
            time.sleep(0.1)
            i = i + 1
        # read XY
        time.sleep(2)
        y = self.dsb_rtpy.value()
        print('yyyyyyyyyyyyyyyyyyyyyy')
        print(y)
        # get XY ok
        self.auto.plc.write_M('292', '1')