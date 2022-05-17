import os, sys
try:
    from turtle import *
except:
    os.system('pip install turtle')
    from turtle import *
try:
    from math import *
except:
    os.system('pip install math')
    from math import *
 
# Based on C implementation
 
iter = 3000
diskRatio = .7 #.5
 
factor = .5 + sqrt(1.25)
 
screen = getscreen()
 
#(winWidth, winHeight) = screen.screensize()
 
#x = winWidth/2.0
 
#y = winHeight/2.0
 
x = 0.0
y = 0.0
 
maxRad = pow(iter,factor)/iter;
 
#bgcolor("light blue")
 
hideturtle()
 
tracer(0, 0)
 
for i in range(iter+1):
    r = pow(i,factor)/iter;

    if r/maxRad < .2:
        pencolor("black")
    if r/maxRad < .3:
        pencolor('#808000') #olive
    elif r/maxRad < .34:
        pencolor('#5E2612') #sepia
    elif r/maxRad < .4: #.4:
        pencolor('#CD3700') #orangered3
    elif r/maxRad < diskRatio:
        pencolor('#5E2612') #sepia
    elif r/maxRad == diskRatio:
        pencolor('#FFA500') #orange
    elif r/maxRad < .85:
        pencolor('#FFA500') #orange
    elif r/maxRad < .95:
        pencolor('#FFC125') #goldenrod
    else:
        pencolor('#FFD700') #gold1 #("yellow")
 
    theta = 2*pi*factor*i;
 
    up()
 
    setposition(x + r*sin(theta), y + r*cos(theta))
 
    down()
 
    circle(10.0 * i/(1.0*iter))
 
update()
 
done()
 