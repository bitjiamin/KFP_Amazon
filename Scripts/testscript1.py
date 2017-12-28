# -*- coding: UTF-8 -*-
"""
FileName: testscript.py
Author: jiaminbit@sina.com
Create date: 2017.6.20
description: 测试脚本，将各测试项的函数定义在该文件中
Update date：2017.7.20
version 1.0.0
"""

import time
import log
import zmq
import os
import subprocess
import plccomm
import daqcomm
try:
    import automationscript
except Exception as e:
    log.loginfo.process_log(e)
import threading
from visionscript import *


class TestFunc():
    #实现一个单例类
    _instance = None
    __first_init = True
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if(self.__class__.__first_init):     # 只初始化一次
            self.__class__.__first_init = False
            automationscript.auto = automationscript.AutoMation()
            self.plc = plccomm.PlcCom()
            self.plcthread = threading.Thread(target=self.plc_thread)
            self.plcthread.setDaemon(True)
            #self.plcthread.start()
            self.in_done = False
            self.zmq_open()
            daqcomm.daq = daqcomm.DAQ()
            self.daq = daqcomm.daq
            #self.daq.tcp_connect()
            #self.vision = Vision()

    def __del__(self):
        self.zmq_close()
        pass

    def plc_thread(self):
        time.sleep(2)
        while(True):
            self.state = automationscript.auto.mainD[0]
            if(self.state == 1):  # scan sn
                self.in_done = False
                self.plc.write_intD("490", 0)  # reset
                #self.plc.write_intD("492", 1)  # scan ok, start dut in
                #self.plc.write_intD("492", 2)  # scan fail
            elif(self.state == 2):      #dut in done
                log.loginfo.process_log(str('dut in done'))
                self.in_done = True
                self.plc.write_intD("490", 0)  # reset
                # capture image
                #z=2.61,x=288.37,y=37.11
                capX = 288.37
                capY = 37.11
                #self.plc.write_intD("502", (int)(capX * 100))
                #self.plc.write_intD("504", (int)(capY * 100))
                #self.plc.write_intD("500", 1)
                #self.vision.snap()
                # start test
                self.zmq_comm('Start')
                #self.plc.write_intD("492", 3)  #通知PLC开始测试
                # 定义结束点
                #self.plc.write_shortD("13", 40)
                #self.plc.write_shortD("12", 5)
            elif(self.state == 3):
                #PLC测试完成
                self.plc.write_intD("490", 0)
                #self.plc.write_intD("492", 4)  #通知PLC，上位机测试完成
                self.plc.write_intD("492", 5) #通知PLC，上位机测试完成,Pass
                #self.plc.write_intD("492", 6)  # 通知PLC，上位机测试完成,Fail

    def zmq_open(self):
        self.con = zmq.Context()
        self.socket = self.con.socket(zmq.REQ)
        #接收超时2秒，发送超时1秒
        self.socket.RCVTIMEO = 2000
        self.socket.SNDTIMEO = 1000
        try:
            self.socket.connect('tcp://127.0.0.1:5555')
        except Exception as e:
            log.loginfo.process_log(str(e))

    def zmq_comm(self, msg):
        try:
            #发送数据
            snd = self.socket.send_string(msg)
            #接收数据
            ret = self.socket.recv_string()
            return ret
        except Exception as e:
            log.loginfo.process_log(str(e))
            return ''

    def zmq_close(self):
        self.socket.close()

    def press_one_key(self,group, point):
        self.daqdata = b''
        self.daq.totalmsg = b''
        self.plc.write_shortD("52", group)
        self.plc.write_shortD("54", point)
        self.plc.write_M("228", "1")
        i = 0
        while(True):
            singledone = self.plc.read_M("233")
            if(singledone[0:1] == '1' or i>100):
                self.plc.write_M("233", "0")
                break
            i = i + 1
        # get daq data
        j = 0
        while(True):
            time.sleep(0.01)
            if (('End' in str(self.daq.totalmsg)) or (j > 100)):
                self.daqdata = self.daq.totalmsg
                break
            if(j > 100):
                log.loginfo.process_log('get daq data timeout')
            j = j + 1

        ret_daq = self.daq.process_data(self.daqdata)
        return ret_daq[0]

    def pre_test(self):
        self.capture_image()
        i = 0
        while(True):
            time.sleep(0.01)
            if(self.in_done or i>10):
                break
            i = i + 1
        self.plc.write_intD("492", 3)  # 通知PLC开始测试

        if(self.in_done):
            return [0.2, 'pre']
        else:
            return[0, 'time out']

    def capture_image(self):
        time.sleep(2)
        return [0, 'capture']

    def test_point1(self):
        #self.zmq_comm('readimage')
        ret = self.press_one_key(1, 1)
        data = ret[0:10]
        detail = ['']
        return data+detail

    def test_point2(self):
        #ret = self.zmq_comm('getimagesize')
        ret = self.press_one_key(1, 2)
        data = ret[0:10]
        detail = ['']
        return data + detail

    def test_point3(self):
        ret = self.press_one_key(1, 3)
        data = ret[0:10]
        detail = ['']
        return data + detail

    def test_point4(self):
        ret = self.press_one_key(2, 1)
        data = ret[0:10]
        detail = ['']
        return data + detail

    def test_point5(self):
        ret = self.press_one_key(2, 2)
        data = ret[0:10]
        detail = ['']
        return data + detail

    def test_point6(self):
        ret = self.press_one_key(2, 3)
        data = ret[0:10]
        detail = ['']
        return data + detail

    def post_test(self):
        self.plc.write_intD("490", 3)
        return [0.9, 'post']