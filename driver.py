'''
Jovienne Trotta
CS 5001 | Fall 2022
Lab 3: A Shape Collection

This is the "driver file" or the starting point for my code execution.
The program on this page will give users a choice between two different scenes, then draw them.
'''

import turtle as t
import shapeLib as sLib
from random import randint

#this will test each function
def test():
    sLib.blocks(70,60,30)
    sLib.tower(60,80,100)
    sLib.draw_circle(20,20,100)
    sLib.triangle(5,10,15,True,"cyan")
    sLib.bar(40,40,60,False,"black")
    sLib.star(-160,160,30,True,"red")
    sLib.tree(-10,-200,200,False,0)
    sLib.mountain(50,50,600,True,"purple")
    sLib.pentagon(-10,-10,50,False,"green")
    sLib.flower_one(10,10,100,True,"orange")
    sLib.flower_two(-40,-40,100,False,"yellow")
    sLib.wave(75,-100,60,True,"pink")
    
#this function will draw my first scene
def scene_one():
    t.bgcolor("beige")
    sLib.star(-160,160,30,True,"navy")
    sLib.tree(-10,-200,200,True,0)

#this function will draw my second scene
def scene_two():
    t.speed(10)
    t.bgcolor("light blue")
    sLib.star(randint(-300, 300),randint(200, 300),5,True,"white")
    sLib.star(randint(-300, 300),randint(200, 300),5,True,"white")
    sLib.star(randint(-300, 300),randint(200, 300),5,True,"white")
    sLib.star(randint(-300, 300),randint(200, 300),5,True,"white")
    sLib.star(randint(-300, 300),randint(200, 300),5,True,"white")
    sLib.star(randint(-300, 300),randint(200, 300),5,True,"white")
    sLib.star(randint(-300, 300),randint(200, 300),5,True,"white")
    sLib.star(randint(-300, 300),randint(200, 300),5,True,"white")
    sLib.star(randint(-300, 300),randint(200, 300),5,True,"white")
    sLib.star(randint(-300, 300),randint(200, 300),5,True,"white")
    sLib.star(randint(-300, 300),randint(200, 300),5,True,"white")
    sLib.star(randint(-300, 300),randint(200, 300),5,True,"white")
    sLib.star(randint(-300, 300),randint(200, 300),5,True,"white")
    sLib.star(randint(-300, 300),randint(200, 300),5,True,"white")
    sLib.mountain(randint(-250, 50),randint(0, 50),randint(50, 200),True,"grey")
    sLib.mountain(randint(-250, 50),randint(0, 50),randint(50, 200),True,"grey")
    sLib.mountain(randint(-250, 50),randint(0, 50),randint(50, 200),True,"grey")
    sLib.mountain(randint(-250, 50),randint(0, 50),randint(50, 200),True,"grey")
    sLib.mountain(randint(-250, 50),randint(0, 50),randint(50, 200),True,"grey")
    sLib.tree(randint(-300, 50),randint(-50, 0),randint(50, 100),True,0)
    sLib.tree(randint(-300, 50),randint(-50, 0),randint(50, 100),True,0)
    sLib.tree(randint(-300, 50),randint(-50, 0),randint(50, 100),True,0)
    sLib.tree(randint(-300, 50),randint(-50, 0),randint(50, 100),True,0)
    sLib.tree(randint(-300, 50),randint(-50, 0),randint(50, 100),True,0)
    sLib.tree(randint(-300, 50),randint(-50, 0),randint(50, 100),True,0)
    sLib.flower_one(randint(-300, 50),randint(-200, -50),randint(5, 10),True,"pink")
    sLib.flower_two(randint(-300, 50),randint(-200, -50),randint(5, 10),True,"red")
    sLib.flower_one(randint(-300, 50),randint(-200, -50),randint(5, 10),True,"purple")
    sLib.flower_two(randint(-300, 50),randint(-200, -50),randint(5, 10),True,"yellow")
    sLib.flower_one(randint(-300, 50),randint(-200, -50),randint(5, 10),True,"pink")
    sLib.flower_two(randint(-300, 50),randint(-200, -50),randint(5, 10),True,"red")
    sLib.flower_one(randint(-300, 50),randint(-200, -50),randint(5, 10),True,"purple")
    sLib.flower_two(randint(-300, 50),randint(-200, -50),randint(5, 10),True,"yellow")
    sLib.flower_one(randint(-300, 50),randint(-200, -50),randint(5, 10),True,"pink")
    sLib.flower_two(randint(-300, 50),randint(-200, -50),randint(5, 10),True,"red")
    sLib.flower_one(randint(-300, 50),randint(-200, -50),randint(5, 10),True,"purple")
    sLib.flower_two(randint(-300, 50),randint(-200, -50),randint(5, 10),True,"yellow")
    sLib.flower_one(randint(-300, 50),randint(-200, -50),randint(5, 10),True,"pink")
    sLib.flower_two(randint(-300, 50),randint(-200, -50),randint(5, 10),True,"red")
    sLib.flower_one(randint(-300, 50),randint(-200, -50),randint(5, 10),True,"purple")
    sLib.flower_two(randint(-300, 50),randint(-200, -50),randint(5, 10),True,"yellow")
    sLib.wave(randint(60, 300),randint(-300, -100),randint(5, 50),True,"blue")
    sLib.wave(randint(60, 300),randint(-300, -100),randint(5, 50),True,"blue")
    sLib.wave(randint(60, 300),randint(-300, -100),randint(5, 50),True,"blue")
    sLib.wave(randint(60, 300),randint(-300, -100),randint(5, 50),True,"blue")
    sLib.wave(randint(60, 300),randint(-300, -100),randint(5, 50),True,"blue")
    sLib.wave(randint(60, 300),randint(-300, -100),randint(5, 50),True,"blue")
    sLib.wave(randint(60, 300),randint(-300, -100),randint(5, 50),True,"blue")
    sLib.wave(randint(60, 300),randint(-300, -100),randint(5, 50),True,"blue")
    sLib.wave(randint(60, 300),randint(-300, -100),randint(5, 50),True,"blue")
    sLib.wave(randint(60, 300),randint(-300, -100),randint(5, 50),True,"blue")
    sLib.wave(randint(60, 300),randint(-300, -100),randint(5, 50),True,"blue")
    sLib.wave(randint(60, 300),randint(-300, -100),randint(5, 50),True,"blue")
    sLib.wave(randint(60, 300),randint(-300, -100),randint(5, 50),True,"blue")
    sLib.wave(randint(60, 300),randint(-300, -100),randint(5, 50),True,"blue")
    sLib.wave(randint(60, 300),randint(-300, -100),randint(5, 50),True,"blue")
    sLib.wave(randint(60, 300),randint(-300, -100),randint(5, 50),True,"blue")
    sLib.wave(randint(60, 300),randint(-300, -100),randint(5, 50),True,"blue")
    sLib.wave(randint(60, 300),randint(-300, -100),randint(5, 50),True,"blue")
    sLib.wave(randint(60, 300),randint(-300, -100),randint(5, 50),True,"blue")
    sLib.wave(randint(60, 300),randint(-300, -100),randint(5, 50),True,"blue")
   
#this calls the main function and is the entry point into my program
#users have a choice of selecting which scene they'd like to see, then the program executes whichever scene they selected
def main():
    #test()
    scene_choice = input("What scene would you like to see? \nPlease enter: \n...'1' for the Maine State Flag \n...'2' for the Maine Wilderness \n: ")
    if scene_choice == "one" or scene_choice == "1":
        print("Thanks! You've selected the Maine State Flag.")
        scene_one()
    elif scene_choice == "two" or scene_choice == "2":
        print("Thanks! You've selected the Maine Wilderness.")
        scene_two()
    else:
        print("Sorry! That's not an option. Please enter 1 or 2.")
        exit()
    t.mainloop()

main()
