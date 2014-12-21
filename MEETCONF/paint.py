import turtle

turtle.shape("turtle")
turtle.speed(9)

#Stamp 1-triangle
def Stamp_1(x,y):
    turtle.pensize(2)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x+20,y+20)
    turtle.goto(x+40,y)
    turtle.goto(x,y)

#Stamp_2-MEET
def Stamp_2(x,y):
    turtle.penup()
    turtle.pencolor("blue")
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x,y+50)
    turtle.goto(x+20,y+30)
    turtle.goto(x+40,y+50)
    turtle.goto(x+40,y)
    turtle.penup()
    turtle.pencolor("orange")
    turtle.goto(x+50,y)
    turtle.pendown()
    turtle.goto(x+50,y+50)
    turtle.goto(x+70,y+50)
    turtle.penup()
    turtle.goto(x+50,y+25)
    turtle.pendown()
    turtle.goto(x+70,y+25)
    turtle.penup()
    turtle.goto(x+50,y)
    turtle.pendown()
    turtle.goto(x+70,y)
    turtle.penup()
    turtle.pencolor("orange")
    turtle.goto(x+80,y)
    turtle.pendown()
    turtle.goto(x+100,y)
    turtle.goto(x+100,y+50)
    turtle.goto(x+80,y+50)
    turtle.penup()
    turtle.goto(x+100,y+25)
    turtle.pendown()
    turtle.goto(x+80,y+25)
    turtle.penup()
    turtle.pencolor("blue")
    turtle.goto(x+130,y)
    turtle.pendown()
    turtle.goto(x+130,y+50)
    turtle.penup()
    turtle.goto(x+110,y+50)
    turtle.pendown()
    turtle.goto(x+150,y+50)

def Clear():
    turtle.clear()
    

    
turtle.onscreenclick(Stamp_1,btn=1)
turtle.onscreenclick(Stamp_2,btn=3)

def swich_color1():
    turtle.color("purple")

def swich_color2():
    turtle.color("green")

def swich_color3():
    turtle.color("red")

def swich_color4():
    turtle.color("pink")

def swich_color5():
    turtle.color("brown")

turtle.getscreen().onkeypress(swich_color1,"1")
turtle.getscreen().onkeypress(swich_color2,"2")
turtle.getscreen().onkeypress(swich_color3,"3")
turtle.getscreen().onkeypress(swich_color4,"4")
turtle.getscreen().onkeypress(swich_color5,"5")
turtle.getscreen().onkeypress(Clear,"space")


turtle.getscreen().listen()
turtle.mainloop()
