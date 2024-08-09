import itertools
import random
import subprocess
import numpy as np
import sys
import math
from math import comb
import matplotlib.pyplot as plt

orig = [18, 16, 5, 14, 7, 12, 9, 10, 11, 8, 13, 6, 15, 3, 1, 0, 2, 4, 17];
labels = ["n+1", "n-1", "n-1", "n+1", "n", "\\quad\\dots", "j+2", "j-1", 1, 0, "\\quad\\dots", "j"]

n = len(orig)
startX = 0
endX = 14

step = (endX-startX)/(n-1)
posX = []
for i in range(n):
    posX.append(i*step+startX)

perm = np.argsort(orig)

# for i in range(n - 1):
#     a = perm[i]
#     b = perm[i+1]
#     u = posX[max(a,b)]
#     l = posX[min(a,b)]
#     c = 0.5*(u+l)
#     r = 0.5*(u-l)
#
#     # print(a, b, u, l, c, r)
#     print("\\begin{scope}")
#     if (i%2 == 0):
#         print("\\clip (" + str(l-.5)+",0) rectangle ("+str(u+.5)+","+str(r+.5)+");")
#     else:
#         print("\\clip (" + str(l-.5)+",0) rectangle ("+str(u+.5)+",-"+str(r+.5)+");")
#     if (i > 9):
#         print("\\draw [ultra thick, color = red] ("+str(c)+",0) ellipse ("+str(r)+" and "+str(0.75*r)+");")
#     else:
#         print("\\draw [ultra thick] ("+str(c)+",0) ellipse ("+str(r)+" and "+str(0.75*r)+");")
#     print("\\end{scope}")
#
# print("\\draw [thick]("+str(startX-1)+",0) -- ("+str(endX+1) +",0);")
#
# for i in range(len(orig)):
#     print("\\filldraw ("+str(posX[i])+",0) circle[radius = 1.5pt];")
#     # print("\\node[below right=1pt of {("+str(posX[i])+",0)}] {\\small $"+str(labels[i])+"$};")
print("\\node[above=2pt of {("+str(posX[0])+",0)}] {\\small $2a-j+2$};")
print("\\node[below right=1pt of {("+str(posX[7])+",0)}] {\\small $a$};")
print("\\node[below right=1pt of {("+str(posX[8])+",0)}] {\\small $a+1$};")
print("\\node[below right=1pt of {("+str(posX[18])+",0)}] {\\small $2a-j+1$};")
