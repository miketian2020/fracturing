from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot, pyqtSignal

from File.ui_wellinfo import Ui_wellinfo


class WellInfo(QWidget):

    Signal_wellInfo = pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_wellinfo()
        self.ui.setupUi(self)


    @pyqtSlot()
    def on_pb_confirm_pressed(self):
        wellBlock = self.ui.le_block.text()
        wellLayer = self.ui.le_layer.text()
        wellNum = self.ui.le_wellnum.text()
        wellBottom = self.ui.sb_bottom.value()
        wellTop = self.ui.sb_top.value()
        wellInfo_list = [wellBlock, wellLayer, wellNum, wellBottom, wellTop]
        self.Signal_wellInfo.emit(wellInfo_list)
        self.close()
