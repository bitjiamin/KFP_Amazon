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
import csv
import time
try:
    import automationscript
except Exception as e:
    log.loginfo.process_log(str(e))
import threading
from visionscript import *
import dataexchange


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
            self.plcthread.start()
            self.in_done = False
            self.zmq_open()
            daqcomm.daq = daqcomm.DAQ()
            self.daq = daqcomm.daq
            self.daq.tcp_connect()
            self.vision = Vision()
            self.testing = False
            self.pointcnt = 6
            # 测试点坐标存放寄存器地址
            self.xd = ['1000', '1002', '1004', '1006', '1008', '1010', '1012', '1014', '1016', '1018']
            self.yd = ['3000', '3002', '3004', '3006', '3008', '3010', '3012', '3014', '3016', '3018']

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
                if(self.testing == False):
                    log.loginfo.process_log(str('dut in done'))
                    self.in_done = True
                    self.plc.write_intD("490", 0)  # reset
                    # capture image
                    #z=2.61,x=288.37,y=37.11
                    capX = 288.37
                    capY = 37.12
                    # start test
                    if(dataexchange.test_mode == 'test'):
                        self.zmq_comm('Start')
                    else:
                        self.zmq_comm('Debug')
                    #self.plc.write_intD("492", 3)  #通知PLC开始测试
                    self.testing = True
            elif(self.state == 3):
                #PLC测试完成
                self.plc.write_intD("490", 0)
                #self.plc.write_intD("492", 4)  #通知PLC，上位机测试完成
                self.plc.write_intD("492", 5)   #通知PLC，上位机测试完成,Pass
                #self.plc.write_intD("492", 6)  # 通知PLC，上位机测试完成,Fail
                self.testing = False

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
        # 打键
        self.plc.write_shortD("52", group)
        self.plc.write_shortD("54", point)
        self.plc.write_M("228", "1")
        i = 0
        while(True):
            singledone = self.plc.read_M("233")
            if(singledone[0:1] == '1' or i>150):
                self.plc.write_M("233", "0")
                break
            time.sleep(0.1)
            i = i + 1
        # get daq data
        j = 0
        while(True):
            if (('End' in str(self.daq.totalmsg)) or (j > 100)):
                self.daqdata = self.daq.totalmsg
                break
            time.sleep(0.03)
            if(j > 100):
                log.loginfo.process_log('get daq data timeout')
            j = j + 1
        ret_daq = self.daq.process_data(self.daqdata)
        return ret_daq

    def get_position(self, point):
        if(self.worldxy != ['']):
            if(point<self.pointcnt/2):
                self.plc.write_intD(self.xd[point], int(self.worldxy[point] * 100))
                self.plc.write_intD(self.yd[point], int(self.worldxy[self.pointcnt - point] * 100))
            else:
                self.plc.write_intD(self.xd[point + 2], int(self.worldxy[point] * 100))
                self.plc.write_intD(self.yd[point + 2], int(self.worldxy[self.pointcnt - point] * 100))
        self.vision.disp_test_point(point)

    def save_rawdata(self, force, displacement, point):
        # 保存波形数据
        savetime = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
        save = inihelper.read_ini(systempath.bundle_dir + '/Config/Config.ini', 'Config', 'SaveData')
        if (save == 'true'):
            filepath = systempath.bundle_dir + '/RawData/' + dataexchange.sn + '-' + savetime + '--point' +str(point) +'.csv'
            f = open(filepath, 'a+', encoding='utf8', newline='')
            writer = csv.writer(f)
            writer.writerow(force)
            writer.writerow(displacement)
            f.close()

    def pre_test(self):
        i = 0
        while(True):
            time.sleep(0.01)
            if(self.in_done or i>10):
                break
            i = i + 1
        self.plc.write_intD("492", 3)  # 通知PLC开始测试

        if(self.in_done):
            self.capture_image()
            return [0.2, 'pre']
        else:
            return[0, 'time out']

    def capture_image(self):
        try:
            self.vision.snap()
            self.worldxy = self.vision.find_test_point()
            self.worldxy = self.worldxy[1:len(self.worldxy)-2]
            self.worldxy = self.worldxy.split(',')
            # 若视觉定位失败，则使用上次测试的坐标值
            if(self.worldxy == ['']):
                xy = self.plc.read_block_intD('1000', 6) + self.plc.read_block_intD('3000', 6)
                self.worldxy = [xy0 / 100 for xy0 in xy]
            for i in range(len(self.worldxy)):
                if(i<int(len(self.worldxy)/2)):
                    self.worldxy[i] = 273.232 + 255.72 - float(self.worldxy[i]) + 288.37 - 170.05
                else:
                    self.worldxy[i] = 28.3567 + 16.27 - float(self.worldxy[i]) + 37.11 - 29.94
        except Exception as e:
            log.loginfo.process_log(str(e))
        return [0, 'capture']

    def test_point1(self):
        self.plc.write_intD("1000", int(self.worldxy[0]*100))
        self.plc.write_intD("3000", int(self.worldxy[6]*100))
        self.vision.disp_test_point(0)
        ret = self.press_one_key(1, 1)
        data = [round(self.worldxy[0],3), round(self.worldxy[6],3)]
        data = data + ret[0]
        dataexchange.points[0] = ret[0]
        dataexchange.displacement[0] = ret[1]
        dataexchange.force[0] = ret[2]

        self.save_rawdata(ret[1], ret[2], 1)

        if(self.worldxy!=['']):
            detail = [str(round(self.worldxy[0],3)) + ', ' + str(round(self.worldxy[6],3))]
        else:
            detail = ['null, null']
        return data+detail

    def test_point2(self):
        self.plc.write_intD("1002", int(self.worldxy[1]*100))
        self.plc.write_intD("3002", int(self.worldxy[7]*100))
        self.vision.disp_test_point(1)
        ret = self.press_one_key(1, 2)
        data = [round(self.worldxy[1],3), round(self.worldxy[7],3)]
        data = data + ret[0]
        dataexchange.points[1] = ret[0]
        dataexchange.displacement[1] = ret[1]
        dataexchange.force[1] = ret[2]

        self.save_rawdata(ret[1], ret[2], 2)

        if (self.worldxy != ['']):
            detail = [str(round(self.worldxy[1], 3)) + ', ' + str(round(self.worldxy[7], 3))]
        else:
            detail = ['null, null']
        return data + detail

    def test_point3(self):
        self.plc.write_intD("1004", int(self.worldxy[2]*100))
        self.plc.write_intD("3004", int(self.worldxy[8]*100))
        self.vision.disp_test_point(2)
        ret = self.press_one_key(1, 3)
        data = [round(self.worldxy[2],3), round(self.worldxy[8],3)]
        data = data + ret[0]
        dataexchange.points[2] = ret[0]

        dataexchange.displacement[2] = ret[1]
        dataexchange.force[2] = ret[2]

        self.save_rawdata(ret[1], ret[2], 3)

        if (self.worldxy != ['']):
            detail = [str(round(self.worldxy[2], 3)) + ', ' + str(round(self.worldxy[8], 3))]
        else:
            detail = ['null, null']
        return data + detail

    def test_point4(self):
        self.plc.write_intD("1010", int(self.worldxy[3]*100))
        self.plc.write_intD("3010", int(self.worldxy[9]*100))
        self.vision.disp_test_point(3)
        ret = self.press_one_key(2, 1)
        data = [round(self.worldxy[3],3), round(self.worldxy[9],3)]
        data = data + ret[0]
        dataexchange.points[3] = ret[0]

        dataexchange.displacement[3] = ret[1]
        dataexchange.force[3] = ret[2]

        self.save_rawdata(ret[1], ret[2], 4)

        if (self.worldxy != ['']):
            detail = [str(round(self.worldxy[3], 3)) + ', ' + str(round(self.worldxy[9], 3))]
        else:
            detail = ['null, null']
        return data + detail

    def test_point5(self):
        self.plc.write_intD("1012", int(self.worldxy[4]*100))
        self.plc.write_intD("3012", int(self.worldxy[10]*100))
        self.vision.disp_test_point(4)
        ret = self.press_one_key(2, 2)
        data = [round(self.worldxy[4],3), round(self.worldxy[10],3)]
        data = data + ret[0]
        dataexchange.points[4] = ret[0]

        dataexchange.displacement[4] = ret[1]
        dataexchange.force[4] = ret[2]

        self.save_rawdata(ret[1], ret[2], 5)

        if (self.worldxy != ['']):
            detail = [str(round(self.worldxy[4], 3)) + ', ' + str(round(self.worldxy[10], 3))]
        else:
            detail = ['null, null']
        return data + detail

    def test_point6(self):
        self.plc.write_intD("1014", int(self.worldxy[5]*100))
        self.plc.write_intD("3014", int(self.worldxy[11]*100))
        self.vision.disp_test_point(5)
        ret = self.press_one_key(2, 3)
        data = [round(self.worldxy[5],3), round(self.worldxy[11],3)]
        data = data + ret[0]
        dataexchange.points[5] = ret[0]

        dataexchange.displacement[5] = ret[1]
        dataexchange.force[5] = ret[2]

        self.save_rawdata(ret[1], ret[2], 6)

        if (self.worldxy != ['']):
            detail = [str(round(self.worldxy[5], 3)) + ', ' + str(round(self.worldxy[11], 3))]
        else:
            detail = ['null, null']
        return data + detail

    def post_test(self):
        self.plc.write_intD("490", 3)
        return [0.9, 'post']