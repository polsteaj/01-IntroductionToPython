"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Alec Polster.
"""
import rosegraphics as rg
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
window = rg.TurtleWindow()
my_turtle = rg.SimpleTurtle('turtle')
my_turtle.pen = rg.Pen('blue', 10)
my_turtle.speed = 10

your_turtle = rg.SimpleTurtle()
your_turtle.pen = rg.Pen('red', 5)
your_turtle.speed = 10
your_turtle.pen_up()
your_turtle.forward(3)
your_turtle.pen_down()
size = 300
for k in range(15):
    my_turtle.draw_square(size)
    my_turtle.pen_up()
    my_turtle.right(45)
    my_turtle.forward(10)
    my_turtle.left(45)
    my_turtle.pen_down()
    your_turtle.draw_square(size-100)
    your_turtle.pen_up()
    your_turtle.right(45)
    your_turtle.forward(10)
    your_turtle.left(45)
    your_turtle.pen_down()
    size = size - 20

window.close_on_mouse_click()
