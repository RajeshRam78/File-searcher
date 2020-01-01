# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Fastsearch(object):

    def __init__(self):
        self.Root_dir_path = ""
        self.Prev_root = self.Root_dir_path
        self.File_hash_table = {}

    def process(self):
        print(self.listWidget.currentItem().text())
        os.startfile(self.listWidget.currentItem().text())


    def browse_directory(self):
        self.Root_dir_path = QtWidgets.QFileDialog.getExistingDirectory()
        self.Root_dir_path = str(self.Root_dir_path)
        self.Le_root_dir_text.setText(self.Root_dir_path)

    def start_searching(self):

        self.listWidget.clear()
        if(not os.path.exists(self.Root_dir_path)):
            dlg = QtWidgets.QMessageBox()
            dlg.setWindowTitle("Missing!!")
            dlg.setText("Not found : {}".format(self.Root_dir_path))
            dlg.exec_()
        elif self.Prev_root != self.Root_dir_path:
            self.ccount = 0
            self.total = 0
            self.status_label.setText("Hashing")
            for folder_path, folder_name, file_names in os.walk(self.Root_dir_path):
                for file_name in file_names:
                    try:
                        self.File_hash_table[file_name[0]].append((file_name, folder_path))
                    except:
                        self.File_hash_table[file_name[0]] = [(file_name, folder_path)]
                #self.progressBar.setValue(1)

            self.status_label.setText("Hashing complete")
            self.Prev_root = self.Root_dir_path

            self.total = len(self.File_hash_table)


        for hash_element in self.File_hash_table:
            self.ccount += 1
            percent = (self.ccount/self.total)*100
            self.progressBar.setValue(percent)
            for element in self.File_hash_table[hash_element]:
                if self.Le_search_text.text() in element[0]:
                    self.listWidget.addItem(str(element[1]) + "\\" + str(element[0]))

    def setupUi(self, Fastsearch):
        Fastsearch.setObjectName("Fastsearch")
        Fastsearch.resize(640, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Fastsearch.setWindowIcon(icon)
        Fastsearch.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(Fastsearch)
        self.centralwidget.setObjectName("centralwidget")
        self.Le_root_dir_text = QtWidgets.QLineEdit(self.centralwidget)
        self.Le_root_dir_text.setGeometry(QtCore.QRect(110, 20, 511, 21))
        self.Le_root_dir_text.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.Le_root_dir_text.setInputMask("")
        self.Le_root_dir_text.setText("")
        self.Le_root_dir_text.setObjectName("Le_root_dir_text")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browse_directory)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.start_searching)


        self.Le_search_text = QtWidgets.QLineEdit(self.centralwidget)
        self.Le_search_text.setGeometry(QtCore.QRect(110, 60, 511, 21))
        self.Le_search_text.setObjectName("Le_search_text")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(110, 100, 511, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(20, 100, 71, 20))
        self.status_label.setText("")
        self.status_label.setObjectName("status_label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 140, 601, 291))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.doubleClicked.connect(self.process)

        Fastsearch.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Fastsearch)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        Fastsearch.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Fastsearch)
        self.statusbar.setObjectName("statusbar")
        Fastsearch.setStatusBar(self.statusbar)

        self.retranslateUi(Fastsearch)
        QtCore.QMetaObject.connectSlotsByName(Fastsearch)

    def retranslateUi(self, Fastsearch):
        _translate = QtCore.QCoreApplication.translate
        Fastsearch.setWindowTitle(_translate("Fastsearch", "File_searcher"))
        self.pushButton.setText(_translate("Fastsearch", "Root Dir"))
        self.pushButton_2.setText(_translate("Fastsearch", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fastsearch = QtWidgets.QMainWindow()
    ui = Ui_Fastsearch()
    ui.setupUi(Fastsearch)
    Fastsearch.show()
    sys.exit(app.exec_())

