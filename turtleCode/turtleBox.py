import turtle

# shortcut to make it easier to write the code
t = turtle.Turtle()
t.shape("turtle")

# change background color to black
turtle.bgcolor('black')

# loops through the four colors to make a box
for c in ['red', 'green', 'blue', 'yellow']:
    t.color(c)
    t.forward(100)
    t.left(90)

turtle.exitonclick()