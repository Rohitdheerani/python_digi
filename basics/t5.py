from turtle import *
speed(0)
start=200
goto(-150,-300)
while start > 0:
    forward(start)
    left(360/5)
    start-=10
    write(start,font=('arial',8,'normal'))

mainloop()