import itertools
import random
import subprocess
import numpy as np
import sys
import math
from math import comb
import matplotlib.pyplot as plt

orig = [8, 7, 10, 5, 2, 0, 1, 12, 3, 4, 11, 6, 9];
labels = ["b_1", "s", "s+3", " ", " ", 0, 1, "b_m", " ", " ", " ", " ", "b_2"]

n = len(orig)
startX = 0
endX = 14

step = (endX-startX)/(n-1)
posX = []
for i in range(n):
    posX.append(i*step+startX)

perm = np.argsort(orig)

for i in range(n - 1):
    a = perm[i]
    b = perm[i+1]
    u = posX[max(a,b)]
    l = posX[min(a,b)]
    c = 0.5*(u+l)
    r = 0.5*(u-l)

    # print(a, b, u, l, c, r)
    print("\\begin{scope}")
    if (i%2 == 0):
        print("\\clip (" + str(l-.5)+",0) rectangle ("+str(u+.5)+","+str(r+.5)+");")
    else:
        print("\\clip (" + str(l-.5)+",0) rectangle ("+str(u+.5)+",-"+str(r+.5)+");")
    if (i > 6):
        print("\\draw [ultra thick, color = red] ("+str(c)+",0) ellipse ("+str(r)+" and "+str(0.75*r)+");")
    else:
        print("\\draw [ultra thick] ("+str(c)+",0) ellipse ("+str(r)+" and "+str(0.75*r)+");")
    print("\\end{scope}")

print("\\draw [thick]("+str(startX-1)+",0) -- ("+str(endX+1) +",0);")

for i in range(len(orig)):
    print("\\filldraw ("+str(posX[i])+",0) circle[radius = 1.5pt];")
    print("\\node[below right = -2pt and 1 pt of {("+str(posX[i])+",0)}] {\\small $"+str(labels[i])+"$};")
