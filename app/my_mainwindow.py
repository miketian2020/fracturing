import sys

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication

from File.loadlogdata import LoadLogData
from app.ui_main import Ui_MainWindow
from File.wellinfo import WellInfo


class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
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
        print("qwe")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())
