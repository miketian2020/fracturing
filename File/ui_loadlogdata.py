# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadlogdata.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoadLogData(object):
    def setupUi(self, LoadLogData):
        LoadLogData.setObjectName("LoadLogData")
        LoadLogData.resize(928, 456)
        LoadLogData.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox = QtWidgets.QGroupBox(LoadLogData)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 421, 431))
        self.groupBox.setStyleSheet("\n"
"background-color: rgb(166, 166, 166);")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 30, 200, 100))
        self.groupBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox.setSuffix("")
        self.doubleSpinBox.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_2.setSuffix("")
        self.doubleSpinBox_2.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout.addWidget(self.doubleSpinBox_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_3.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_3.setSuffix("")
        self.doubleSpinBox_3.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout.addWidget(self.doubleSpinBox_3, 2, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(210, 30, 200, 100))
        self.groupBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_4.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_4.setSuffix("")
        self.doubleSpinBox_4.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout_2.addWidget(self.doubleSpinBox_4, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_5.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_5.setSuffix("")
        self.doubleSpinBox_5.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout_2.addWidget(self.doubleSpinBox_5, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_6.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_6.setSuffix("")
        self.doubleSpinBox_6.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.gridLayout_2.addWidget(self.doubleSpinBox_6, 2, 1, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 160, 200, 100))
        self.groupBox_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_7.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_7.setSuffix("")
        self.doubleSpinBox_7.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.gridLayout_3.addWidget(self.doubleSpinBox_7, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        self.doubleSpinBox_9 = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_9.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_9.setSuffix("")
        self.doubleSpinBox_9.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.gridLayout_3.addWidget(self.doubleSpinBox_9, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_8.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_8.setSuffix("")
        self.doubleSpinBox_8.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.gridLayout_3.addWidget(self.doubleSpinBox_8, 1, 1, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(210, 160, 200, 100))
        self.groupBox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_19 = QtWidgets.QLabel(self.groupBox_5)
        self.label_19.setObjectName("label_19")
        self.gridLayout_7.addWidget(self.label_19, 2, 0, 1, 1)
        self.doubleSpinBox_19 = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_19.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_19.setSuffix("")
        self.doubleSpinBox_19.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_19.setObjectName("doubleSpinBox_19")
        self.gridLayout_7.addWidget(self.doubleSpinBox_19, 0, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_5)
        self.label_20.setObjectName("label_20")
        self.gridLayout_7.addWidget(self.label_20, 1, 0, 1, 1)
        self.doubleSpinBox_20 = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_20.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_20.setSuffix("")
        self.doubleSpinBox_20.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_20.setObjectName("doubleSpinBox_20")
        self.gridLayout_7.addWidget(self.doubleSpinBox_20, 2, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_5)
        self.label_21.setObjectName("label_21")
        self.gridLayout_7.addWidget(self.label_21, 0, 0, 1, 1)
        self.doubleSpinBox_21 = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_21.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_21.setSuffix("")
        self.doubleSpinBox_21.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_21.setObjectName("doubleSpinBox_21")
        self.gridLayout_7.addWidget(self.doubleSpinBox_21, 1, 1, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 300, 200, 100))
        self.groupBox_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_9.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_22 = QtWidgets.QLabel(self.groupBox_9)
        self.label_22.setObjectName("label_22")
        self.gridLayout_8.addWidget(self.label_22, 2, 0, 1, 1)
        self.doubleSpinBox_22 = QtWidgets.QDoubleSpinBox(self.groupBox_9)
        self.doubleSpinBox_22.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_22.setSuffix("")
        self.doubleSpinBox_22.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_22.setObjectName("doubleSpinBox_22")
        self.gridLayout_8.addWidget(self.doubleSpinBox_22, 0, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox_9)
        self.label_23.setObjectName("label_23")
        self.gridLayout_8.addWidget(self.label_23, 1, 0, 1, 1)
        self.doubleSpinBox_23 = QtWidgets.QDoubleSpinBox(self.groupBox_9)
        self.doubleSpinBox_23.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_23.setSuffix("")
        self.doubleSpinBox_23.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_23.setObjectName("doubleSpinBox_23")
        self.gridLayout_8.addWidget(self.doubleSpinBox_23, 2, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox_9)
        self.label_24.setObjectName("label_24")
        self.gridLayout_8.addWidget(self.label_24, 0, 0, 1, 1)
        self.doubleSpinBox_24 = QtWidgets.QDoubleSpinBox(self.groupBox_9)
        self.doubleSpinBox_24.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_24.setSuffix("")
        self.doubleSpinBox_24.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_24.setObjectName("doubleSpinBox_24")
        self.gridLayout_8.addWidget(self.doubleSpinBox_24, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 300, 81, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(310, 300, 91, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 350, 81, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableView = QtWidgets.QTableView(LoadLogData)
        self.tableView.setGeometry(QtCore.QRect(460, 10, 451, 431))
        self.tableView.setObjectName("tableView")

        self.retranslateUi(LoadLogData)
        QtCore.QMetaObject.connectSlotsByName(LoadLogData)

    def retranslateUi(self, LoadLogData):
        _translate = QtCore.QCoreApplication.translate
        LoadLogData.setWindowTitle(_translate("LoadLogData", "导入测井文件"))
        self.groupBox.setTitle(_translate("LoadLogData", "数据预处理："))
        self.groupBox_2.setTitle(_translate("LoadLogData", "声波时差处理："))
        self.label.setText(_translate("LoadLogData", "Max(μs/m)"))
        self.label_2.setText(_translate("LoadLogData", "Min(μs/m)"))
        self.label_3.setText(_translate("LoadLogData", "校正值"))
        self.groupBox_3.setTitle(_translate("LoadLogData", "密度处理："))
        self.label_4.setText(_translate("LoadLogData", "Max(g/cm*3)"))
        self.label_5.setText(_translate("LoadLogData", "Min(g/cm*3)"))
        self.label_6.setText(_translate("LoadLogData", "校正值"))
        self.groupBox_4.setTitle(_translate("LoadLogData", "视电阻率处理："))
        self.label_9.setText(_translate("LoadLogData", "校正值"))
        self.label_8.setText(_translate("LoadLogData", "Min(Ω·m)"))
        self.label_7.setText(_translate("LoadLogData", "Max(Ω·m)"))
        self.groupBox_5.setTitle(_translate("LoadLogData", "自然伽马处理："))
        self.label_19.setText(_translate("LoadLogData", "校正值"))
        self.label_20.setText(_translate("LoadLogData", "Min(API)"))
        self.label_21.setText(_translate("LoadLogData", "Max(API)"))
        self.groupBox_9.setTitle(_translate("LoadLogData", "自然电位处理："))
        self.label_22.setText(_translate("LoadLogData", "校正值"))
        self.label_23.setText(_translate("LoadLogData", "Min(Ω·m)"))
        self.label_24.setText(_translate("LoadLogData", "Max(Ω·m)"))
        self.pushButton_2.setText(_translate("LoadLogData", "确定预处理值"))
        self.pushButton.setText(_translate("LoadLogData", "导入测井文件"))
        self.pushButton_3.setText(_translate("LoadLogData", "确认测井数据"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoadLogData = QtWidgets.QWidget()
    ui = Ui_LoadLogData()
    ui.setupUi(LoadLogData)
    LoadLogData.show()
    sys.exit(app.exec_())
