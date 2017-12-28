# coding=utf-8

# clr是公共运行时环境，这个模块是与C#交互的核心
import clr
import sys
# 导入clr时这个模块最好也一起导入，这样就可以用AddReference方法
import System
import time

clr.FindAssembly('MyDll.dll')  # 加载c#dll文件
from MyDll import *  # 导入命名空间

my = MyClass()

print(my.add('a', 'b')[0])
my.LoadSettings()
my.InitServer(0)

my.InitResource('asdf', 0)
#kfp = KFPVision()
#open = kfp.open_camera()
#print(open)
#time.sleep(0.5)
#close = kfp.close_camera()
#rint(close)

class Test():
    _instance = None
    __first_init = True
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    count = 0
    def __init__(self):
        if(self.__class__.__first_init):
            print('init')
            Test.count = Test.count + 1
            self.data = 1
            self.__class__.__first_init = False

