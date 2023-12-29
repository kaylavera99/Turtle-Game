import turtle


width = 500
height = 500
delay = 400 #milliseconds


def move_snake():
    stamper.clearstamps() #remove existing stamps make by stamper

    new_head = snake[-1].copy()
    new_head[0] += 20

    #Add new head to snake body
    snake.append(new_head)

    #Remove last segment of snake
    snake.pop(0)

    #Draw snake for the first time
    for segment in snake:
        stamper.goto(segment[0], segment[1]) #X Y coordinates
        stamper.stamp()
    
    #Refresh screen
    screen.update()

    #Rinse and repeat
    turtle.ontimer(move_snake, delay)
    



#Creating the window where we do the game
screen = turtle.Screen()
screen.setup(width, height)
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0) #Disables automatic animation


#creating a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

#Creating snake representation
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]

#Draw the snake for the first time:
for segment in snake:
    stamper.goto(segment[0], segment[1]) #X Y coordinates
    stamper.stamp()


#Set animation in motion
move_snake()
turtle.done()
