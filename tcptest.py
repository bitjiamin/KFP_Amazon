# -*- coding: utf-8 -*-
import socket

socket.setdefaulttimeout(1)
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con_ok = skt.connect(('169.254.142.39', 5010))
print(con_ok)
msg='500000FF03FF000018001004010001M*0000970008'
skt.send(msg.encode())
ret = skt.recv(100).decode()
print(ret)

