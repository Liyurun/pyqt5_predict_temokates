import math
import os
import random
import numpy as np
from PyQt5.QtGui import QPalette, QPixmap, QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QListWidgetItem, QAbstractItemView, \
    QTableWidgetItem, QGraphicsScene, QGraphicsPixmapItem, QSlider, QFileDialog
from PyQt5.QtCore import Qt, QPoint
from PyQt5 import uic
from PyQt5 import QtWidgets
# import cv2
from main import Ui_MainWindow


class Stats(QMainWindow, Ui_MainWindow):

    def __init__(self):
        # 从文件中加载UI定义
        super(Stats,self).__init__()
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        # self.ui = Ui_MainWindow()  # uic.loadUi("main.ui")
        self.setupUi(self)
        self.start()
        # tab1
        self.pushButton_2.clicked.connect(self.tab1_daoru)
        self.pushButton.clicked.connect(self.tab1_jisuan)

        # tab2
        self.pushButton_3.clicked.connect(self.tab2_tianjia1)
        self.pushButton_4.clicked.connect(self.tab2_daoru)
        self.pushButton_5.clicked.connect(self.tab2_tianjia2)
        self.pushButton_10.clicked.connect(self.tab2_jisuan)

        # tab3
        self.filename_ls = os.listdir('./fig')
        self.pushButton_11.clicked.connect(self.tab3_liulan)
        self.pushButton_8.clicked.connect(self.tab3_tianjia1)
        self.pushButton_7.clicked.connect(self.tab3_qidian)
        self.pushButton_6.clicked.connect(self.tab3_zhongdian)
        self.pushButton_9.clicked.connect(self.tab3_tianjia2)
        self.tab3_get_parameter()



        # self.ui.pushButton.clicked.connect(self.handleCalc)

    def start(self):
        #tab1
        well_name = ['H1-1','H1-2','H1-3','H1-4','H1-5','H1-6','H1-7','H1-8','H1-9','H1-10']
        self.listWidget.addItems(well_name)
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)  #设置多选

        #tab2
        well_name1 = ['H1-1','H1-2','H1-3','H1-4']
        well_name2 = ['H1-6','H1-7','H1-8','H1-9','H1-10']
        self.listWidget1.addItems(well_name1)

        self.listWidget_2.addItems(well_name2)
        self.listWidget_2.setSelectionMode(QAbstractItemView.ExtendedSelection)  # 设置多选

        # tab3
        #Qsilder
        self.horizontalSlider_2.setMinimum(5)
        self.horizontalSlider_2.setMaximum(50)
        self.horizontalSlider_2.setSingleStep(5)
        self.horizontalSlider_2.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_2.setTickInterval(5)
        self.horizontalSlider_2.valueChanged.connect(self.tab3_silder1_changed)
        self.lineEdit_3.setReadOnly(True)

        self.pix = QPixmap()
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(1500)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.valueChanged.connect(self.tab3_silder2_changed)

    def tab1_daoru(self):

        text_list = self.listWidget.selectedItems()
        text_ls = [ti.text() for ti in text_list]
        well_num = len(text_list)
        print([ls.text() for ls in text_list])

        # table widgets
        header_la = ['井号','渗透率','非均质程度','有效厚度','孔隙度','低水强度','注采井距','产气量与注气量之比','生产气油比','注气压力变化特征','产出气组分变化','原油粘度']
        data_base = dict()
        data_base['H1-1'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        data_base['H1-2'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        data_base['H1-3'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        data_base['H1-4'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        data_base['H1-5'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        data_base['H1-6'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        data_base['H1-7'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        data_base['H1-8'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        data_base['H1-9'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        data_base['H1-10'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

        count = 0
        if self.checkBox.isChecked():
            header_la.append('示踪剂速度')
            count += 1
        if self.checkBox_2.isChecked():
            header_la.append('PI指数')
            count += 1
        if self.checkBox_3.isChecked():
            header_la.append('试井结果')
            count += 1
        self.tableWidget.setRowCount(well_num)
        self.tableWidget.setColumnCount(12+count)
        self.tableWidget.setHorizontalHeaderLabels(header_la)   #q1
        col_count = 0
        for ti in text_ls:
            if data_base[ti]:
                self.tableWidget.setItem(col_count, 0, QTableWidgetItem(str(ti)))
                for i,xi in enumerate(data_base[ti]):
                    self.tableWidget.setItem(col_count,i+1,QTableWidgetItem(str(xi)))
            col_count += 1
        # self.tableWidget.setItem(1,0,QTableWidgetItem('a'))
    def tab1_jisuan(self):
        # self.tableWidget. #q1 read
        text_list = self.listWidget.selectedItems()
        text_ls = [ti.text() for ti in text_list]
        well_num = len(text_list)
        self.tableWidget_2.setRowCount(well_num)
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setHorizontalHeaderLabels(['井号','决策因子'])

        for i,xi in enumerate(text_ls):
            self.tableWidget_2.setItem(i, 0, QTableWidgetItem(str(xi)))
            self.tableWidget_2.setItem(i, 1, QTableWidgetItem('0.1'))

    def tab2_tianjia1(self):
        # self.accept_new_well()  #接受新的井名和数据    #q2


        self.listWidget1.addItems('new_in_well')
    def tab2_tianjia2(self):
        self.accept_new_well()  # 接受新的井名和数据
        self.listWidget_2.addItems('new_pro_well')  #q3
    def accept_new_well(self):
        new_well_name, data = 0,0
        #new windows
        return new_well_name,data
    def tab2_daoru(self):
        text_list = self.listWidget1.selectedItems()
        inj_well_name = text_list[0].text()
        self.tab2_inj_well_name = inj_well_name

        text_list = self.listWidget_2.selectedItems()
        pro_well_name = [ti.text() for ti in text_list]
        well_num = len(pro_well_name)
        self.tab2_pro_well_name = pro_well_name


        # well_name = self.listWidget_2.getContents()    #q1 获取数据
        ls = []
        if self.checkBox_4.isChecked():
            for well in pro_well_name:
                ls.append(well+'产油量')
                ls.append(well + '产水量')
                ls.append(well + '产气量')
                ls.append(well + '井底压力')
        else:
            for well in pro_well_name:
                ls.append(well+'产油量')
                ls.append(well + '产水量')
                ls.append(well + '产气量')


        self.tableWidget3.setRowCount(100)
        self.tableWidget3.setColumnCount(len(ls))
        self.tableWidget3.setHorizontalHeaderLabels(ls)   #q1
        for i,welli in enumerate(pro_well_name):
            self.tableWidget.setItem(i+1,0,QTableWidgetItem(welli))
    def tab2_jisuan(self):
        ans = dict()
        ans['H1'] = 0.5
        ans['H2']=0.4
        data_base = {}
        interwell_index = ['0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8']
        for i in range(len(self.tab2_pro_well_name)):
            data_base[self.tab2_pro_well_name[i]] = interwell_index[i]

        self.tableWidget1.setRowCount(len(self.tab2_pro_well_name))
        self.tableWidget1.setColumnCount(2)
        self.tableWidget1.setHorizontalHeaderLabels(['井号','连通系数'])

        for i,xi in enumerate(data_base):
            self.tableWidget1.setItem(i, 0, QTableWidgetItem(str(xi)))
            self.tableWidget1.setItem(i, 1, QTableWidgetItem(data_base[xi]))
        # plot

        # self.graphicsView     #添加图片  q1
        self.graphicsView.scene_img = QGraphicsScene()
        self.imgShow = QPixmap()
        self.imgShow.load('ltt.jpg')
        self.imgShowItem = QGraphicsPixmapItem()
        self.imgShowItem.setPixmap(QPixmap(self.imgShow))
        # self.imgShowItem.setPixmap(QPixmap(self.imgShow).scaled(8000,  8000))    //自己设定尺寸
        self.graphicsView.scene_img.addItem(self.imgShowItem)
        self.graphicsView.setScene(self.graphicsView.scene_img)
        # self.graphicsView.fitInView(QGraphicsPixmapItem(QPixmap(self.imgShow))) ## 图像自适应大小

    def tab3_liulan(self):
        # apk_file = self.lineEdit_22.getCacheString('perm_figure')
        filename, _ = QFileDialog.getOpenFileName(self);
        self.filename = filename
        # text=open(filename,'r').read()
        self.lineEdit_22.setText(filename)
        # 添加渗透率图
        self.pix = QPixmap(filename)
        self.label_29.setPixmap(self.pix)
        # self.graphicsView_2.scene_img = QGraphicsScene()
        # self.imgShow = QPixmap()
        # self.imgShow.load(filename)
        # self.imgShowItem = QGraphicsPixmapItem()
        # self.imgShowItem.setPixmap(QPixmap(self.imgShow))
        # # self.imgShowItem.setPixmap(QPixmap(self.imgShow).scaled(8000,  8000))    //自己设定尺寸
        # self.graphicsView_2.scene_img.addItem(self.imgShowItem)
        # self.graphicsView_2.setScene(self.graphicsView_2.scene_img)
        # self.graphicsView.fitInView(QGraphicsPixmapItem(QPixmap(self.imgShow))) ## 图像自适应大小




    def tab3_tianjia1(self):
        well_name = self.lineEdit.text()
        # self.graphicsView_2()    #画图 p1
        self.pix = QPixmap()
        self.pix = QPixmap(400, 400)
        self.lastPoint = QPoint()
        self.endPoint = QPoint()

        self.pix = QPixmap(self.filename)
        self.label_29.setPixmap(self.pix)

    def paintEvent(self, event):
        pp = QPainter(self.pix)
        # pp.setPen(Qt.red)
        pp.setPen(QPen(Qt.red, 20))

        pp.drawArc(0,0,100,100,0,45*16)
        # 根据鼠标指针前后两个位置绘制直线
        pp.drawPoints(self.lastPoint, self.endPoint)
        # pp.drawArc(0, 0, self.lastPoint, self.endPoint, 0, 360 * 16)

        # pp.drawLine(self.lastPoint, self.endPoint)
        # 让前一个坐标值等于后一个坐标值，
        # 这样就能实现画出连续的线
        self.lastPoint = self.endPoint
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix)

        self.label_29.setPixmap(self.pix)
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.endPoint= event.pos()
            print(self.endPoint)
            self.update()
    def mouseMoveEvent(self, event):
        # if event.buttons() and Qt.LeftButton:
        #     self.endPoint = event.pos()
        #     self.update()
        pass

    def mouseReleaseEvent(self, event):
        # 鼠标左键释放
        # if event.button() == Qt.LeftButton:
        #     self.endPoint = event.pos()
        #     # 进行重新绘制
        #     self.update()
        pass


    def tab3_qidian(self):
        #q1 画图
        self.start_p = 0
    def tab3_zhongdian(self):
        #q1 画图 drawline
        self.end_p = 10
    def tab3_tianjia2(self):
        pass

    def tab3_get_parameter(self):
        # self.para.perm = float(self.lineEdit_4.text())
        # self.para.poro = float(self.lineEdit_5.text())
        # self.para.thickness = float(self.lineEdit_6.text())
        # self.para.water_saturation = float(self.lineEdit_7.text())
        # self.para.viso = float(self.lineEdit_8.text())
        # self.para.comp = float(self.lineEdit_9.text())
        # self.para.temp = float(self.lineEdit_10.text())
        # self.para.gas_rate = list(map(float,self.lineEdit_11.text()))
        # self.para.dip = float(self.lineEdit_15.text())
        # self.para.perf_position = list(map(float,self.lineEdit_13.text()))
        # self.para.rhy = float(self.lineEdit_14.text())
        # self.para.water_inten = float(self.lineEdit_12.text())
        # self.para.pro_rate = list(map(float,self.lineEdit_19.text()))
        # self.para.pressure = list(map(float,self.lineEdit_20.text()))
        # self.para.scale = self.lineEdit_3.text()  # 得到数值  q1
        # self.para.time = self.lineEdit_21.text()
        pass

    def tab3_silder1_changed(self):

        print('value change %s' % self.horizontalSlider_2.value())
        self.lineEdit_3.setText(str(self.horizontalSlider_2.value()))


    def tab3_silder2_changed(self):
        print('value change %s' % self.horizontalSlider.value())
        # 更新饱和度图片
        self.graphicsView_3.scene_img = QGraphicsScene()
        self.imgShow = QPixmap()

        self.imgShow.load('./fig/'+self.filename_ls[int(self.horizontalSlider.value())])
        # self.imgShow.load('QQ.jpg')
        self.imgShowItem = QGraphicsPixmapItem()
        self.imgShowItem.setPixmap(QPixmap(self.imgShow))
        # self.imgShowItem.setPixmap(QPixmap(self.imgShow).scaled(8000,  8000))    //自己设定尺寸
        self.graphicsView_3.scene_img.addItem(self.imgShowItem)
        self.graphicsView_3.setScene(self.graphicsView_3.scene_img)
        self.graphicsView_3.fitInView(QGraphicsPixmapItem(QPixmap(self.imgShow)))  ## 图像自适应大小
        # 更新数值
        perm = list(range(1,1551))
        dis = list(range(1, 1551))
        vert = list(range(1, 1551))

        self.lineEdit_16.setText(str(math.sin(self.horizontalSlider.value())))
        self.lineEdit_17.setText(str(math.cos(self.horizontalSlider.value())))
        self.lineEdit_18.setText(str(math.sin(self.horizontalSlider.value())))



if __name__ == '__main__':
    app = QApplication([])
    stats = Stats()
    stats.show()
    app.exec_()
