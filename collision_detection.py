import turtle


width = 500     #X Axis
height = 500    #Y Axis
delay = 400 #milliseconds

offsets = {
    "Up": (0, 20), 
    "Down": (0, -20), 
    "Left": (-20, 0), 
    "Right": (20, 0)
}

def go_up():
    global snake_direction
    if snake_direction != "Down":
        snake_direction = "Up"

def go_right():
    global snake_direction
    if snake_direction != "Left":
        snake_direction = "Right"

def go_down():
    global snake_direction
    if snake_direction != "Up":
        snake_direction = "Down"

def go_left():
    global snake_direction
    if snake_direction != "Right":
        snake_direction = "Left"


def game_loop():
    stamper.clearstamps() #remove existing stamps make by stamper

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]


    #Check for collisions
    if new_head in snake or new_head[0] < - width/2 or new_head[0] > width/2 or new_head[1] < - height/2 or new_head[1] > height /2:
        #  Left Wall, Right Wall, Bottom Wall, Top Wall, 
        turtle.bye()
    else:
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
        turtle.ontimer(game_loop, delay)
    



#Creating the window where we do the game
screen = turtle.Screen()
screen.setup(width, height)
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0) #Disables automatic animation

#Event handlers
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")
screen.onkey(go_down, "Down")




#creating a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

#Creating snake representation
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
snake_direction = "Up"

#Draw the snake for the first time:
for segment in snake:
    stamper.goto(segment[0], segment[1]) #X Y coordinates
    stamper.stamp()


#Set animation in motion
game_loop()
turtle.done()
