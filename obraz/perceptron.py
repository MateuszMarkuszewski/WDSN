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


    def __init__(self,pixel,values):
        self.pixel=pixel
        self.trening_data = values
        self.pixel_value = values[pixel+1]
        self.rand_w()
        self.ucz()

    def rand_w(self):
        self.weight = []
        for i in range(2501):
            self.weight.append(float(randint(0,100))/100)
        # print(self.weight)

    def ucz(self):
        o_sum = 0
        n = 0.02
        self.activation = 0
        for j in range(1):
            for i in range(2501):
                o_sum += self.trening_data[i] * self.weight[i]

            err = self.pixel_value - (lambda o_sum: 1 if o_sum > 0 else -1)(o_sum)
            o_sum = 0
            if err == 0:
                continue
            else:
                for i in range(2501):
                    self.weight[i] += (n*err*self.trening_data[i] )
                    self.activation += (self.trening_data[i]*self.weight[i])


            # for i in range(26):
                # print("%d --> %d" % (self.trening_data[i],self.weight[i]))
        # print("------------------")
        # print(self.weight)
        # print(self.pixel)
        # print(self.activation)


    def check(self,val_in):
        value = 0
        for i in range(2501):
            value += (val_in[i]*self.weight[i])

        # print("pixel %s, wartosc %s" % (self.pixel,value))
        if value == self.activation:
            return 0
        else:

            return 1
