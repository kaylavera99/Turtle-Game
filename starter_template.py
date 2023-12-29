import turtle

width = 500
height = 500


#Creating the window where we do the game
screen = turtle.Screen()
screen.setup(width, height)
screen.title("Snake Game")
screen.bgcolor("cyan")


#creating a turtle to do your bidding
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")


#Your turtle awaits your command
my_turtle.forward(100) #sample

#This statement (or an equivalent) is needed at the end of all your turtle programs
turtle.done()
