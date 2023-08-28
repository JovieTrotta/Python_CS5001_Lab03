'''
Jovienne Trotta
CS 5001 | Fall 2022
Lab 3: A Shape Collection

This program is part of our in-class recittion demonstration
'''

import turtle as t
import shapeLib as sLib

'''
go to function
moves turtle curser to new position
'''

def goto(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()


'''
block function
accepts x and y coordinates
'''

def block(x,y,size):
    goto(x,y)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.penup()
    t.home()
    t.pendown()


'''
tower function
draws a three block tower
'''

def tower(x,y,scale):
    block(x,y,scale)
    block(x+(scale*0.25),y+scale,scale*0.5)
    block(x+(scale*0.38),y+scale + scale*0.5,scale*0.25)

def tower_city():
    tower(0,0,64)
    tower(-40,0,32)
    tower(-60,0,16)

def main():
    t.speed(0)
    print("woot")
    #t.forward(100)
    #goto(20,20)
    #block(0,0,10)
    #tower(20,20,70)
    tower_city()

    t.mainloop()

main()