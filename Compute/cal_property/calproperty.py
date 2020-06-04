import sys
from math import e

from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication

from pd_to_tv import pandasModel
from ui_calproperty import Ui_CalProperty

import pandas as pd

# ori_data = pd.read_table("延页2井标准.txt", sep="\s+", skiprows=6)
# test = ori_data[(ori_data["AC"] > 50)
#                     & (ori_data["AC"] < 500)
#                     & (ori_data["DEN"] > 1)
#                     & (ori_data["DEN"] < 5)].reset_index(drop=True)

class CalProperty(QWidget):
    Signal_result = pyqtSignal(object)
    def __init__(self, parent, handled_data):
        super().__init__(parent)
        self.ui = Ui_CalProperty()
        self.ui.setupUi(self)
        self.handled_data = handled_data


        model = pandasModel(self.handled_data)
        self.ui.tv_han_data.setModel(model)

    @pyqtSlot()
    def on_pb_convert_pressed(self):

        # 获取该窗口各参数的数据
        Biot = self.ui.sb_Biot.value()
        Pp = self.ui.sb_Pp.value()
        H_xishu = self.ui.sb_H_xishu.value()
        h_xishu = self.ui.sb_h_xishu.value()
        cor_density = self.ui.sb_cor_density.value()

        depth = self.handled_data['#DEPTH'] # 处理结果的深度数据
        tp = self.handled_data['AC'] # 纵波时差数据
        den = self.handled_data['DEN'] # 密度数据

        k_ymod = self.ui.sb_k_ymod.value()
        b_ymod = self.ui.sb_b_ymod.value()
        k_pois = self.ui.sb_k_pois.value()
        b_pois = self.ui.sb_b_pois.value()

        # 计算横波时差及初始杨氏模量和泊松比
        ts = tp / (1 - 1.15 * (((1 / den) + (1 / den) ** 3) / (e ** (1 / den)))) ** 1.5
        ori_y_mod = (den / ts ** 2) * ((3 * ts ** 2 - 4 * tp ** 2) / (ts ** 2 - tp ** 2)) * 10 ** 6
        ori_p_ratio = (ts ** 2 - 2 * tp ** 2) / (2 * (ts ** 2 - tp ** 2))

        # 计算在公式下得出的杨氏模量及泊松比
        y_mod = k_ymod * ori_y_mod + b_ymod
        p_ratio = k_pois * ori_p_ratio + b_pois

        # 垂向地应力计算
        dep_den = self.handled_data[["#DEPTH", "DEN"]] # 密度与深度曲线
        delta_depth = dep_den.iloc[100,0] - dep_den.iloc[99,0] # 深度间隔

        list1 = dep_den["DEN"].tolist()# 将密度转化成数组，方便计算
        delta_den = [] # 为离散化的ρ值
        for i in range(len(list1)):
            if(i == 0):
                delta_den.append(list1[i]) # 第一个密度值前无其他值，故不需要迭代
            elif(i > 0):
                delta_den.append(delta_den[i-1] + list1[i])

        ver_p = [(x * delta_depth + depth[0] * cor_density) * 10 / 1000 for x in delta_den] # 前面的

        result = pd.DataFrame(list(zip(depth, y_mod, p_ratio, ver_p)),
                              columns=["深度", "杨氏模量", "泊松比", "垂向地应力"]).round(3)

        # 水平地应力计算
        result["水平最小地应力"] = (Biot * Pp * depth / 100 + p_ratio / (1 - p_ratio) * (ver_p - Biot * Pp * depth / 100) \
                            + y_mod * h_xishu / (1 - p_ratio ** 2) + p_ratio * y_mod * H_xishu / (1 - p_ratio ** 2)).__round__(3)

        result["水平最大地应力"] = (Biot * Pp * depth / 100 + p_ratio / (1 - p_ratio) * (ver_p - Biot * Pp * depth / 100) \
                            + y_mod * H_xishu / (1 - p_ratio ** 2) + p_ratio * y_mod * h_xishu / (1 - p_ratio ** 2)).__round__(3)

        result["垂向应力差"] = (abs(ver_p - result["水平最小地应力"])).__round__(3)

        result["水平应力差"] = (abs(result["水平最大地应力"] - result["水平最小地应力"])).__round__(3)


        result_model = pandasModel(result)
        self.ui.tv_result.setModel(result_model)

        self.Signal_result.emit(result)

if  __name__ == "__main__": # 显示GUI界面的主函数
    app = QApplication(sys.argv)
    form=CalProperty()
    form.show()
    sys.exit(app.exec_())