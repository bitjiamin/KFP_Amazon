from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from editsequence import *
import load
import systempath
import csv
import log
import testthread

class EditThread(Ui_editsequence, QDialog):
    def __init__(self, parent=None):
        super(EditThread, self).__init__(parent)
        self.setupUi(self)
        # 获取屏幕分辨率
        self.screen = QDesktopWidget().screenGeometry()
        self.width = self.screen.width()
        self.height = self.screen.height()
        self.init_seq()
        self.connect_signal()
        # 加载sequence
        self.edit_sequence()

        # 初始化编辑测试序列的表格

    def init_seq(self):
        self.cb_seq.clear()
        for i in range(load.threadnum):
            self.cb_seq.addItem('Sequence' + str(i+1))

        log.loginfo.process_log('Initialize sequence table')
        self.tableseq.setRowCount(1000)
        self.tableseq.setColumnCount(7)
        self.tableseq.setHorizontalHeaderLabels(
            ['TestItem', 'Function', 'Mode', 'Low Limit', 'Up Limit', 'Next Step', 'Level'])
        self.tableseq.setColumnWidth(0, self.width * 0.3)
        self.tableseq.setColumnWidth(1, self.width * 0.1)
        self.tableseq.horizontalHeader().setStretchLastSection(True)
        self.pb_saveseq.setMaximumWidth(self.width * 0.08)
        self.cb_seq.setMaximumWidth(self.width * 0.08)
        self.pb_delrow.setMaximumWidth(self.width * 0.08)
        self.pb_insertrow.setMaximumWidth(self.width * 0.08)

    def English_ui(self):
        # 序列编辑
        self.lb_edit.setText('Edit Test Sequence')
        self.pb_insertrow.setText('Insert Row')
        self.pb_delrow.setText('Delete Row')
        self.pb_saveseq.setText('Save')
        self.tableseq.setHorizontalHeaderLabels(
            ['TestItem', 'Function', 'Mode', 'Low Limit', 'Up Limit', 'Next Step', 'Level'])

    def Chinese_ui(self):
        # 序列编辑
        self.lb_edit.setText('序列编辑')
        self.pb_insertrow.setText('插入行')
        self.pb_delrow.setText('删除选定行')
        self.pb_saveseq.setText('保存序列')
        self.tableseq.setHorizontalHeaderLabels(['测试项', '函数', '模式', '下限', '上限', '失败后跳转', '等级'])

    def change_language(self):
        if (self.language.currentIndex() == 0):
            self.English_ui()
        else:
            self.Chinese_ui()

    def connect_signal(self):
        self.cb_seq.currentIndexChanged.connect(self.edit_sequence)
        self.pb_saveseq.clicked.connect(self.save_sequence)
        self.pb_delrow.clicked.connect(self.delete_row)
        self.pb_insertrow.clicked.connect(self.insert_row)

        # 连接运动控制相关函数
        # self.pb_jog1.pressed.connect(self.jog_forward)
        # self.pb_jog1.released.connect(self.axis_stop)
        # self.pb_jog2.pressed.connect(self.jog_backward)
        # self.pb_jog2.released.connect(self.axis_stop)
        # self.pb_absolute.clicked.connect(self.absolute_run)
        # self.pb_relative.clicked.connect(self.relative_run)
        # self.cb_axis.currentIndexChanged.connect(self.change_axis)
        # self.pb_reset.clicked.connect(self.axis_reset)

    # 切换到序列编辑页面，并且将Seq1的信息读取到表格
    def edit_sequence(self):
        #self.tableseq.clear()
        ld = testthread.t_load[self.cb_seq.currentIndex()]

        ld.load_seq()

        items = [ld.seq_col1, ld.seq_col2, ld.seq_col3, ld.seq_col4, ld.seq_col5, ld.seq_col6, ld.seq_col7]
        for j in range(7):
            i = 0
            for seq in items[j][1:len(items[j])]:
                if(j==20000):
                    self.MyCombo = QComboBox()
                    self.MyCombo.addItem("test")
                    self.MyCombo.addItem("skip")
                    self.tableseq.setCellWidget(i, j, self.MyCombo)
                    if(seq == 'test'):
                        self.MyCombo.setCurrentIndex(0)
                    else:
                        self.MyCombo.setCurrentIndex(1)
                elif(j==50000):
                    self.MyCombo1 = QComboBox()
                    self.MyCombo1.addItem("continue")
                    self.MyCombo1.addItem("finish")
                    self.tableseq.setCellWidget(i, j, self.MyCombo1)
                    if (seq == 'continue'):
                        self.MyCombo1.setCurrentIndex(0)
                    else:
                        self.MyCombo1.setCurrentIndex(1)
                elif (j == 60000):
                    self.MyCombo2 = QComboBox()
                    self.MyCombo2.addItem("root")
                    self.MyCombo2.addItem("child")
                    self.tableseq.setCellWidget(i, j, self.MyCombo2)
                    if (seq == 'root'):
                        self.MyCombo2.setCurrentIndex(0)
                    else:
                        self.MyCombo2.setCurrentIndex(1)
                else:
                    newItem1 = QTableWidgetItem(seq)
                    self.tableseq.setItem(i, j, newItem1)
                i = i + 1

    # 保存测试序列信息
    def save_sequence(self):
        filepath = systempath.bundle_dir + '/CSV Files/Seq' + str(self.cb_seq.currentIndex()+1) + '.csv'

        f = open(filepath, 'w',encoding='utf8',newline='')
        writer = csv.writer(f)
        writer.writerow(['TestItem', 'Function', 'Mode', 'Low Limit', 'Up Limit', 'Next Step', 'Level'])
        try:
            for i in range(1000):
                row = []
                if (self.tableseq.item(i, 0) != None):
                    for j in range(7):
                        if(j==20000):
                            if(self.tableseq.cellWidget(i, j).currentIndex()==0):
                                row.append('test')
                            else:
                                row.append('skip')
                        elif(j==500000):
                            if (self.tableseq.cellWidget(i, j).currentIndex() == 0):
                                row.append('continue')
                            else:
                                row.append('finish')
                        elif(j==60000):
                            if (self.tableseq.cellWidget(i, j).currentIndex() == 0):
                                row.append('root')
                            else:
                                row.append('child')
                        else:
                            row.append(self.tableseq.item(i,j).text())
                    writer.writerow(row)
        except Exception as e:
            log.loginfo.process_log(str(e))
        f.close()
        #self.load_sequence()

    # 删除当前行
    def delete_row(self):
        self.tableseq.removeRow(self.tableseq.currentRow())

    def insert_row(self):
        row_cnt = self.tableseq.currentRow()
        self.tableseq.insertRow(row_cnt)
        for j in range(7):
                if(j==2):
                    self.MyCombo = QComboBox()
                    self.MyCombo.addItem("test")
                    self.MyCombo.addItem("skip")
                    self.tableseq.setCellWidget(row_cnt, j, self.MyCombo)
                elif(j==5):
                    self.MyCombo1 = QComboBox()
                    self.MyCombo1.addItem("continue")
                    self.MyCombo1.addItem("finish")
                    self.tableseq.setCellWidget(row_cnt, j, self.MyCombo1)
                elif (j == 6):
                    self.MyCombo2 = QComboBox()
                    self.MyCombo2.addItem("root")
                    self.MyCombo2.addItem("child")
                    self.tableseq.setCellWidget(row_cnt, j, self.MyCombo2)
                else:
                    newItem1 = QTableWidgetItem('')
                    self.tableseq.setItem(row_cnt, j, newItem1)