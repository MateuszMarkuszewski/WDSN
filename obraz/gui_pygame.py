# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'

# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import pygame, sys,os, random
from pygame.locals import *
from perceptron import Perceptron
import numpy
pygame.init()
# utworzenie okna
window = pygame.display.set_mode((101, 50))
xyz = pygame.image.load('image.png').convert()
screen = pygame.display.get_surface()
screen.fill((255,255,255))
screen.blit(xyz, (0,0))
for i in range(50):
    screen.set_at((51, i), (0,0,0))

imgdata = pygame.surfarray.pixels_red(xyz)
pygame.display.flip()




draw_on = False
last_pos = (0, 0)
color = (255, 128, 0)
radius = 1
perceptrons = [[] for i in range(50)]


def roundline(srf, color, start, end, radius=1):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int( start[0]+float(i)/distance*dx)
        y = int( start[1]+float(i)/distance*dy)
        pygame.draw.circle(srf, color, (x, y), radius)

def values():
    values = []
    values.append(1)
    for x in range(50):
        for y in range(50):
            if imgdata[x][y] != 255:
                values.append(1)
            else:
                values.append(0)

    return values

def learn(values):
    global perceptrons
    del perceptrons[:]
    perceptrons = [[] for i in range(50)]
    i = 0
    for x in range(50):
        for y in range(50):
            perceptrons[x].append(Perceptron(i,values))
            i = i + 1

    print("done")




def check():
    values_in = values()
    i=0
    values_out=[]
    ####
    for i in range(50):
        for j in range(50):
            values_out.append(perceptrons[i][j].check(values_in))
    values_out = numpy.array(values_out).reshape((50,50))
    repair(values_out)

def repair(values):
    print("-------")
    print(values)
    # print(values)
    for x in range(50):
        for y in range(50):
            if values[x][y] == 1:
                screen.set_at((x+51, y), (0,0,0))
            else:
                screen.set_at((x+51, y), (255,255,255))

def process_image(image):
    global xyz
    global imgdata
    xyz = pygame.image.load(image).convert()
    screen = pygame.display.get_surface()
    screen.blit(xyz, (0,0))
    pygame.display.flip()
    imgdata = pygame.surfarray.pixels_red(xyz)
    learn(values())


# działaj aż do przerwania
try:


    while True:
        if pygame.key.get_focused():
            press=pygame.key.get_pressed()
            for i in xrange(0,len(press)):
                if press[i]==1:
                    name=pygame.key.name(i)
                    print(name)
                    if name == "1":
                        process_image("image.png")
                    if name == "2":
                        process_image("indeks.png")
                    if name == "3":
                        process_image("xyz.png")
                    if name == "4":
                        process_image("cxc.png")
                    if name == "return":
                        check()
                        for i in range(50):
                            screen.set_at((51, i), (0,0,0))

        e = pygame.event.wait()
        if e.type == pygame.QUIT:
            raise StopIteration
        if e.type == pygame.MOUSEBUTTONDOWN:
            color = (0,0,0)
            pygame.draw.circle(screen, color, e.pos, radius)
            draw_on = True
        if e.type == pygame.MOUSEBUTTONUP:
            draw_on = False
        if e.type == pygame.MOUSEMOTION:
            if draw_on:
                pygame.draw.circle(screen, color, e.pos, radius)
                roundline(screen, color, e.pos, last_pos,  radius)
            last_pos = e.pos
        pygame.display.flip()

except StopIteration:
    pass

pygame.quit()
