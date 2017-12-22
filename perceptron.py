import sys
#from gui_tools import MyForm
from PyQt4 import QtCore, QtGui
from random import randint


class Perceptron:

    data = {0:(1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1),
            1:(1,0,0,0,1,0,0,0,1,1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0),
            2:(1,0,1,1,1,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,1,1,1,0),
            3:(1,0,1,1,1,0,0,0,0,1,0,0,1,1,1,0,0,0,0,1,0,0,1,1,1,0),
            4:(1,0,1,0,1,0,0,1,0,1,0,0,1,1,1,0,0,0,0,1,0,0,0,0,1,0),
            5:(1,0,1,1,1,0,0,1,0,0,0,0,1,1,1,0,0,0,0,1,0,0,1,1,1,0),
            6:(1,0,1,1,1,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0),
            7:(1,0,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0),
            8:(1,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0),
            9:(1,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,0,0,1,0,0,1,1,1,0)}


    def __init__(self,pixel):
        self.liczba=liczba
        self.trening_data = {}
        for key, value in self.data.items():
            if key == liczba:
                self.trening_data[value]=1
            else:
                self.trening_data[value]=-1
        self.rand_w()
        self.ucz()

    def rand_w(self):
        self.weight = []
        print(self.liczba)
        for i in range(26):
            self.weight.append(float(randint(0,100))/100)


    def ucz(self):
        o_sum = 0
        n = 0.02
        for j in range(100):
            for value, t in self.trening_data.items():
                for i in range(26):
                    o_sum += (value[i] * self.weight[i])

                err = t - (lambda o_sum: 1 if o_sum > 0 else -1)(o_sum)
                o_sum = 0
                if err == 0:
                    continue
                else:
                    for i in range(26):
                        self.weight[i] += (n*err*value[i])
                print("------------------")
                for i in range(26):
                    print("%d --> %f" % (i, self.weight[i]))


    def check(self,val_in):
        value = 0
        for i in range(26):
            value += (val_in[i]*self.weight[i])
        # print(self.weight)
        # print("Wynik sieci dla perceptronu %d : %s" % (self.liczba,value))
        if value>=0:
            print("Rozpoznano %s" % self.liczba)
