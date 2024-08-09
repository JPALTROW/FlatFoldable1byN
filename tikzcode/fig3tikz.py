import itertools
import random
import subprocess
import numpy as np
import sys
import math
from math import comb
import matplotlib.pyplot as plt

orig = [6, 3, 1, 0, 2, 5, 4];
labels = ["n+1", "n-1", "1", "0", "2", "n+1", "n"]

n = len(orig)
startX = 0
endX = 14

step = (endX-startX)/(n-1)
posX = []
for i in range(n):
    posX.append(i*step+startX)

perm = np.argsort(orig)

for i in range(n-2):
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
    print("\\draw [ultra thick] ("+str(c)+",0) ellipse ("+str(r)+" and "+str(0.75*r)+");")
    print("\\end{scope}")

a = 0
b = 6
u = posX[max(a,b)]
l = posX[min(a,b)]
c = 0.5*(u+l)
r = 0.5*(u-l)
print("\\begin{scope}")
print("\\clip (" + str(l-.5)+",0) rectangle ("+str(u+.5)+","+str(r+.5)+");")
print("\\draw [ultra thick, color = red] ("+str(c)+",0) ellipse ("+str(r)+" and "+str(0.75*r)+");")
print("\\end{scope}")

print("\\draw [thick]("+str(startX-1)+",0) -- ("+str(endX+1) +",0);")

for i in range(len(orig)):
    print("\\filldraw ("+str(posX[i])+",0) circle[radius = 1.5pt];")
    print("\\node[below right=1pt of {("+str(posX[i])+",0)}] {\\small$"+str(labels[i])+"$};")
