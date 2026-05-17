import turtle as t

def move_forward(brush):
    brush.fd(10)
def move_backward(brush):
    brush.bk(10)
def turn_left(brush):
    brush.left(5)
def turn_right(brush):
    brush.right(5)
def clear_screen(brush):
    brush.clear()
    brush.pu()
    brush.home()
    brush.pd()

brush = t.Turtle()
brush.speed(0)

screen = t.Screen()
screen.listen()
screen.onkeypress(key = "w", fun = lambda: move_forward(brush))
screen.onkeypress(key = "a", fun = lambda: turn_left(brush))
screen.onkeypress(key = "s", fun = lambda: move_backward(brush))
screen.onkeypress(key = "d", fun = lambda: turn_right(brush))
screen.onkey(key = "c", fun = lambda: clear_screen(brush))
screen.exitonclick()