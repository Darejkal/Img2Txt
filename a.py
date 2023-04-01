import cv2 
import numpy as np  
import math
f = open("end.txt", "w")

X=297
Y=420
cap = cv2.imread('./end.png')
cap = cv2.resize(cap, (Y,X))

for x in range (0,X,1):
    for y in range(0,Y,1):
        color = cap[x,y]
        temp = color[0]/8.5 + color[1]/8.5 + color[2]/8.5+36
        if(temp == 126):
            temp=32
        f.write(chr(math.floor(temp)))
    f.write("\n")