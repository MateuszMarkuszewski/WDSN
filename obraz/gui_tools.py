import sys
from PyQt4 import QtCore, QtGui
from perceptron import Perceptron
from wdsn_ui import Ui_MainWindow


class MyForm(QtGui.QMainWindow):
    buttons = []
    perceptrons = []

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.zgaduj.clicked.connect(lambda:self.check())
        self.ui.nauka.clicked.connect(lambda:self.nauka())
        self.ui.pushButton1.clicked.connect(lambda:self.is_checked(self.ui.pushButton1))
        self.ui.pushButton2.clicked.connect(lambda:self.is_checked(self.ui.pushButton2))
        self.ui.pushButton3.clicked.connect(lambda:self.is_checked(self.ui.pushButton3))
        self.ui.pushButton4.clicked.connect(lambda:self.is_checked(self.ui.pushButton4))
        self.ui.pushButton5.clicked.connect(lambda:self.is_checked(self.ui.pushButton5))
        self.ui.pushButton6.clicked.connect(lambda:self.is_checked(self.ui.pushButton6))
        self.ui.pushButton7.clicked.connect(lambda:self.is_checked(self.ui.pushButton7))
        self.ui.pushButton8.clicked.connect(lambda:self.is_checked(self.ui.pushButton8))
        self.ui.pushButton9.clicked.connect(lambda:self.is_checked(self.ui.pushButton9))
        self.ui.pushButton10.clicked.connect(lambda:self.is_checked(self.ui.pushButton10))
        self.ui.pushButton11.clicked.connect(lambda:self.is_checked(self.ui.pushButton11))
        self.ui.pushButton12.clicked.connect(lambda:self.is_checked(self.ui.pushButton12))
        self.ui.pushButton13.clicked.connect(lambda:self.is_checked(self.ui.pushButton13))
        self.ui.pushButton14.clicked.connect(lambda:self.is_checked(self.ui.pushButton14))
        self.ui.pushButton15.clicked.connect(lambda:self.is_checked(self.ui.pushButton15))
        self.ui.pushButton16.clicked.connect(lambda:self.is_checked(self.ui.pushButton16))
        self.ui.pushButton17.clicked.connect(lambda:self.is_checked(self.ui.pushButton17))
        self.ui.pushButton18.clicked.connect(lambda:self.is_checked(self.ui.pushButton18))
        self.ui.pushButton19.clicked.connect(lambda:self.is_checked(self.ui.pushButton19))
        self.ui.pushButton20.clicked.connect(lambda:self.is_checked(self.ui.pushButton20))
        self.ui.pushButton21.clicked.connect(lambda:self.is_checked(self.ui.pushButton21))
        self.ui.pushButton22.clicked.connect(lambda:self.is_checked(self.ui.pushButton22))
        self.ui.pushButton23.clicked.connect(lambda:self.is_checked(self.ui.pushButton23))
        self.ui.pushButton24.clicked.connect(lambda:self.is_checked(self.ui.pushButton24))
        self.ui.pushButton25.clicked.connect(lambda:self.is_checked(self.ui.pushButton25))

        # self.ui.pushButton25.installEventFilter(self)
        # self.ui.pushButton24.installEventFilter(self)
        self.buttons = [
                self.ui.pushButton1,
                self.ui.pushButton2,
                self.ui.pushButton3,
                self.ui.pushButton4,
                self.ui.pushButton5,
                self.ui.pushButton6,
                self.ui.pushButton7,
                self.ui.pushButton8,
                self.ui.pushButton9,
                self.ui.pushButton10,
                self.ui.pushButton11,
                self.ui.pushButton12,
                self.ui.pushButton13,
                self.ui.pushButton14,
                self.ui.pushButton15,
                self.ui.pushButton16,
                self.ui.pushButton17,
                self.ui.pushButton18,
                self.ui.pushButton19,
                self.ui.pushButton20,
                self.ui.pushButton21,
                self.ui.pushButton22,
                self.ui.pushButton23,
                self.ui.pushButton24,
                self.ui.pushButton25,
                ]


    def is_checked(self,button):

        if button.isChecked():
            button.setChecked(True)
        else:
            button.setChecked(False)

    def check(self):
        values_in = self.values()
        values_out = []
        for i in range(25):
            values_out.append(self.perceptrons[i].check(values_in))
        self.repair(values_out)


    def values(self):
        values = []
        values.append(1)
        for button in self.buttons:
            if button.isChecked():
                values.append(1)
            else:
                values.append(0)
        return values

    def nauka(self):
        for i in range(25):
            self.perceptrons.append(Perceptron(i,self.values()))

    def repair(self,values):
        for i in range(25):
            if values[i] == 1:
                self.buttons[i].setChecked(True)
            else:
                self.buttons[i].setChecked(False)

    # def eventFilter(self, object, event):
    #     print(event.type())
    #     if event.type() == 2:
    #         self.drawing = 1
    #         return True
    #
    #     if drawing == 1:
    #         if event.type() == QtCore.QEvent.HoverMove:
    #             print(event.type())
    #             print( "C'mon! CLick-meeee!!!")
    #             return True
    #
    #     return False


if __name__ == "__main__":
     app = QtGui.QApplication(sys.argv)
     myapp = MyForm()
     myapp.show()
     sys.exit(app.exec_())
