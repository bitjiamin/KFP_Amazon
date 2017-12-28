# -*- coding: UTF-8 -*-
"""
FileName: visionscript.py
Author: jiaminbit@sina.com
Create date: 2017.6.20
description: 视觉脚本
Update date：2017.7.20
version 1.0.0
"""

import cv2 as cv
import numpy as np

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ctypes import *
import systempath
import time
import ctypes

class Vision():
    def __init__(self):
        self.cap = None

    def init_window(self,id,row1,col1,row2,col2):
        return True

    def load_image(self):
        return True

    def find_cameras(self, dev):
        cams = []
        return cams

    def open_camera(self, num):
        return True

    def close_camera(self):
        return True

    def snap(self):
        return True