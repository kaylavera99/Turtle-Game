import turtle


width = 500
height = 500


#Creating the window where we do the game
screen = turtle.Screen()
screen.setup(width, height)
screen.title("Stamping")
screen.bgcolor("cyan")


#creating a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.color("red")
stamper.shapesize(50/20) 
stamper.stamp()
stamper.penup()
stamper.shapesize(10/20)
stamper.goto(100, 100)
stamper.stamp()


turtle.done()
