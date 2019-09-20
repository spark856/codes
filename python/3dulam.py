import numpy as np
import math
import sys
from myplot import myplot

num = 2
length = 51
first = (length-1)//2

x = y = z = first

xs = [x]
ys = [y]
zs = [z]

def xadd():
	global x
	x += 1
	check()
def xsub():
	global x
	x -= 1
	check()
def yadd():
	global y
	y += 1
	check()
def ysub():
	global y
	y -= 1
	check()
def zadd():
	global z
	z += 1
	check()
def zsub():
	global z
	z -= 1
	check()

def check():
    global num
    global x
    global y
    global z
    global xs
    global ys
    global zs
    if x>=length or y>=length or z>=length:
        xs = np.asarray(xs)
        ys = np.asarray(ys)
        zs = np.asarray(zs)
        myplot(xs,ys,zs)
        sys.exit()
    if prime(num):
        xs += [x]
        ys += [y]
        zs += [z]
    num += 1
def prime(val):
	if val!=2 and val%2 == 0:
		return 0
		
	div = 3
	border = math.sqrt(val)
	while div <= border:
		if val%div == 0:
			return 0
		div += 2
	return 1

def movex(count,f):
    if count==0:
        yadd()
        return 0
    if f:
        xadd()
    else:
        yadd()
    for i in range(count):
        yadd()
    for i in range(count-1):
        xsub()
    xsub()
    for i in range(count):
        zadd()
    for i in range(count-1):
        ysub()
    ysub()
    for i in range(count):
        xadd()
    for i in range(count-1):
        zsub()
    return movex(count-1,0)

def movey(count,f):
    if count==0:
        zsub()
        return 0
    if f:
        yadd()
    else:
        zsub()
    for i in range(count):
        zsub()
    for i in range(count-1):
        ysub()
    ysub()
    for i in range(count):
        xsub()
    for i in range(count-1):
        zadd()
    zadd()
    for i in range(count):
        yadd()
    for i in range(count-1):
        xadd()
    return movey(count-1,0)

def movez(count,f):
    if count==0:
        xadd()
        return 0
    if f:
        zsub()
    else:
        xadd()
    for i in range(count):
        xadd()
    for i in range(count-1):
        zadd()
    zadd()
    for i in range(count):
        ysub()
    for i in range(count-1):
        xsub()
    xsub()
    for i in range(count):
        zsub()
    for i in range(count-1):
        yadd()
    return movez(count-1,0)
    
if __name__ == '__main__':
    count = 1
    while True:
        if count%3==1:
            movex(count,1)
            count += 1
        elif count%3==2:
            movey(count,1)
            count += 1
        elif count%3==0:
            movez(count,1)
            count += 1