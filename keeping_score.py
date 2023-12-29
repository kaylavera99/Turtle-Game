import turtle
import random


width = 500     #X Axis
height = 500    #Y Axis
delay = 400 #milliseconds
food_size = 10

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

        #Check food collision
        if not food_collision():
            snake.pop(0)  #Keep the snake the same length unless fed

        #Draw snake for the first time
        for segment in snake:
            stamper.goto(segment[0], segment[1]) #X Y coordinates
            stamper.stamp()
        
        screen.title(f"Snake Game: Score = {score}")

        #Refresh screen
        screen.update()

        #Rinse and repeat
        turtle.ontimer(game_loop, delay)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    distance = ((y2 - y1)**2 + (x2-x2) **2) ** 0.5 #Pythagoras
    return distance

def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score +=1 #score = score + 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False


def get_random_food_pos():
    x = random.randint(-width / 2 + food_size, width / 2 - food_size)
    y = random.randint(-height / 2 + food_size, height / 2 - food_size)
    return (x, y)



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
score = 0

#Creating snake representation
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
snake_direction = "Up"


#Draw the snake for the first time:
for segment in snake:
    stamper.goto(segment[0], segment[1]) #X Y coordinates
    stamper.stamp()

#Food

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(food_size /20)
food.penup()
food_pos=get_random_food_pos()
food.goto(food_pos)

#Set animation in motion
game_loop()
turtle.done()