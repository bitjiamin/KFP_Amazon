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
import systempath
import threading

class MainSlots(MainUI):
    def __init__(self, parent=None):
        super(MainSlots, self).__init__(parent)
        self.actionWaveform.triggered.connect(self.check_wave_thread)
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
        self.load1 = load.Load('Seq1.csv')
        self.load1.load_seq()
        self.lowall =  self.load1.seq_col4
        self.upall = self.load1.seq_col5
        index = [5,6,9,10,11,12,13,14]
        self.up = [[],[],[],[],[],[]]
        self.low = [[],[],[],[],[],[]]
        for j in range(6):
            for i in index:
                self.low[j].append(float(self.load1.seq_col4[i + j*23]))
                self.up[j].append(float(self.load1.seq_col5[i + j*23]))

    def plot_limit(self, point):
        l = int(len(self.low[point-1])/2)
        for i in range(l):
            x = [self.low[point-1][i], self.up[point-1][i], self.up[point-1][i], self.low[point-1][i], self.low[point-1][i]]
            y = [self.low[point-1][i + l], self.low[point-1][i + l], self.up[point-1][i + l], self.up[point-1][i + l], self.low[point-1][i + l]]
            color = ['-r','-g','-b','-r','-g','-b']
            self.ax.plot(y, x, '-r',alpha=0.5)

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
            self.vision.kfpv.set_extime(180000.0)
            pass
        except Exception as e:
            print(e)

    def set_test_mode(self):
        if(self.cb_debug.isChecked()):
            dataexchange.test_mode = 'debug'
        else:
            dataexchange.test_mode = 'test'

    def resizeEvent(self, event):
        if(self.lb_image.height()>self.height*0.3):
            try:
                self.vision.init_window(int(self.lb_image.winId()), 0, 0, self.lb_image.width(), self.lb_image.height())
                pass
            except Exception as e:
                print(e)
            pass

    def check_wave_thread(self):
        self.wave = threading.Thread(target=self.check_wave)
        self.wave.setDaemon(True)
        self.wave.start()

    def check_wave(self):
        try:
            plt.figure(figsize = (10,5))
            plt.title('Waveform')
            #plt.subplots_adjust(left=0.2, bottom=0.2, right=0.3, top=0.3)
            plt.xlabel('displacement')
            plt.ylabel('force')
            plt.subplot(2, 3, 1)
            plt.plot(dataexchange.displacement[0][1:], dataexchange.force[0][1:])
            x = [dataexchange.points[0][6], dataexchange.points[0][7], dataexchange.points[0][8], dataexchange.points[0][9]]
            y = [dataexchange.points[0][0], dataexchange.points[0][1], dataexchange.points[0][4], dataexchange.points[0][5]]
            plt.plot(x,y,'.r')
            plt.subplot(2, 3, 2)
            plt.plot(dataexchange.displacement[1][1:], dataexchange.force[1][1:])
            x = [dataexchange.points[1][6], dataexchange.points[1][7], dataexchange.points[1][8],
                 dataexchange.points[1][9]]
            y = [dataexchange.points[1][0], dataexchange.points[1][1], dataexchange.points[1][4],
                 dataexchange.points[1][5]]
            plt.plot(x, y, '.r')
            plt.subplot(2, 3, 3)
            plt.plot(dataexchange.displacement[2][1:], dataexchange.force[2][1:])
            x = [dataexchange.points[2][6], dataexchange.points[2][7], dataexchange.points[2][8],
                 dataexchange.points[2][9]]
            y = [dataexchange.points[2][0], dataexchange.points[2][1], dataexchange.points[2][4],
                 dataexchange.points[2][5]]
            plt.plot(x, y, '.r')
            plt.subplot(2, 3, 4)
            plt.plot(dataexchange.displacement[3][1:], dataexchange.force[3][1:])
            x = [dataexchange.points[3][6], dataexchange.points[3][7], dataexchange.points[3][8],
                 dataexchange.points[3][9]]
            y = [dataexchange.points[3][0], dataexchange.points[3][1], dataexchange.points[3][4],
                 dataexchange.points[3][5]]
            plt.plot(x, y, '.r')
            plt.subplot(2, 3, 5)
            plt.plot(dataexchange.displacement[4][1:], dataexchange.force[4][1:])
            x = [dataexchange.points[4][6], dataexchange.points[4][7], dataexchange.points[4][8],
                 dataexchange.points[4][9]]
            y = [dataexchange.points[4][0], dataexchange.points[4][1], dataexchange.points[4][4],
                 dataexchange.points[4][5]]
            plt.plot(x, y, '.r')
            plt.subplot(2, 3, 6)
            plt.plot(dataexchange.displacement[5][1:], dataexchange.force[5][1:])
            x = [dataexchange.points[5][6], dataexchange.points[5][7], dataexchange.points[5][8],
                 dataexchange.points[5][9]]
            y = [dataexchange.points[5][0], dataexchange.points[5][1], dataexchange.points[5][4],
                 dataexchange.points[5][5]]
            plt.plot(x, y, '.r')
            plt.show()
        except Exception as e:
            log.loginfo.process_log(str(e))

    def init_wave(self):
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
        # create an axis
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlabel('Displacement(mm)')
        self.ax.set_ylabel('Force(g)')
        self.ax.set_autoscalex_on(False)
        self.ax.set_autoscaley_on(False)

    def refresh_wave(self,xy):
        try:
            self.ax.clear()
            self.ax.set_xlabel('Displacement(mm)')
            self.ax.set_ylabel('Force(g)')
            # plot data
            index = xy[1].index(max(xy[1]))
            self.ax.plot(xy[0][0:index], xy[1][0:index], '-g')
            self.ax.plot(xy[0][index:], xy[1][index:], '-b')
            x = [xy[2][6],xy[2][7], xy[2][8], xy[2][9]]
            y = [xy[2][0],xy[2][1], xy[2][4], xy[2][5]]
            self.ax.text(0.02,250,'Point' + str(dataexchange.testpoint),fontsize=10)
            self.ax.plot(x, y, '.r')
            #SetLimit Arrry
            # self.ax.plot(x, y, marker="o",markersize=20,alpha=0.2)
            self.plot_limit(dataexchange.testpoint)
            self.ax.set_xlim(0, 0.5)
            self.ax.set_ylim(0, 300)
            # refresh canvas
            self.canvas.draw()
        except Exception as e:
            pass

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
        self.info[0].item(5,1).setText('')