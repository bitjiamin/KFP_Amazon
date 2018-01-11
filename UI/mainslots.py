from automation import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import load
from visionscript import *
from automationscript import *
import daqcomm
import dataexchange
import plccomm
from mainsetup import *


class MainSlots(MainUI):
    def __init__(self, parent=None):
        super(MainSlots, self).__init__(parent)
        self.actionWaveform.triggered.connect(self.check_wave)
        self.init_wave()
        self.total_cnt = []
        self.pass_cnt = []
        self.y_cnt = []
        for i in range(load.threadnum):
            self.total_cnt.append(0)
            self.pass_cnt.append(0)
            self.y_cnt.append(0)
            self.info[i].itemChanged.connect(self.info_changed)

        # 实例化信号槽需要用到的类
        # init image window with halcon
        daqcomm.daq.refreshwave.connect(self.refresh_wave)

    def showEvent(self, e):
        try:
            self.vision = Vision()
            self.auto = AutoMation()
            self.auto.plc_para1.start()
            self.auto.plc_error.start()
            self.pb_snap.clicked.connect(self.vision.snap)
            self.pb_reset.clicked.connect(self.auto.system_reset)
            self.cb_debug.clicked.connect(self.set_test_mode)
            if (self.vision.kfpv.open_camera()):
                log.loginfo.process_log('open camera ok')
            else:
                log.loginfo.process_log('open camera fail')
            self.vision.kfpv.set_extime(150000.0)
            pass
        except Exception as e:
            print(e)

    def set_test_mode(self):
        if(self.cb_debug.isChecked()):
            dataexchange.test_mode = 'debug'
            print(dataexchange.test_mode)
        else:
            dataexchange.test_mode = 'test'
            print(dataexchange.test_mode)

    def resizeEvent(self, event):
        if(self.lb_image.height()>self.height*0.3):
            try:
                self.vision.init_window(int(self.lb_image.winId()), 0, 0, self.lb_image.width(), self.lb_image.height())
                pass
            except Exception as e:
                print(e)
            pass

    def check_wave(self):
        try:
            plt.figure(figsize = (10,5))
            plt.title('Waveform')
            #plt.subplots_adjust(left=0.2, bottom=0.2, right=0.3, top=0.3)
            plt.xlabel('displacement')
            plt.ylabel('force')
            plt.subplot(2, 3, 1)
            plt.plot(dataexchange.displacement[0], dataexchange.force[0])
            x = [dataexchange.points[0][6], dataexchange.points[0][7], dataexchange.points[0][8], dataexchange.points[0][9]]
            y = [dataexchange.points[0][0], dataexchange.points[0][1], dataexchange.points[0][4], dataexchange.points[0][5]]
            plt.plot(x,y,'.r')
            plt.subplot(2, 3, 2)
            plt.plot(dataexchange.displacement[1], dataexchange.force[1])
            x = [dataexchange.points[1][6], dataexchange.points[1][7], dataexchange.points[1][8],
                 dataexchange.points[1][9]]
            y = [dataexchange.points[1][0], dataexchange.points[1][1], dataexchange.points[1][4],
                 dataexchange.points[1][5]]
            plt.plot(x, y, '.r')
            plt.subplot(2, 3, 3)
            plt.plot(dataexchange.displacement[2], dataexchange.force[2])
            x = [dataexchange.points[2][6], dataexchange.points[2][7], dataexchange.points[2][8],
                 dataexchange.points[2][9]]
            y = [dataexchange.points[2][0], dataexchange.points[2][1], dataexchange.points[2][4],
                 dataexchange.points[2][5]]
            plt.plot(x, y, '.r')
            plt.subplot(2, 3, 4)
            plt.plot(dataexchange.displacement[3], dataexchange.force[3])
            x = [dataexchange.points[3][6], dataexchange.points[3][7], dataexchange.points[3][8],
                 dataexchange.points[3][9]]
            y = [dataexchange.points[3][0], dataexchange.points[3][1], dataexchange.points[3][4],
                 dataexchange.points[3][5]]
            plt.plot(x, y, '.r')
            plt.subplot(2, 3, 5)
            plt.plot(dataexchange.displacement[4], dataexchange.force[4])
            x = [dataexchange.points[4][6], dataexchange.points[4][7], dataexchange.points[4][8],
                 dataexchange.points[4][9]]
            y = [dataexchange.points[4][0], dataexchange.points[4][1], dataexchange.points[4][4],
                 dataexchange.points[4][5]]
            plt.plot(x, y, '.r')
            plt.subplot(2, 3, 6)
            plt.plot(dataexchange.displacement[5], dataexchange.force[5])
            x = [dataexchange.points[5][6], dataexchange.points[5][7], dataexchange.points[5][8],
                 dataexchange.points[5][9]]
            y = [dataexchange.points[5][0], dataexchange.points[5][1], dataexchange.points[5][4],
                 dataexchange.points[5][5]]
            plt.plot(x, y, '.r')
            plt.show()
        except Exception as e:
            log.loginfo.process_log(str(e))

    def init_wave(self):
        print('asfasdf')
        # a figure instance to plot on
        self.figure = Figure()
        self.figure.subplots_adjust(left=0.14, bottom=0.14, right=0.9, top=0.9)
        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        self.imagewave.addWidget(self.canvas)
        self.imagewave.setRowStretch(0, 1)
        self.imagewave.setRowStretch(1, 1)
        ''' plot some random stuff '''
        # random data
        #import random
        #import math
        #data = [random.random() for i in range(10)]
        #x0 = math.pi/5
        #x = [-5*x0, -4*x0, -3*x0, -2*x0, -x0, 0, x0, 2*x0, 3*x0, 4*x0, 5*x0]
        #y = []
        #for x1 in x:
            #y0 = math.sin(x1)
            #y.append(y0)
        # create an axis
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlabel('Displacement')
        self.ax.set_ylabel('Force')
        self.ax.set_xlim(0,0.6)
        self.ax.set_autoscalex_on(False)
        self.ax.set_autoscaley_on(False)
        self.ax.set_ylim(0, 400)

        # discards the old graph
        #self.ax.clear()
        # plot data
        #self.ax.plot(x, y, '.-')
        # refresh canvas
        #self.canvas.draw()

    def refresh_wave(self,xy):
        try:
            self.ax.clear()
            # plot data
            self.ax.plot(xy[0], xy[1], '-')
            x = [xy[2][6],xy[2][7], xy[2][8], xy[2][9]]
            y = [xy[2][0],xy[2][1], xy[2][4], xy[2][5]]
            self.ax.plot(x, y, '.r')
            self.ax.set_xlim(0, 0.5)
            self.ax.set_ylim(0, 300)
            # refresh canvas
            self.canvas.draw()
        except Exception as e:
            print(e)


    def info_changed(self, item):
        if(item.row()==5 and item.column()==1):
            dataexchange.sn = item.text()
            if(len(dataexchange.sn)>5):
                plccomm.plc.write_intD("492", 1)  # scan ok, start dut in

    def set_state(self, result, thread_id):
        # 设置系统测试状态
        newItem = QTableWidgetItem(result)
        self.info[thread_id].setItem(0, 1, newItem)
        if(result=='Testing'):
            newItem.setBackground(QColor(255,255,0))
        elif (result == 'Fail'):
            newItem.setBackground(QColor(255, 0, 0))
        elif (result == 'Pass'):
            newItem.setBackground(QColor(0, 255, 0))

    def set_count(self, ls):
        thread_id = ls[2]
        newItem = QTableWidgetItem(str(round(ls[0], 2)))
        self.info[thread_id].setItem(4, 1, newItem)
        # 统计测试个数及通过率
        self.total_cnt[thread_id] = int(self.info[thread_id].item(1, 1).text()) + 1
        newItem = QTableWidgetItem(str(self.total_cnt[thread_id]))
        self.info[thread_id].setItem(1, 1, newItem)
        if (ls[1] == 'Pass'):
            self.pass_cnt[thread_id] = int(self.info[thread_id].item(2, 1).text()) + 1
            newItem = QTableWidgetItem(str(self.pass_cnt[thread_id]))
            self.info[thread_id].setItem(2, 1, newItem)
        self.y_cnt[thread_id] = self.pass_cnt[thread_id] / self.total_cnt[thread_id]
        newItem = QTableWidgetItem(str("%.2f" % (self.y_cnt[thread_id] * 100)) + '%')
        self.info[thread_id].setItem(3, 1, newItem)