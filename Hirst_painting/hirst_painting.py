import turtle as t
import random 

t.colormode(255)
brush = t.Turtle()
brush.penup()
brush.speed(0)

rgb_list = [(202, 160, 98), (232, 210, 99), (156, 19, 40), (162, 76, 40), (168, 165, 37), (149, 65, 84), (205, 137, 158), (134, 175, 194), (69, 95, 134), (151, 27, 22), (120, 182, 164), (39, 43, 63), (68, 29, 45), (223, 77, 50), (47, 129, 96), (199, 83, 122), (61, 46, 103), (71, 39, 36), (229, 166, 181), (40, 58, 54), (57, 159, 137), (62, 167, 178), (152, 208, 218), (240, 168, 159), (162, 208, 199), (79, 70, 35)]

x_init = -150
y_init = -150

brush.setpos(x_init, y_init)


def draw_row_dots(brush):
    """draws 10 dots in a row"""
    
    for _ in range(10):
        brush.dot(20, random.choice(rgb_list))
        brush.fd(50)

def move_row(brush, x_init, y_init):
    """uses setpos() to bring turtle to a new row"""

    y_init += 50
    brush.setpos(x_init, y_init)
    return y_init

for _ in range(10):
    draw_row_dots(brush)
    y_init = move_row(brush, x_init, y_init)

screen = t.Screen()
screen.exitonclick()