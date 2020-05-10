import os
import sys
from math import e

import pandas as pd

from PyQt5.QtCore import QItemSelectionModel, pyqtSlot
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QMainWindow, QApplication, QAbstractItemView, QFileDialog

from data_convert.pd_to_tv import pandasModel
from data_convert.ui_dataconvert import Ui_dataconvert


class Convert(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_dataconvert()
        self.ui.setupUi(self)


# ==========自定义槽函数===========
    @pyqtSlot()
    def on_act_open_con_triggered(self):
        path = os.getcwd()
        filename, flt = QFileDialog.getOpenFileName(self, "选择一个测井文件", path,
                                                    "常规测井文建(*.txt);;")
        if (filename == ""):
            return

        file = open(filename, "r", encoding="UTF-8")
        self.con_data = pd.read_table(file, sep="\s+")
        file.close()

        # 以下是Model的相关设置，从而完整展现tableview
        self.model = pandasModel(self.con_data)
        self.ui.con_logdata.setModel(self.model)
        self.selectionModel = QItemSelectionModel(self.model)
        self.ui.con_logdata.setSelectionModel(self.selectionModel)


    @pyqtSlot()
    def on_pb_convert_pressed(self):
        depth = self.con_data['DEPTH']
        tp = self.con_data['AC']
        den = self.con_data['DEN']

        k_ymod = self.ui.k_ymod.value()
        b_ymod = self.ui.b_ymod.value()
        k_pois = self.ui.k_pois.value()
        b_pois = self.ui.b_pois.value()

        ts = tp / (1 - 1.15 * (((1 / den) + (1 / den) ** 3) / (e ** (1 / den)))) ** 1.5
        con_y_mod = (den / ts ** 2) * ((3 * ts ** 2 - 4 * tp ** 2) / (ts ** 2 - tp ** 2)) * 10 ** 6
        con_p_ratio = (ts ** 2 - 2 * tp ** 2) / (2 * (ts ** 2 - tp ** 2))

        y_mod = k_ymod * con_y_mod + b_ymod
        p_ratio = k_pois * con_p_ratio + b_pois

        self.handled_data = pd.DataFrame(list(zip(depth,y_mod,p_ratio)), columns=["深度", "杨氏模量", "泊松比"])

        self.handled_data_model = pandasModel(self.handled_data)
        self.ui.handled_data.setModel(self.handled_data_model)


if  __name__ == "__main__": # 显示GUI界面的主函数
    app = QApplication(sys.argv)
    form=Convert()
    form.show()
    sys.exit(app.exec_())