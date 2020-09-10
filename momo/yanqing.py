import turtle as t


def Screen():
    # t.setup(width=1024, height=960, startx=100, starty=100)
    t.bgcolor("orange")
    t.screensize(2000, 1500, "#0ffff0")
    t.title("Hello!")


def Draw0():
    t.penup()
    t.pensize(5)  # pen's width
    # t.color("black")       #default is black
    # t.forward(10)
    t.circle(100, steps=3)
    t.pendown()  # default is down
    t.goto(-100, -200)
    t.penup()


def Draw1():
    t.penup()
    t.goto(100, 100)
    t.pendown()  #
    t.begin_fill()
    t.color("yellow")
    t.circle(50)
    t.end_fill()
    t.penup()


def Draw2():
    t.penup()
    t.goto(200, 100)
    t.pendown()
    t.begin_fill()  #
    t.color("blue")  #
    t.fillcolor("black")  #
    t.circle(50)
    t.end_fill()
    t.penup()


'''
turtle.write(arg, move=False, align="left", font=("Arial", 8, "normal"))
    Parameters:    
        arg – object to be written to the TurtleScreen
        move – True/False
        align – one of the strings “left”, “center” or right”
        font – a triple (fontname, fontsize, fonttype) 
'''


def Write():
    t.penup()
    # t.goto(0,0)
    # t.write("Color Draw",font=("Times",18,"bold"))
    t.write("Home = ", False, align="left")
    t.write((0, 0), True)
    t.clear()


def Draw3():
    t.penup()
    t.setpos(200, 200)
    t.pendown()
    t.pencolor("blue")
    t.right(50)  # Rotate right
    t.forward(100)  #
    t.dot(10, "red")  #
    t.left(50 + 180)  # Ritate left
    t.color("blue")
    t.speed(10)
    t.forward(100)


def Draw4():
    t.penup()
    t.goto(100, 100)
    t.pen(fillcolor="red", pencolor="black", pensize=10)
    t.pendown()
    t.circle(50)
    t.goto(-100, -100)
    t.pencolor("#ffff00")  # "#%02x%02x%02x" % (r, g, b)
    t.width(2)
    t.forward(100)
    t.left(180)


def Draw5():
    # t.color("black","red")
    # t.begin_fill()
    t.speed(10)
    t.circle(80)
    # t.end_fill()
    t.clear()
    t.clearscreen()
    t.delay(0)


def main():
    Screen()
    # Write()
    # while(True):
    #    Draw5()
    Draw4()
    # t.mainloop()    #stop
    # t.bye()         #close window
    t.exitonclick()


if __name__ == "__main__":
    main()