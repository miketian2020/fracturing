import sys

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

from Compute.fi_compute.compute import Compute
from File.loadlogdata import LoadLogData
from app.ui_main import Ui_MainWindow
from File.wellinfo import WellInfo
from data_convert.convert import Convert

class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    @pyqtSlot()
    def on_actFile_wellinfo_triggered(self):
        form_wellInfo = WellInfo(self)
        # form_wellInfo.setAttribute(Qt.WA_DeleteOnClose)
        form_wellInfo.setWindowModality(Qt.ApplicationModal)
        form_wellInfo.setWindowFlag(Qt.Window, True)

        form_wellInfo.show()

    @pyqtSlot()
    def on_actFile_loadlogdata_triggered(self):
        form_loadLogdata = LoadLogData(self)
        form_loadLogdata.setWindowModality(Qt.ApplicationModal)
        form_loadLogdata.setWindowFlag(Qt.Window, True)

        form_loadLogdata.show()

    @pyqtSlot()
    def on_actCal_strength_triggered(self):
        form_calStrength = Convert(self)
        form_calStrength.setWindowModality(Qt.ApplicationModal)
        form_calStrength.setWindowFlag(Qt.Window, True)

        form_calStrength.show()

    @pyqtSlot()
    def on_actCal_fi_triggered(self):
        form_calFi = Compute(self)
        form_calFi.setWindowModality(Qt.ApplicationModal)
        form_calFi.setWindowFlag(Qt.Window, True)

        form_calFi.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())
