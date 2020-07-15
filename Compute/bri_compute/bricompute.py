import os
import sys
import pandas as pd

from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog

from ui_britcompute import Ui_BritCompute


class BritCompute(QWidget):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_BritCompute()
        self.ui.setupUi(self)


    @pyqtSlot()
    def on_pb_triaxial_pressed(self):
        path = os.getcwd()
        filename, flt = QFileDialog.getOpenFileName(self, "选择三轴实验结果文件",
                                                    path, "标准格式文件(*.csv);;")

        self.tridata = pd.read_csv(filename,skiprows=6,header=None,usecols=[1,6,7,8], names=['时间','应力','应变1','应变2'])


if  __name__ == "__main__": # 显示GUI界面的主函数
    app = QApplication(sys.argv)
    form = BritCompute()
    form.show()
    sys.exit(app.exec_())