# -*- coding: utf-8 -*-
import socket
import log
import time
import threading
import dataexchange


global plc
socket.setdefaulttimeout(2)
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
l = threading.Lock()

class PlcCom():
    def __init__(self):
        pass

    def tcp_connect(self):
        con_ok = skt.connect(('169.254.142.39', 5010))
        if (con_ok == None):
            log.loginfo.process_log('plc connect ok')
            dataexchange.plcconn = True
        else:
            skt.close()
            log.loginfo.process_log('plc connect fail')
            dataexchange.plcconn = False

    def send_and_recv(self, msg, cnt):
        l.acquire()
        try:
            skt.send(msg.encode())
        except Exception as e:
            log.loginfo.process_log(str(e))
        try:
            recvmsg = skt.recv(cnt).decode()
        except Exception as e:
            log.loginfo.process_log(str(e))
        l.release()  # 释放锁
        return recvmsg

    def tcp_close(self):
        try:
            skt.close()
            log.loginfo.process_log('close plc connect')
        except Exception as e:
            log.loginfo.process_log(str(e))

    #'500000FF03FF000020001014010001M*000104000800000000'
    def write_M(self, m, data):
        old = self.read_M(m)[1:8]
        head = '500000FF03FF000020001014010001'
        m = m.zfill(6)
        id = 'M*' + m
        msg = head + id + '0008' + data + old
        recv = self.send_and_recv(msg, 100)
        return True

    def read_M(self, m):
        try:
            head = '500000FF03FF000018001004010001'
            m = m.zfill(6)
            id = 'M*' + m
            s_size = hex(8)[2:]
            if (len(s_size) > 4):
                return ''
            s_size = s_size.zfill(4)
            msg = head + id + s_size;
            recv = self.send_and_recv(msg, 500)
        except Exception as e:
            log.loginfo.process_log(str(e))
            recv = '000000000'
        return recv[22:30]

    def read_blockM(self, m, size):
        try:
            head = '500000FF03FF000018001004010001'
            m = m.zfill(6)
            id = 'M*' + m
            s_size = hex(size)[2:]
            if (len(s_size) > 4):
                return ''
            s_size = s_size.zfill(4)
            msg = head + id + s_size;
            recv = self.send_and_recv(msg, 500)
            return recv[22:22+size]
        except Exception as e:
            return '0'.zfill(size)

    def write_shortD(self, d,data):
        head = '500000FF03FF00001C001014010000'
        d = d.zfill(6)
        id = 'D*' + d
        s_data = hex(data)[2:]
        if (len(s_data) > 4):
            return False;
        s_data = s_data.zfill(4)
        msg = head + id + '0001' + s_data
        recv = self.send_and_recv(msg, 100)
        if (recv == 'D00000FF03FF0000040000'):
            return True
        else:
            return False

    def write_intD(self, d, data):
        head = '500000FF03FF000020001014010000'
        d = d.zfill(6)
        id = 'D*' + d
        s_data = hex(data)[2:]
        if (len(s_data) > 8):
            return False
        s_data = s_data.zfill(8)

        msg = head + id + '0002' + s_data[4:8] + s_data[0:4]
        recv = self.send_and_recv(msg, 100)
        if (recv == 'D00000FF03FF0000040000'):
            return True
        else:
            return False

    def read_block_intD(self, d, size):
        head = '500000FF03FF000018001004010000'
        d=d.zfill(6)
        id = 'D*' + d
        s_size = hex(size)[2:]
        if (len(s_size) > 4):
            return ''
        s_size = s_size.zfill(4)
        msg = head + id + s_size
        try:
            ret = []
            recv = self.send_and_recv(msg, size * 4 + 100)
            for i in range(int(size / 2)):
                sub = recv[22 + 4 * (2 * i + 1): 26 + 4 * (2 * i + 1)] + recv[22 + 8 * i:26 + 8 * i]
                if(int(sub, 16)>2**31):
                    ret.append(int(sub, 16)-2**32)
                else:
                    ret.append(int(sub, 16))
            return ret
        except Exception as e:
            ret1 = []
            for i in range(int(size / 2)):
                ret1.append(0)
            return ret1

    def read_shortD(self, d):
        try:
            head = '500000FF03FF000018001004010000'
            d = d.zfill(6)
            id = 'D*' + d
            msg = head + id + '0001'
            recv = self.send_and_recv(msg, 100)
            ret = int(recv[22:26], 16)
            return ret
        except Exception as e:
            return 0