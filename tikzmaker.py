import itertools
import random
import subprocess
import numpy as np
import sys
import math
from math import comb
import matplotlib.pyplot as plt

orig = [1, 0, 2, 4, 3];

n = len(orig)
startX = 0
endX = 10

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
        print("\\clip (" + str(l)+",0) rectangle ("+str(u)+","+str(r)+");")
    else:
        print("\\clip (" + str(l)+",0) rectangle ("+str(u)+",-"+str(r)+");")
    print("\\draw ("+str(c)+",0) circle ("+str(r)+");")
    print("\\end{scope}")
