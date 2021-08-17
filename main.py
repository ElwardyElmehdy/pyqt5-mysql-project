
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from PyQt5.QtWidgets import QTableWidgetItem,QAction,QFileDialog


class Ui_AnalyseurTrameCan(object):
    def setupUi(self, AnalyseurTrameCan):
        AnalyseurTrameCan.setObjectName("AnalyseurTrameCan")
        AnalyseurTrameCan.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(AnalyseurTrameCan)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.recherch = QtWidgets.QPushButton(self.centralwidget)
        self.recherch.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("search.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recherch.setIcon(icon)
        self.recherch.setIconSize(QtCore.QSize(50, 50))
        self.recherch.setFlat(True)
        self.recherch.setObjectName("recherch")
        self.recherch.clicked.connect(self.recherche)
        self.verticalLayout_2.addWidget(self.recherch)
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setEnabled(True)
        self.refresh.setAutoFillBackground(False)
        self.refresh.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("refresh.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh.setIcon(icon1)
        self.refresh.setIconSize(QtCore.QSize(50, 50))
        self.refresh.setFlat(True)
        self.refresh.setObjectName("refresh")
        self.refresh.clicked.connect(self.mysql_connect)
        self.verticalLayout_2.addWidget(self.refresh)
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("save.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save.setIcon(icon2)
        self.save.setIconSize(QtCore.QSize(50, 50))
        self.save.setFlat(True)
        self.save.setObjectName("save")
        self.save.clicked.connect(self.file_save)
        self.verticalLayout_2.addWidget(self.save)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("close.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.destr)
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(25)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(str("ID:DLC:DATA:Time:Date").split(":"))
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        AnalyseurTrameCan.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AnalyseurTrameCan)
        self.statusbar.setObjectName("statusbar")
        AnalyseurTrameCan.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(AnalyseurTrameCan)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 549, 21))
        self.menuBar.setObjectName("menuBar")
        self.menufile = QtWidgets.QMenu(self.menuBar)
        self.menufile.setObjectName("menufile")
        AnalyseurTrameCan.setMenuBar(self.menuBar)
        self.actionsearch = QtWidgets.QAction(AnalyseurTrameCan)
        self.actionsearch.setObjectName("actionsearch")
        self.actionsave = QtWidgets.QAction(AnalyseurTrameCan)
        self.actionsave.setObjectName("actionsave")
        self.actionclose = QtWidgets.QAction(AnalyseurTrameCan)
        self.actionclose.setObjectName("actionclose")
        self.actionrefresh = QtWidgets.QAction(AnalyseurTrameCan)
        self.actionrefresh.setObjectName("actionrefresh")
        self.menufile.addAction(self.actionsearch)
        self.menufile.addAction(self.actionsave)
        self.menufile.addAction(self.actionclose)
        self.menufile.addAction(self.actionrefresh)
        self.menuBar.addAction(self.menufile.menuAction())

        self.retranslateUi(AnalyseurTrameCan)
        QtCore.QMetaObject.connectSlotsByName(AnalyseurTrameCan)
    def mysql_connect(self):

        mydb = mysql.connector.connect(
            host="remotemysql.com",
            user="LbdaNp7qLn",
            password="ZAJL2y8FMN",
            database="LbdaNp7qLn"

        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM nodemcu_table ORDER BY ID DESC")
        result = mycursor.fetchall()
        self.tableWidget.setRowCount(0)
        for row_num,row_data in enumerate(result) :
            self.tableWidget.insertRow(row_num)
            for colu_num,data in enumerate(row_data):
                self.tableWidget.setItem(row_num,colu_num,QTableWidgetItem(str(data)))

    def recherche(self):
        mydb = mysql.connector.connect(
            host="remotemysql.com",
            user="LbdaNp7qLn",
            password="ZAJL2y8FMN",
            database="LbdaNp7qLn"

        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM nodemcu_table ORDER BY ID DESC")
        result = mycursor.fetchall()


        rech=self.lineEdit.text()

        self.tableWidget.setRowCount(0)
        i=0
        for x in result:
            if rech in str(x[0]):
                self.tableWidget.insertRow(i)


                for colu_num,data in enumerate(x) :
                    self.tableWidget.setItem(i, colu_num, QTableWidgetItem(str(data)))
                i += 1






    def destr(self):
        self.AnalyseurTrameCan.destroyed()

    def file_save(self):
        mydb = mysql.connector.connect(
            host="remotemysql.com",
            user="LbdaNp7qLn",
            password="ZAJL2y8FMN",
            database="LbdaNp7qLn"

        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM nodemcu_table ORDER BY ID DESC")
        result =mycursor.fetchall()
        res=""
        for x in result:
            res=res+str(x)+' \n'


        name = QtWidgets.QFileDialog.getSaveFileName(AnalyseurTrameCan, "Save File", '/', '.txt')
        if name[0]+name[1]!="" :
            file = open(name[0] + name[1], 'w')
            file.write(res)
            file.close()



    def retranslateUi(self, AnalyseurTrameCan):
        _translate = QtCore.QCoreApplication.translate
        AnalyseurTrameCan.setWindowTitle(_translate("AnalyseurTrameCan", "MainWindow"))
        self.menufile.setTitle(_translate("AnalyseurTrameCan", "Edit"))
        self.actionsearch.setText(_translate("AnalyseurTrameCan", "search"))
        self.actionsearch.setShortcut(_translate("AnalyseurTrameCan", "Ctrl+S"))
        self.actionsave.setText(_translate("AnalyseurTrameCan", "save "))
        self.actionsave.setShortcut(_translate("AnalyseurTrameCan", "Ctrl+1"))
        self.actionclose.setText(_translate("AnalyseurTrameCan", "close"))
        self.actionclose.setShortcut(_translate("AnalyseurTrameCan", "Ctrl+C"))
        self.actionrefresh.setText(_translate("AnalyseurTrameCan", "refresh"))
        self.actionrefresh.setShortcut(_translate("AnalyseurTrameCan", "Ctrl+F"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AnalyseurTrameCan = QtWidgets.QMainWindow()
    AnalyseurTrameCan.setWindowTitle("qt application")
    ui = Ui_AnalyseurTrameCan()
    ui.setupUi(AnalyseurTrameCan)
    AnalyseurTrameCan.show()
    sys.exit(app.exec_())
