import sys

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas,
                 NavigationToolbar2QT as NavigationToolbar)

from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtCore import  Qt

## FigureCanvas 的父类是QWidget，是Figure的容器类
## NavigationToolbar 是图表上的工具栏

## from matplotlib.figure import Figure   #创建plot窗口的类
## Figure是图表类

class PaintProperty(QMainWindow):
    def __init__(self, parent, result_property):
        super().__init__(parent)
        self.setWindowTitle("岩石力学参数曲线")
        mpl.rcParams['font.sans-serif']=['SongTi','SimHei']    #汉字字体
        mpl.rcParams['axes.unicode_minus'] = False  # 正常显示负号

        self.result_property = result_property
        self.__iniFigure()
        self.__drawFigure()

    def __iniFigure(self):
        self.__fig = mpl.figure.Figure() # 不采用plt.figure方法，此方法不适合面向对象
        self.__fig.suptitle("岩石力学参数曲线")
        figCanvas = FigureCanvas(self.__fig)

        # 制作一个工具栏导航条
        naviToolbar = NavigationToolbar(figCanvas, self)  # 创建工具栏
        naviToolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # ToolButtonTextUnderIcon,ToolButtonTextBesideIcon

        self.addToolBar(naviToolbar)  # 添加工具栏到主窗口
        self.setCentralWidget(figCanvas)

    def __drawFigure(self):
        pic_ymod = self.__fig.add_subplot(1,6,1)
        pic_ymod.plot(self.result_property["杨氏模量"], self.result_property["深度"],
                      linewidth = 1, color = "red")
        pic_ymod.set_xlabel("杨氏模量/GPa")
        pic_ymod.set_ylabel("深度/m")

        pic_ymod = self.__fig.add_subplot(1,6,2)
        pic_ymod.plot(self.result_property["泊松比"], self.result_property["深度"],
                      linewidth = 1, color = "blue")
        pic_ymod.set_xlabel("泊松比")
        pic_ymod.set_ylabel("深度/m")

        pic_ymod = self.__fig.add_subplot(1,6,3)
        pic_ymod.plot(self.result_property["垂向应力差"], self.result_property["深度"],
                      linewidth = 1, color = "brown")
        pic_ymod.set_xlabel("垂向应力差/MPa")
        pic_ymod.set_ylabel("深度/m")

        pic_ymod = self.__fig.add_subplot(1,6,4)
        pic_ymod.plot(self.result_property["水平应力差"], self.result_property["深度"],
                      linewidth = 1, color = "green")
        pic_ymod.set_xlabel("水平应力差/MPa")
        pic_ymod.set_ylabel("深度/m")





if  __name__ == "__main__":         #用于当前窗体测试
   app = QApplication(sys.argv)     #创建GUI应用程序
   form=PaintProperty()             #创建窗体
   form.show()
   sys.exit(app.exec_())