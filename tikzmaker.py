import itertools
import random
import subprocess
import numpy as np
import sys
import math
from math import comb
import matplotlib.pyplot as plt

orig = [5, 14, 7, 12, 9, 10, 11, 8, 13, 6, 3, 1, 0, 2, 4];
labels = ["j+1", "2a-j+2", "j+3", " ", " ", 'a', 'a+1', " ", " ", "j+2", "j-1", "1", "0", " ", "j"]

n = len(orig)
startX = 0
endX = 14

step = (endX-startX)/(n-1)
posX = []
for i in range(n):
    posX.append(i*step+startX)

perm = np.argsort(orig)

def draw_top_arc(c,r, color):
    print("\\begin{scope}")
    print("\\clip (" + str(c-r-.5)+",0) rectangle ("+str(c+r+.5)+","+str(r+.5)+");")
    print("\\draw [ultra thick, color = "+color+"] ("+str(c)+",0) ellipse ("+str(r)+" and "+str(0.75*r)+");")
    print("\\end{scope}")

def draw_bottom_arc(c,r, color):
    print("\\begin{scope}")
    print("\\clip (" + str(c-r-.5)+",0) rectangle ("+str(c+r+.5)+",-"+str(r+.5)+");")
    print("\\draw [ultra thick, color = "+color+"] ("+str(c)+",0) ellipse ("+str(r)+" and "+str(0.75*r)+");")
    print("\\end{scope}")

def rspiral(i, color):
    c = posX[perm[i]]+step/4
    r = step/4
    for j in range(5):
        if (j%2 == 0):
            draw_top_arc(c, r, color)
        else:
            draw_bottom_arc(c,r,color)

        c = c+r*((-1)**j)/2
        r = r/2

def lspiral(i, color):
    c = posX[perm[i]]-step/4
    r = step/4
    for j in range(5):
        if (j%2 == 1):
            draw_top_arc(c, r, color)
        else:
            draw_bottom_arc(c,r,color)

        c = c-r*((-1)**j)/2
        r = r/2


for i in range(n - 1):
    a = perm[i]
    b = perm[i+1]
    c = 0.5*(a+b)
    r = 0.5*(abs(a-b))
    color = 'black'
    if (i> 9):
        color = 'red'
    if (i%2 == 0):
        draw_top_arc(c,r, color)
    else:
        draw_bottom_arc(c,r,color)
rspiral(12, 'red')
lspiral(11, 'red')
lspiral(13, 'red')

print("\\draw [thick]("+str(startX-1)+",0) -- ("+str(endX+1) +",0);")

for i in range(len(orig)):
    print("\\filldraw ("+str(posX[i])+",0) circle[radius = 1.5pt];")
    print("\\node[below right = -2pt and 0 pt of {("+str(posX[i])+",0)}] {\\small $"+str(labels[i])+"$};")
