import turtle

width = 500
height = 500
DELAY = 20 #Milliseconds between screen updates

def move_turtle():
    my_turtle.forward(1)
    my_turtle.right(1)
    screen.update()
    screen.ontimer(move_turtle, DELAY)



screen = turtle.Screen()
screen.setup(width, height)
screen.title("Program title")
screen.bgcolor("cyan")

screen.tracer(0) #turns off automatic animation


my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")


#set animation in motion
move_turtle()
turtle.done()