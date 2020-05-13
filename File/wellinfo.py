from PyQt5.QtWidgets import QWidget

from File.ui_wellinfo import Ui_wellinfo


class WellInfo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_wellinfo()
        self.ui.setupUi(self)

