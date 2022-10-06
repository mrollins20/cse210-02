"""
This is the program that creates the different images for the card suites.
"""
import turtle

def main():
    """
    This contains all of the function calls. Use the functions below as needed.
    """
    _t = turtle.Turtle()
    
    #draw_spade(_t)
    #draw_heart(_t)
    #draw_red_star(_t)
    #draw_diamond(_t)
    #draw_part_circle(_t, (x=none), (y=none), 5, 5, "black")
def draw_clubs(_t):
    """
    Draws a clubs in the ceter of the screen. No parameters necessary.
    """
    draw_rectangle(_t, -100, -100, 300, 200, 0, "white", "black")
    draw_rectangle(_t, 0, 0, 50, 10, 0, "black", "black")
    draw_circle(_t, -45, 30, 25, "black", "black")
    draw_circle(_t, -20, 75, 25, "black", "black")
    draw_circle(_t, 5, 30, 25, "black", "black")

def draw_diamond(_t):
    """
    Draws a diamond in the center of the screen. No parameters necessary.
    """
    draw_rectangle(_t, -100, -100, 300, 200, 0, "white", "black")
    draw_right_triangle(_t, -41, 64, 40, 50, "red", "red", 0)
    draw_right_triangle(_t, -1, 24, 40, 60, "red", "red", 90)
    draw_right_triangle(_t, 39, 64, 40, 60, "red", "red", 180)
    draw_right_triangle(_t, -1, 104, 40, 60, "red", "red", 270)
        
#def draw_curve_right_triangle(_t, _x, _y, side, hype, fillcolor, pencolor, tilt):
#    """
#    Atomic shape used to create the triforce used on the shield.
#    _x, and _y are for coordinates
#    side is used for the triangle size
#    fillcolor is for the color inside of the circles
#    pencolor is for the circle borders
#    """
#    _t.up()
#    _t.goto(_x, _y)
#    _t.setheading(tilt)
#    _t.fillcolor(fillcolor)
#    _t.down()
#    _t.begin_fill()
#    _t.forward(side)
#    _t.left(90)
#    _t.forward(side)
#    _t.left(135)
#    hype = part_circle(_t, _x, _y, 50, 50, 3, "red")
#    _t.forward(part_circle(_t, 5, 5, 50, 50, 3, "red"))
#    _t.end_fill()
#    _t.up()
#def part_circle(_t, _x, _y, radius, ext, step, pencolor):
#    """
#    This is the atomic shape circle used for the ball on the sword and the shield in various places throughout.
#    _x, and _y are for coordinates
#    radius is used for the circle size
#    fillcolor is for the color inside of the circles
#    pencolor is for the circle borders
#    """
#    _t.pencolor(pencolor)
#    _t.up()
#    _t.goto(_x,_y)
#    _t.down()
#    _t.circle(radius, ext, step)
#    _t.speed(0)
    
def draw_circle(_t, _x, _y, radius, fillcolor, pencolor):
    """
    This is the atomic shape circle used for the ball on the sword and the shield in various places throughout.
    _x, and _y are for coordinates
    radius is used for the circle size
    fillcolor is for the color inside of the circles
    pencolor is for the circle borders
    """
    _t.color(pencolor, fillcolor)
    _t.begin_fill()
    _t.up()
    _t.goto(_x,_y)
    _t.down()
    _t.circle(radius)
    _t.end_fill()
    _t.speed(0)
    
def draw_red_star(_t):
    """
    Draws a red star in the center, could be used instead of the diamond. No parameters necessary.
    """
    draw_rectangle(_t, -100, -100, 300, 200, 0, "white", "black")
    draw_triangle(_t, -1, 64, 40, "red", "red", 120)
    draw_triangle(_t, -1, 24, 40, "red", "red", 180)
    draw_triangle(_t, 34, 44, 40, "red", "red", 150)
    draw_triangle(_t, -40, 64, 40, "red", "red", 210)
    draw_rectangle(_t, -40, 23, 41, 40, 0, "red", "red")
    
def draw_heart(_t):
    """
    Draws a red heart in the center of the screen. No parameters necessary.
    """
    draw_rectangle(_t, -100, -100, 300, 200, 0, "white", "black")
    draw_circle(_t, -20, 50, 25, "red", "red")
    draw_circle(_t, -45, 75, 25, "red", "red")
    draw_circle(_t, 5, 75, 25, "red", "red")
    draw_triangle(_t, -1, 64, 40, "red", "red", 180)
    draw_triangle(_t, -25, 92, 40, "red", "red", 197)
    draw_triangle(_t, 23, 80, 40, "red", "red", 163)

def draw_spade(_t):
    """
    Draws a spade in the center of the screen. No parameters necessary.
    """
    draw_rectangle(_t, -100, -100, 300, 200, 0, "white", "black")
    draw_rectangle(_t, 0, -10, 70, 10, 0, "black", "black")
    draw_circle(_t, -20, 50, 25, "black", "black")
    draw_circle(_t, -45, 25, 25, "black", "black")
    draw_circle(_t, 5, 25, 25, "black", "black")
    draw_triangle(_t, -15, 69, 40, "black", "black", 0)
    draw_triangle(_t, -40, 40, 40, "black", "black", -10)
    draw_triangle(_t, 5, 40, 40, "black", "black", 10)
        
def draw_right_triangle(_t, _x, _y, side, hype, fillcolor, pencolor, tilt):
    """
    Atomic shape used to create the triforce used on the shield.
    _x, and _y are for coordinates
    side is used for the triangle size
    fillcolor is for the color inside of the circles
    pencolor is for the circle borders
    """
    _t.up()
    _t.goto(_x, _y)
    _t.setheading(tilt)
    _t.fillcolor(fillcolor)
    _t.down()
    _t.begin_fill()
    _t.forward(side)
    _t.left(90)
    _t.forward(side)
    _t.left(135)
    _t.forward(hype)
    _t.end_fill()
    _t.up()
    
def draw_triangle(_t, _x, _y, side, fillcolor, pencolor, tilt):
    """
    Atomic shape used to create the triforce used on the shield.
    _x, and _y are for coordinates
    side is used for the triangle size
    fillcolor is for the color inside of the circles
    pencolor is for the circle borders
    """
    _t.up()
    _t.goto(_x, _y)
    _t.setheading(tilt)
    _t.fillcolor(fillcolor)
    _t.down()
    _t.begin_fill()
    for _i in range(3):
        _t.forward(side)
        _t.left(120)
    _t.end_fill()
    _t.up()

def draw_rectangle(_t, _x, _y, height, width, tilt, fillcolor, pencolor):
    """
    _x, and _y are for coordinates
    height and width are used for the rectangle size
    tilt is for the direction that the rectangle is tilted or not.
    fillcolor is for the color inside of the circles
    pencolor is for the circle borders
    """
    _t.setheading(tilt)
    _t.up()
    _t.goto(_x, _y)
    _t.down()
    _t.color(pencolor, fillcolor)
    _t.begin_fill()
    for _i in range(2):
        _t.forward(width)
        _t.left(90)
        _t.forward(height)
        _t.left(90)

    _t.right(90)
    _t.end_fill()
    _t.up()

if __name__== "__main__":
    main()
