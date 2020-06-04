import os
import sys

from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog

from File.ui_loadlogdata import Ui_LoadLogData

import pandas as pd

from pd_to_tv import pandasModel


class LoadLogData(QWidget):
    Signal_handleddata = pyqtSignal(object)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoadLogData()
        self.ui.setupUi(self)

    @pyqtSlot()
    def on_pb_load_pressed(self):
        path = os.getcwd()
        filename, flt = QFileDialog.getOpenFileName(self, "选择一个测井文件",
                                                    path, "常规测井文件(*.txt);;")
        if(filename == ""):
            return

        file = open(filename, "r", encoding="UTF-8")
        self.ori_data = pd.read_table(file, sep="\s+", skiprows=6)
        file.close()

        model_ori = pandasModel(self.ori_data)
        self.ui.tv_ori_data.setModel(model_ori)


    @pyqtSlot()
    def on_pb_handle_pressed(self):
        # 判断是否有深度、声波时差、密度、井径、自然电位、伽马测井数据

        # 初步处理原始数据
        handled_data = self.ori_data[["#DEPTH", "AC", "DEN", "CAL", "GR", "SP"]].round(3)

        # 获取设定参数值
        ac_max = self.ui.sb_ac_max.value()
        ac_min = self.ui.sb_ac_min.value()
        ac_cor = self.ui.sb_ac_cor.value()

        den_max = self.ui.sb_den_max.value()
        den_min = self.ui.sb_den_min.value()
        den_cor = self.ui.sb_den_cor.value()

        cal_max = self.ui.sb_cal_max.value()
        cal_min = self.ui.sb_cal_min.value()
        cal_cor = self.ui.sb_cal_cor.value()

        gr_max = self.ui.sb_gr_max.value()
        gr_min = self.ui.sb_gr_min.value()
        gr_cor = self.ui.sb_gr_cor.value()

        sp_max = self.ui.sb_sp_max.value()
        sp_min = self.ui.sb_sp_min.value()
        sp_cor = self.ui.sb_sp_cor.value()

        # 按照设定参数修改数据值
        self.handled_data = handled_data[(handled_data["AC"] > ac_min)
                                    & (handled_data["AC"] < ac_max)
                                    & (handled_data["DEN"] > den_min)
                                    & (handled_data["DEN"] < den_max)
                                    # & (handled_data["CAL"] > cal_min)
                                    # & (handled_data["CAL"] < cal_max)
                                    # & (handled_data["GR"] > gr_min)
                                    # & (handled_data["GR"] < gr_max)
                                    # & (handled_data["SP"] > sp_min)
                                    # & (handled_data["SP"] < sp_max)
                                    ].reset_index(drop=True)

        # 将修改后的数据填入表格
        model_han = pandasModel(self.handled_data)
        self.ui.tv_han_data.setModel(model_han)

        self.Signal_handleddata.emit(self.handled_data)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = LoadLogData()
    form.show()
    sys.exit(app.exec_())