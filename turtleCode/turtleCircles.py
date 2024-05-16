import turtle

# define the loop to draw a circle
def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.pendown()

# define variables
tommy = turtle.Turtle() # shortcut

# define the shape of the arrow and its speed
tommy.shape("turtle")
tommy.speed(5)

# change the background color to black
turtle.bgcolor('black')

# Side to Side
draw_circle(tommy, "purple", 100, 100, -100)
draw_circle(tommy, "green", 100, 0, -100)
draw_circle(tommy, "orange", 100, -100, -100)

# Up Down
draw_circle(tommy, "blue", 100, 0, 0)
draw_circle(tommy, "green", 100, 0, -100)
draw_circle(tommy, "red", 100, 0, -200)

turtle.done()