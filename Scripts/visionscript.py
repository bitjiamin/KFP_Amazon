# -*- coding: UTF-8 -*-
"""
FileName: visionscript.py
Author: jiaminbit@sina.com
Create date: 2017.6.20
description: 视觉脚本
Update date：2017.7.20
version 1.0.0
"""


import systempath
import time
import clr
import log

clr.FindAssembly('KFPVisionLib.dll')  # 加载c#dll文件
from KFPVisionLib import *  # 导入命名空间

class Vision():
    #实现一个单例类
    _instance = None
    __first_init = True
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if (self.__class__.__first_init):  # 只初始化一次
            self.__class__.__first_init = False
            self.kfpv = KFPVision()
            if(self.kfpv.open_camera()):
                log.loginfo.process_log('open camera ok')
            else:
                log.loginfo.process_log('open camera fail')
            self.kfpv.set_extime(100000.0)

    def init_window(self,id,row1,col1,row2,col2):
        self.kfpv.init_window(id, row1, col1, row2, col2)

    def convert_to_qimage(self, im, copy=False):
        gray_color_table = [qRgb(i, i, i) for i in range(256)]
        if im is None:
            return QImage()

        if im.dtype == np.uint8:
            if len(im.shape) == 2:
                qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_Indexed8)
                qim.setColorTable(gray_color_table)
                return qim.copy() if copy else qim

            elif len(im.shape) == 3:
                if im.shape[2] == 3:
                    qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_RGB888);
                    return qim.copy() if copy else qim
                elif im.shape[2] == 4:
                    qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_ARGB32);
                    return qim.copy() if copy else qim

    def open_camera(self, num):
        ret = self.kfpv.open_camera()
        return ret

    def close_camera(self):
        ret = self.kfpv.close_camera()
        return ret

    def snap(self):
        self.kfpv.snap()
        self.kfpv.disp_image()