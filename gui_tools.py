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
        self.ui.zgaduj.clicked.connect(lambda:self.values())
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
        if button.isFlat():
            button.setFlat(False)
        else:
            button.setFlat(True)

    def values(self):
        values = []
        values.append(1)
        for button in self.buttons:
            if button.isFlat():
                values.append(1)
            else:
                values.append(0)
        for p in self.perceptrons:
            p.check(values)

    def nauka(self):
        for i in range(25):
            self.perceptrons.append(Perceptron(i))


if __name__ == "__main__":
     app = QtGui.QApplication(sys.argv)
     myapp = MyForm()
     myapp.show()
     sys.exit(app.exec_())
