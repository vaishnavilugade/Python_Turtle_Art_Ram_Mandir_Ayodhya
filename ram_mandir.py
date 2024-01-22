import turtle

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Draw a circle with black and orange fill in the middle of the screen
def draw_circle():
    pen.penup()
    pen.goto(0, -400)  # Move to the center of the screen
    pen.pendown()
    
    pen.color("black", "orange")
    pen.begin_fill()
    pen.circle(420)
    pen.end_fill()

# Main program
draw_circle()
pen.color("black")
pen.pendown()
pen.begin_fill()
pen.fillcolor("black")
pen.right(179)
pen.forward(340)
pen.right(90)
pen.forward(180)
pen.right(90)
pen.forward(30)
pen.left(90)
pen.forward(30)
pen.right(90)
pen.forward(30)
pen.left(90)
pen.forward(170)
pen.left(90)
pen.forward(10)
pen.right(90)
pen.forward(7)
pen.left(90)
pen.forward(15)
pen.right(90)
pen.forward(10)
pen.right(90)
pen.forward(35)
pen.left(89)

#top1
pen.forward(45)
pen.right(7)
pen.forward(45)
pen.right(6)
pen.forward(45)
pen.right(5)
pen.forward(45)

pen.left(115)
pen.forward(10)
pen.right(90)
pen.forward(5)
pen.right(100)
pen.forward(10)
pen.left(80)
pen.forward(10)


pen.left(3)
pen.forward(30)
pen.left(80)
pen.forward(30)
pen.right(140)
pen.forward(30)
pen.right(110)
pen.forward(20)
pen.left(7)
pen.forward(10)
pen.left(2)
pen.forward(10)
pen.left(2)
pen.forward(10)
pen.left(2)
pen.forward(10)
pen.left(80)
pen.forward(10)
pen.right(90)
pen.forward(5)
pen.right(90)
pen.forward(10)

#top2
pen.left(110)
pen.forward(20)
pen.right(2)
pen.forward(10)
pen.right(2)
pen.forward(10)
pen.right(2)
pen.forward(10)
pen.right(1)
pen.forward(20)
pen.right(1)
pen.forward(20)
pen.right(1)
pen.forward(10)
pen.right(1)
pen.forward(10)
pen.right(1)
pen.forward(10)
pen.right(1)
pen.forward(10)
pen.right(1)
pen.forward(10)
pen.right(2)
pen.forward(10)
pen.right(2)
pen.forward(10)
pen.right(2)
pen.forward(10)
pen.left(85)
pen.forward(25)

pen.left(90)
pen.forward(10)
pen.right(90)
pen.forward(15)
pen.left(90)
pen.forward(10)
pen.right(90)
pen.forward(15)

pen.left(90)
pen.forward(15)

pen.right(90)
pen.forward(15)
pen.left(90)
pen.forward(10)
pen.right(90)
pen.forward(15)

pen.left(90)
pen.forward(15)
pen.right(90)
pen.forward(10)
pen.left(90)
pen.forward(15)

pen.right(90)
pen.forward(15)
pen.left(90)
pen.forward(10)
pen.right(90)
pen.forward(15)

#top start
pen.left(90)
pen.forward(10)
pen.right(90)
pen.forward(10)
pen.left(90)
pen.forward(10)
pen.left(70)
pen.forward(20)
pen.right(130)
pen.forward(25)
pen.right(125)
pen.forward(20)
pen.left(95)
pen.forward(10)



pen.right(90)
pen.forward(10)


pen.left(90)
pen.forward(15)
pen.right(90)
pen.forward(10)
pen.left(90)
pen.forward(15)

pen.right(90)
pen.forward(15)
pen.left(90)
pen.forward(10)
pen.right(90)
pen.forward(15)

pen.left(90)
pen.forward(15)
pen.right(90)
pen.forward(10)
pen.left(90)
pen.forward(15)

pen.right(90)
pen.forward(15)
pen.left(90)
pen.forward(10)
pen.right(90)
pen.forward(15)


pen.left(90)
pen.forward(15)
pen.right(90)
pen.forward(10)
pen.left(90)
pen.forward(15)

pen.right(90)
pen.forward(15)
pen.left(90)
pen.forward(10)





pen.left(90)
pen.forward(15)
pen.right(90)
pen.forward(10)
pen.left(90)
pen.forward(15)

pen.right(90)
pen.forward(15)
pen.left(90)
pen.forward(10)
pen.right(90)
pen.forward(15)

pen.left(90)
pen.forward(15)
pen.right(90)
pen.forward(10)
pen.left(90)
pen.forward(15)

pen.right(90)
pen.forward(15)
pen.left(90)
pen.forward(10)
pen.right(90)
pen.forward(15)

pen.left(90)
pen.forward(10)
pen.right(90)
pen.forward(10)
pen.left(90)
pen.forward(10)
pen.left(70)
pen.forward(20)
pen.right(130)
pen.forward(25)
pen.right(125)
pen.forward(20)
pen.left(95)
pen.forward(10)




pen.right(90)
pen.forward(10)
pen.left(90)
pen.forward(15)

pen.right(90)
pen.forward(15)
pen.left(90)
pen.forward(10)
pen.right(90)
pen.forward(15)

pen.left(90)
pen.forward(15)
pen.right(90)
pen.forward(10)
pen.left(90)
pen.forward(15)

pen.right(90)
pen.forward(15)
pen.left(90)
pen.forward(10)
pen.right(90)
pen.forward(15)

pen.left(90)
pen.forward(30)
pen.left(90)
pen.forward(40)
pen.right(45)
pen.forward(35)
pen.right(90)
pen.forward(35)
pen.right(45)
pen.forward(40)


pen.left(90)
pen.forward(20)

pen.right(120)
pen.forward(20)
pen.left(30)
pen.forward(160)
pen.left(90)
pen.forward(30)
pen.right(90)
pen.forward(210)
pen.right(89)
pen.forward(300)
pen.end_fill()

def print_text():
    pen.penup()
    pen.color("orange")
    pen.goto(0, -190)  # Move to the bottom center
    pen.pendown()
    pen.write("!! जय श्री राम !!", align="center", font=("Arial", 50, "bold"))
print_text()
# Keep the window open
turtle.done()
