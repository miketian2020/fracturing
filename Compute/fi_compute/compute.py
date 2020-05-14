import os
import sys

from PyQt5.QtCore import pyqtSlot, QItemSelectionModel
from PyQt5.QtGui import QStandardItem,QStandardItemModel
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QLabel, \
    QMessageBox

import matplotlib as mpl
import matplotlib.style as mplStyle  #一个模块
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas,
                                                NavigationToolbar2QT as NavigationToolbar)
from Compute.fi_compute.ficompute_ui import Ui_ficompute


class Compute(QMainWindow):
    def __init__(self,parent = None):#单继承
        super().__init__(parent) #调用父类构造函数，创建窗体
        self.ui = Ui_ficompute() #创建UI对象
        self.ui.setupUi(self) #构造UI界面
        self.setCentralWidget(self.ui.splitter)  # 使两个空间占满


        # 设置tableview的规格
        self.__ColCount = 6 #共设置6列数据，分别为深度，杨氏模量，泊松比，断裂韧性，水平应力差，垂向应力差
        self.itemModel = QStandardItemModel(5, self.__ColCount, self) # 创建QStandardItemModel的数据模型，并设置行数与列数

        self.selectionModel = QItemSelectionModel(self.itemModel) # Item选择模型，以self.itemModel作为参数，从而反映数据模型itemModel的项数据选择操作
        self.selectionModel.currentChanged.connect(self.do_curChanged) # 在选择的当前单元格发生变化时会发射此信号，从而在槽函数显示当前单元格的行列号及内容


        # logdata的模型相关设置
        self.ui.logdata.setModel(self.itemModel) # logdata的数据模型设置为之前定义过的数据模型

        # self.ui.logdata.setSelectionModel(self.selectionModel) # 设置选择模型
        # oneorMore = QAbstractItemView.ExtendedSelection # 选择模式
        # self.ui.logdata.setSelectionMode(oneorMore) # 可以多选单元格
        #
        # itemOrRow = QAbstractItemView.SelectItems # 项选择模式
        # self.ui.logdata.setSelectionBehavior(itemOrRow) # 单元格选择
        # self.ui.logdata.verticalHeader().setDefaultSectionSize(22) #缺省行高

        # 样式设置
        mplStyle.use("classic")  # 使用样式，必须在绘图之前调用,修改字体后才可显示汉字
        mpl.rcParams['font.sans-serif'] = ['HeiTi', 'SimHei']  # 显示汉字为 黑体， 汉字
        mpl.rcParams['font.size'] = 12
        mpl.rcParams['axes.unicode_minus'] = False  # 减号unicode编码

        # 可压性权重参数按钮的设置


        #状态栏及工具栏等设置
        self.__buildStatusBar()  # 构建状态栏
        self.curve_data = [] # 由深度和可压性指数组成的二维数组
#  ==========自定义功能函数==================
    def __buildStatusBar(self): # 构建状态栏
        self.LabCellPos = QLabel("当前单元格",self)
        self.LabCellPos.setMinimumWidth(180)
        self.ui.statusbar.addWidget(self.LabCellPos)

        self.LabCellText = QLabel("单元格内容：", self)
        self.LabCellText.setMinimumWidth(150)
        self.ui.statusbar.addWidget(self.LabCellText)

        self.LabCurFile = QLabel("当前文件", self)
        self.ui.statusbar.addPermanentWidget(self.LabCurFile)

    def __iniModelFromStringList(self, allLines): # 从可压性csv文件的字符串列表构建模型
        rowCnt = len(allLines) # 文本行数，第1行为行表头
        self.itemModel.setRowCount(rowCnt - 1)  # 实际数据行数

        headerText = allLines[0].strip() # 第1行是表头，去掉末尾的换行符“\n”
        headerList =  headerText.split("\t")
        headerList.append("可压性指数")
        self.itemModel.setHorizontalHeaderLabels(headerList) # 设置表头标题

        for i in range(rowCnt-1): # 第一行作为表头，此后才是数据体
            lineText = allLines[i+1].strip() # 一行的数据，以\t分割
            strList = lineText.split("\t") # 分割为字符串列表
            for j in range(self.__ColCount):
                item = QStandardItem(strList[j])
                self.itemModel.setItem(i,j,item)

    def __createFigure(self): # figure对象为绘图的画布对象，figurecanvas可以放在页面上
        self.__fig = mpl.pyplot.Figure()
        figCanvas = FigureCanvas(self.__fig) # 创建FigureCanvas对象，必须传递一个Figure对象
        self.__fig.suptitle("可压性曲线")

        naviToolbar = NavigationToolbar(figCanvas, self) # 创建NavigationToolbar工具栏
        actList = naviToolbar.actions() # 关联的Action列表
        count = len(actList) # Action的个数
        self.addToolBar(naviToolbar)


        self.ui.layout_curve.addWidget(figCanvas)

    def __drawFiCurve(self):
        curve = self.__fig.add_subplot(1,1,1)
        x = []
        y = []
        for i in self.curve_data:
            x.append(i[0])
            y.append(i[1])
        curve.plot(y,x)
        curve.set_xlabel("可压性指数")
        curve.set_ylabel("深度")
        curve.set_xlim([0,100])
        curve.set_ylim([0,1000])
        curve.xaxis.tick_top()


#  ==========由connectSlotsByName() 自动连接的槽函数==================
    @pyqtSlot()  ##“打开文件”
    def on_actopen_triggered(self):
        curPath = os.getcwd() # 获取当前路径
        filename, flt = QFileDialog.getOpenFileName(self, "打开一个文件", curPath,
                                                    "可压性数据文件(*.txt *.csv);;"
                                                    "可压性数据文件(*.xlsx);;"
                                                    "所有文件(*.*)")
        if(filename == ""):
            return

        self.LabCurFile.setText("当前文件："+ filename)

        aFile = open(filename, "r", encoding="utf-8") # 需要设置解码格式为utf-8
        allLines = aFile.readlines() # 读取所有行，list类型，每行末尾带有\n
        aFile.close() # 使用完后需关闭这个文件对象

        self.__iniModelFromStringList(allLines) # 将每一行读取到logdata中

    @pyqtSlot()#修改权重因子时设置权重为可修改
    def on_pbmodify_pressed(self):
        self.ui.f1.setEnabled(True)
        self.ui.f2.setEnabled(True)
        self.ui.f3.setEnabled(True)
        self.ui.f4.setEnabled(True)
        self.ui.f5.setEnabled(True)

    @pyqtSlot()#确定权重因子时设置权重为可修改
    def on_pbconfirm_pressed(self):
        self.ui.f1.setEnabled(False)
        self.ui.f2.setEnabled(False)
        self.ui.f3.setEnabled(False)
        self.ui.f4.setEnabled(False)
        self.ui.f5.setEnabled(False)

    @pyqtSlot()#计算可压性并填写进最后一列
    def on_pbcompute_pressed(self):
        #添加可压性的列

        #取出spinbox中的权重因子
        f1 = self.ui.f1.value()
        f2 = self.ui.f2.value()
        f3 = self.ui.f2.value()
        f4 = self.ui.f2.value()
        f5 = self.ui.f2.value()

        # 计算可压性
        try:
            for i in range(self.itemModel.rowCount()): # 第i行的数据运算
                # 每一列是一个数据模型，需要将其转化为float
                col1 = float(self.itemModel.item(i,1).text())
                col2 = float(self.itemModel.item(i,2).text())
                col3 = float(self.itemModel.item(i,3).text())
                col4 = float(self.itemModel.item(i,4).text())
                col5 = float(self.itemModel.item(i,5).text())
                fi = col1*f1 + col2*f2 + col3*f3 + col4*f4 + col5*f5 # 计算公式，获取lineedit中的权重因子
                item_fi = QStandardItem(str(fi)) # 计算可压性后，将可压性作为最后一列的项放入
                self.itemModel.setItem(i, 6, item_fi) # 将每个深度的可压性导入到item中
        except:
            dlgTitle = "错误提示！"
            strInfo = "请检查数据输入"
            QMessageBox.warning(self, dlgTitle, strInfo)

    @pyqtSlot()
    def on_pbpaint_pressed(self):
        try:
            for i in range(self.itemModel.rowCount()):
                depth = float(self.itemModel.item(i,0).text())
                fi = float(self.itemModel.item(i,6).text())
                self.curve_data.append([depth,fi])
            self.__createFigure()  # 将figurecanvas画布展现在右侧
            self.__drawFiCurve()
        except:
            dlgTitle = "错误提示！"
            strInfo = "请检查可压性参数是否输入正确"
            QMessageBox.warning(self, dlgTitle, strInfo)


#  ==========自定义槽函数  不需要添加@pyqtslot============
    def do_curChanged(self, current, previous):
        if(current != None):    #当前模型索引有效
            text="当前单元格：%d行，%d列"%(current.row(),current.column())
            self.LabCellPos.setText(text)
            item = self.itemModel.itemFromIndex(current)  # 从模型索引获得Item
            self.LabCellText.setText("单元格内容：" + item.text())  # 显示item的文字内容


if  __name__ == "__main__": # 显示GUI界面的主函数
    app = QApplication(sys.argv)
    form=Compute()
    form.show()
    sys.exit(app.exec_())
