import cv2 
import numpy as np  
import math
f = open("end3.html", "w")

X=628
Y=1200 
cap = cv2.imread('./aa1.png')
cap = cv2.resize(cap, (Y,X))
f.write("<!DOCTYPE html>\n<html style=\"background-color:white\">\n<div style=\"font-family: monospace;white-space: pre;\">")
for x in range (0,X,1):
    for y in range(0,Y,1):
        color = cap[x,y]
        temp = color[0]/8.5 + color[1]/8.5 + color[2]/8.5+36
        if(temp == 126):
            towrite= f"<span style=\"color: white\">0</span>"
        else :
            towrite=f"<span style=\"color: rgb({color[2]}, {color[1]}, {color[0]})\">"+chr(math.floor(temp))+"</span>"
        f.write(towrite)
    f.write("<br>")
f.write("</div>\n</html>")