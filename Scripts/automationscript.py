# -*- coding: UTF-8 -*-
"""
FileName: automationscript.py
Author: jiaminbit@sina.com
Create date: 2017.6.20
description: 自动化脚本，将运动控制相关函数定义在改文件
Update date：2017.7.20
version 1.0.0
"""

import random
import socket
import struct
import time
import systempath
import csv
import serial
import os
import plccomm
from automation import *
from PyQt5 import QtCore
import threading
import configparser
import log

global axis
global read_thread
axis = 0
read_thread = False
global auto


class AutoMation(QtCore.QThread):
    #实现一个单例类
    _instance = None
    __first_init = True
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    refreshui = QtCore.pyqtSignal()
    syncdata = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        if(self.__class__.__first_init):     # 只初始化一次
            self.__class__.__first_init = False  # 只初始化一次
            super(AutoMation, self).__init__(parent)
            plccomm.plc = plccomm.PlcCom()
            self.plc = plccomm.plc
            #self.create_connect()
            self.plc_para1 = threading.Thread(target=self.read_plcpara1)
            self.plc_para1.setDaemon(True)
            #self.plc_para1.start()
            self.axisM = ['10','11','12','13','14','15']
            self.mainD = [0,0,0,0]
            self.singledone = '00000000'

    def read_error(self, key):
        try:
            cf = configparser.ConfigParser()
            cf.read( systempath.bundle_dir + '/Config/ErrorInfo.ini')
            value = cf.get('Error', key)
        except Exception as e:
            value = ''
        return value

    def read_plcpara1(self):
        time.sleep(2)
        j = 0
        while (True):
            self.errM = self.plc.read_blockM("800", 50)
            self.mainD = self.plc.read_block_intD("490", 4)
            for i in range(len(self.errM)):
                if (self.errM[i] == '1'):
                    err = self.read_error(str(i + 1))
                    if (err != ''):
                        #time.sleep(1)
                        log.loginfo.process_log(err)
            if(read_thread):
                self.plcD = self.plc.read_block_intD('0', 200) + self.plc.read_block_intD('200', 200) \
                            + self.plc.read_block_intD('400', 200) + self.plc.read_block_intD('600', 100)
                self.plcP = self.plc.read_block_intD('1000', 20) + self.plc.read_block_intD('3000', 20)
                self.plcM = self.plc.read_blockM('660', 50)
                self.refreshui.emit()
                if(j<10):
                    self.syncdata.emit()
                j =j + 1
                time.sleep(0.1)
            time.sleep(0.01)

    #读取IO配置列表
    def read_config(self):
        self.path = os.getcwd()
        self.cvspath = systempath.bundle_dir+ '/CSV Files/' + 'IO Config.csv'
        csvfile = open(self.cvspath, 'r')
        reader = csv.reader(csvfile)
        self.io_channel=[]
        self.io_channel2=[]
        for seg in reader:
            self.io_channel.append(seg[2])
        for seg2 in self.io_channel[1:]:    #从csv表第2行开始读int数据
            self.io_channel2.append(int(seg2))
        self.io_channel2 = sorted(self.io_channel2)
        self.start_index = self.io_channel2[0]      #io开始位索引
        self.io_length = self.io_channel2[-1]-self.io_channel2[0]+1     #读取长度
        return [self.start_index, self.io_length]

    def create_connect(self):
        con_ok = self.plc.tcp_connect()

    def close_connect(self):
        self.tcp_close()

    def dut_in(self):
        self.plc.write_M("97", "1")
        self.plc.write_M("104", "0")

    def dut_out(self):
        self.plc.write_M("97", "0")
        self.plc.write_M("104", "1")

    def dut_press(self):
        self.plc.write_M("98", "1")
        self.plc.write_M("116", "0")

    def dut_release(self):
        self.plc.write_M("98", "0")
        self.plc.write_M("116", "1")

    def mannual_in(self):
        self.plc.write_M("230", "1")

    def mannual_out(self):
        self.plc.write_M("231", "1")

    def air_in(self):
        self.plc.write_M("99", "1")

    def air_out(self):
        self.plc.write_M("99", "0")

    def z_init_pos(self):
        self.plc.write_M("204", '1')

    def z_press_pos(self):
        self.plc.write_M("203", '1')

    def single_press(self):
        self.plc.write_M("250", '1')

    def loop_press(self):
        self.plc.write_M("251", '1')

    def loop_stop(self):
        self.plc.write_M("251", '0')

    def clear_loop_count(self):
        self.plc.write_M("40", '0')

    def switch_red(self, index):
        if (index == 0):
            self.plc.write_M("90", "0")
        else:
            self.plc.write_M("90", "1")

    def switch_yellow(self, index):
        if (index == 0):
            self.plc.write_M("92", "0")
        else:
            self.plc.write_M("92", "1")

    def switch_green(self, index):
        if(index == 0):
            self.plc.write_M("93", "0")
        else:
            self.plc.write_M("93", "1")

    def switch_buzz(self, index):
        if (index == 0):
            self.plc.write_M("91", "0")
        else:
            self.plc.write_M("91", "1")

    def switch_fail(self, index):
        if (index == 0):
            self.plc.write_M("115", "0")
        else:
            self.plc.write_M("115", "1")

    def switch_daq(self, index):
        if (index == 0):
            self.plc.write_M("119", "0")
        else:
            self.plc.write_M("119", "1")

    def switch_start(self, index):
        if (index == 0):
            self.plc.write_M("94", "0")
        else:
            self.plc.write_M("94", "1")

    def switch_stop(self, index):
        if (index == 0):
            self.plc.write_M("95", "0")
        else:
            self.plc.write_M("95", "1")

    def switch_reset(self, index):
        if (index == 0):
            self.plc.write_M("96", "0")
        else:
            self.plc.write_M("96", "1")

    def switch_pass(self, index):
        if (index == 0):
            self.plc.write_M("114", "0")
        else:
            self.plc.write_M("114", "1")

    def switch_light(self, index):
        if (index == 0):
            self.plc.write_M("118", "0")
        else:
            self.plc.write_M("118", "1")

    def switch_manual(self, index):
        if (index == 0):
            self.plc.write_M("227", "0")
        else:
            self.plc.write_M("227", "1")

    def switch_door(self, index):
        if (index == 0):
            self.plc.write_M("236", "0")
        else:
            self.plc.write_M("236", "1")

    def axis_jog1_run(self):
        self.plc.write_M("9", "1")
        self.plc.write_M(self.axisM[2*axis], "1")

    def axis_jog1_stop(self):
        self.plc.write_M("9", "1")
        self.plc.write_M(self.axisM[2*axis], "0")

    def axis_jog2_run(self):
        self.plc.write_M("9", "1")
        self.plc.write_M(self.axisM[2*axis + 1], "1")

    def axis_jog2_stop(self):
        self.plc.write_M("9", "1")
        self.plc.write_M(self.axisM[2*axis + 1], "0")

    def axis_reset(self):
        if(axis == 0):
            self.plc.write_M('61', "1")
        elif(axis == 1):
            self.plc.write_M('65', "1")
        elif (axis == 2):
            self.plc.write_M('69', "1")

    def axis_stop(self):
        return True