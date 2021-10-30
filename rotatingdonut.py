from vpython import *
canvas(background=color.magenta)
donut=ring(thickness=0.25,radius=0.5,color=vector(400,100,1))
chocolate=ring(thickness=0.25,radius=0.55,color=vector(0.4,0.2,0)) #since the chocolate coating on a donut is a slight thicker than the donut itself
rad=0
while True:
    rate(10)
    donut.pos=vector(3*cos(rad),sin(rad),0)   #to make the donut move not only in all directions but also in all planes
    chocolate.pos=vector(3*cos(rad),sin(rad),0) #same with the chocolate part
    rad=rad+0.05