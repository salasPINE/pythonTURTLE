# turtleSpiral.py

import turtle
colors=['red', 'purple', 'blue', 'green', 'yellow', 'orange']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(160):
  t.pencolor(colors[x%6])
  t.width(x/100+1)
  t.forward(x)
  t.left(59)
# change the range value to make the spiral bigger or smaller
# change the width + to make each new line bigger
turtle.done()