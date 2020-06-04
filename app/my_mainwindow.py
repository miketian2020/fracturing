import sys

from PyQt5.QtCore import pyqtSlot, Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

from Compute.fi_compute.compute import Compute
from File.loadlogdata import LoadLogData
from app.ui_main import Ui_MainWindow
from File.wellinfo import WellInfo
from calproperty import CalProperty
from data_convert.convert import Convert
from paintproperty import PaintProperty
from pd_to_tv import pandasModel


class Main(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    @pyqtSlot()
    def on_actFile_wellinfo_triggered(self):
        form_wellInfo = WellInfo(self)
        # form_wellInfo.setAttribute(Qt.WA_DeleteOnClose)
        form_wellInfo.Signal_wellInfo.connect(self.wellInformation)

        form_wellInfo.setWindowModality(Qt.ApplicationModal)
        form_wellInfo.setWindowFlag(Qt.Window, True)

        form_wellInfo.show()


    @pyqtSlot()
    def on_actFile_loadlogdata_triggered(self):
        form_loadLogdata = LoadLogData(self)
        form_loadLogdata.Signal_handleddata.connect(self.handle)
        form_loadLogdata.setWindowModality(Qt.ApplicationModal)
        form_loadLogdata.setWindowFlag(Qt.Window, True)
        form_loadLogdata.show()

    @pyqtSlot()
    def on_actCal_property_triggered(self):
        form_calProperty = CalProperty(self, self.handled_data)
        form_calProperty.Signal_result.connect(self.property_result)
        form_calProperty.setWindowModality(Qt.ApplicationModal)
        form_calProperty.setWindowFlag(Qt.Window, True)
        form_calProperty.show()

    @pyqtSlot()
    def on_actCal_fi_triggered(self):
        form_calFi = Compute(self)
        form_calFi.setWindowModality(Qt.ApplicationModal)
        form_calFi.setWindowFlag(Qt.Window, True)

        form_calFi.show()

    @pyqtSlot()
    def on_actPaint_property_triggered(self):
        form_paintProperty = PaintProperty(self, self.property)
        form_paintProperty.setWindowModality(Qt.ApplicationModal)
        form_paintProperty.setWindowFlag(Qt.Window, True)
        form_paintProperty.show()


    def wellInformation(self, wellInfo_list):
        self.wellBlock = wellInfo_list[0]
        self.wellLayer = wellInfo_list[1]
        self.wellNum = wellInfo_list[2]
        self.wellBottom = wellInfo_list[3]
        self.wellTop = wellInfo_list[4]

    def handle(self, data):
        self.handled_data = data

    def property_result(self, result):
        self.property = result

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())
