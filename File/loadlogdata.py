import sys

from PyQt5.QtWidgets import QWidget, QApplication

from File.ui_loadlogdata import Ui_LoadLogData


class LoadLogData(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoadLogData()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = LoadLogData()
    form.show()
    sys.exit(app.exec_())