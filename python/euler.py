#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import math
import sys
from plot2d import myplot


xe = []
ye = []
xp = []
yp = []
text = []


a = 41
for b in range(100):
    num = b*b+b+a
    ulim = (2*b+1+2*np.sqrt(num))/(4*a-1)
    dlim = (2*b+1-2*np.sqrt(num))/(4*a-1)

    y1 = np.linspace(dlim, ulim, 1000)
    x1 = np.sqrt(np.abs((4*b+2)*y1-(4*a-1)*y1*y1+1))
    y2 = np.linspace(ulim, dlim, 1000)
    x2 = -np.sqrt(np.abs((4*b+2)*y1-(4*a-1)*y1*y1+1))

    ye += [np.concatenate([y1,y2])]
    xe += [np.concatenate([x1,x2])]

    y=1
    count = 0
    yt = [0]
    xt = [1]
    while True:
        D = (y+1)*(y+1)-4*y*(y*a-b)
        if D < 0:
            if count:
                text += [f'$\quad b^2+b+a={num} \quad is \quad not \quad a \quad prime \quad number$']
            else:
                text += [f'$\quad b^2+b+a={num} \quad is \quad a \quad prime \quad number$']
            break;

        x = math.sqrt(D)
        if x.is_integer():
            count += 1
            x = int(x)
            xt += [x]
            yt += [y]
        y += 1

    xt = np.asarray(xt)
    xp += [np.concatenate([xt,-xt])]
    yt = np.asarray(yt)
    yp += [np.concatenate([yt,yt])]

myplot(xe,ye,xp,yp,text)
