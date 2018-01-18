# -*- coding: UTF-8 -*-
"""
FileName: tcptool.py
Author: jiaminbit@sina.com
Create date: 2017.6.20
description: tcp调试工具
Update date：2017.7.20
version 1.0.0
"""

import socket
import threading
import time
import struct
from PyQt5 import QtCore
import log
import dataexchange
import inihelper
import systempath

global daq
socket.setdefaulttimeout(0.2)
class DAQ(QtCore.QThread):
    refreshwave = QtCore.pyqtSignal(list)
    def __init__(self, parent = None):
        super(DAQ, self).__init__(parent)
        self.ip = '169.254.142.68'
        self.port = 8888
        self.totalmsg = b''

    def tcp_connect(self):
        self.skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.skt.settimeout(0.1)
        try:
            con_ok = self.skt.connect((self.ip, self.port))
            print(con_ok)
            if(con_ok == None):
                k = float(inihelper.read_ini(systempath.bundle_dir + '/Config/Calibration.ini', 'Calibration', 'k'))
                self.send_cal_cmd()
                self.write_calibration(k)
                log.loginfo.process_log('connect daq ok')
                self.recv_thread = threading.Thread(target=self.tcp_recv)
                self.recv_thread.setDaemon(True)
                self.recv_thread.start()
            else:
                log.loginfo.process_log('connect daq fail')
        except Exception as e:
            print(e)
            log.loginfo.process_log(str(e))

    def tcp_send(self,sendmsg):
        try:
            self.skt.send(sendmsg.encode())
        except Exception as e:
            log.loginfo.process_log(str(e))

    def send_cal_cmd(self):
        print('send')
        sendmsg = b'\x0B\x00\x00\x00\x4B\x46\x50\x5F\x43\x41\x4C'
        self.skt.send(sendmsg)

    def tcp_recv(self):
        i = 0
        while(True):
            try:
                if(True):
                    recvmsg = self.skt.recv(1024)
                    print ("------------------------------")
                    print (recvmsg)
                    if ('OK' in str(recvmsg)):
                        print(recvmsg)
                    if ('CAL' in str(recvmsg)):
                        f1 = struct.unpack('<f', recvmsg[7:11])[0]
                        f2 = struct.unpack('<f', recvmsg[11:15])[0]
                        dataexchange.daqcal1[i] = f1
                        dataexchange.daqcal2[i] = f2
                        i = i + 1
                        if(i == 15):
                            i = 0
                    self.totalmsg = self.totalmsg + recvmsg
            except Exception as e:
                pass
                #log.loginfo.process_log(str(e))

    def process_data(self, data):
        try:
            # 获取数据长度
            l_data = struct.unpack('<i',data[0:4])[0]
            log.loginfo.process_log('Package length:' + str(l_data))
            s_start = str(data[4:19])[1:]
            l_force1 = struct.unpack('<i',data[19:23])[0]
            log.loginfo.process_log('Data length:' + str(l_force1))
            l_force2 = struct.unpack('<i', data[23:27])[0]
            # print('l_force2:',l_force2)
            # 特征点
            point1=[]
            for i in range(20):
                point = struct.unpack('<f', data[27+4*i:31+4*i])[0]
                point = round(point, 3)
                point1.append(point)
            #print('point1:', point1)
            #force signal,[87:]
            force=[]
            for i in range(l_force1):
                force0 = struct.unpack('<f', data[107+4*i:111+4*i])[0]
                #force0 = round(force0, 2)
                force.append(force0)
            #displace
            displace = []
            for i in range(l_force1):
                displace0 = struct.unpack('<f', data[107 + 4 * l_force1 + 4*i:111 + 4 * l_force1 + 4*i])[0]
                #displace0 = round(displace0, 4)
                displace.append(displace0)
            # self.refreshwave.emit([displace, force, point1])
            return [point1, displace, force]
        except Exception as e:
            log.loginfo.process_log(str(e))
            ret = []
            for i in range(20):
                ret.append(-1)
            return [ret,[-1],[-1]]

    def write_calibration(self, k):
        Data = [k, 1000, 0.001, 1, 0, 20, 250, 250, 10000]
        # CHJ[ForceSlope,FilterLowpass,PositionSlope,Filter(unuser), GetRaw, RIOlow, RIOHigh, High1(unuser), SampleFreq
        cmdData = "".encode()
        for d in Data:
            if d == Data[len(Data) - 1]:
                cmdData = cmdData + struct.pack("<f", d)
            else:
                cmdData = cmdData + struct.pack("<f", d) + ",".encode()
        cmd = struct.pack("<i", 60) + "KFP_DAQSET{".encode() + cmdData + "}".encode()
        try:
            self.skt.send(cmd)
        except Exception as e:
            log.loginfo.process_log(str(e))