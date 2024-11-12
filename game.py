import turtle #import  the turtle graphics module
import time #import time module for handling delays 
import random #import random module for generation random position for the food 
 
 #initial delay for the game speed
delay = 0.1

# initial score values
score = 0  #current score
high_score = 0  #highest score achieved

# set up the screen
wn = turtle.Screen()  #create screen object
wn.title("Snake Game") #set title of the window
wn.bgcolor("green")    #set the bgcolor of window
wn.setup(width=600, height=600) #set dimension of window
wn.tracer(0)  # turn off the automatic screen updates to manually control updates

# snake head of circle
head = turtle.Turtle() #create a turtle object for snake head
head.speed(0)  #animation speed of turtle (0=fastest)
head.shape("square") #set the shape of head
head.color("black") #set the color of head
head.penup()  #prevent drawing lines as head moves
head.goto(0, 0)   #start head at the center of screen
head.direction = "stop"   #initial direction of head is stopped

# snake food
food = turtle.Turtle() #create a turtle object for food
food.speed(0) #aniamtion speed of turtle
food.shape("circle") #set shape of food 
food.color("red")  #set color of food 
food.penup() #prevent drawing lines as food moves 
food.goto(0, 100)  #start food ata fixed position on the screen

#list to hold snake segments (body parts) 
segments = []

# pen for writing score
pen = turtle.Turtle() #create a turle object for the pen
pen.speed(0)  #animation speed of turle 
pen.shape("square")  #set the shape of pen (not visible)
pen.color("white")  #set color of pen text
pen.penup()  #prevent drawing lines 
pen.hideturtle()  #hide the turle cursor
pen.goto(0, 260)   #position the pen at the top center 
pen.write("score: 0 high score: 0", align="center", font=("courier", 24, "normal")) #initial score display

# function for movement and stuff
def go_up():
    if head.direction != "down": #prevent the snake from moving in opposite direction
        head.direction = "up" #change the direction to up

def go_down():
    if head.direction != "up": #prevent the snake from moving in opposite direction
        head.direction = "down" #change the direction to down

def go_left():
    if head.direction != "right": #prevent the snake from moving in opposite direction
        head.direction = "left"  #change the direction to left 

def go_right():
    if head.direction != "left":  #prevent the snake from moving in opposite direction
        head.direction = "right"  #change the direction to right

#function to move the snake 
def move():
    if head.direction == "up":   #if the direction is up
        y = head.ycor()  #get the current y-coordinate 
        head.sety(y + 20) #move head up by 20pixels

    if head.direction == "down":  #if the direction is down
        y = head.ycor()   #get the current y-coordinate 
        head.sety(y - 20)   #move head down by 20 pixels

    if head.direction == "left":   #if the direction is left
        x = head.xcor()             #get the current x-coordinate
        head.setx(x - 20)            #move head left by 20 pixels

    if head.direction == "right":     #if the direction is right
        x = head.xcor()             #get the current x-coordinate
        head.setx(x + 20)            #move head right by 20 pixels

# keyboard bindings/setting up key press
wn.listen()  #listen for keyboard input
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# main game loop
while True:
    wn.update()  #update the screen

    # check for collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1) #pause the game for a second
        head.goto(0, 0)  #move the head back to starting position
        head.direction = "stop" #stop the head movement

        # hide the bpdy segments
        for segment in segments:
            segment.goto(1000, 1000) #move up the segment off the screen

        segments.clear() #clear the  segment list

        # reset the score and delay
        score = 0
        delay = 0.1

         #update the score display
        pen.clear() #clear the previous score
        pen.write("score: {} high score: {}".format(score, high_score), align="center", font=("courier", 24, "normal"))

    # check for collision with the food
    if head.distance(food) < 20:
        # move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y) #move food to a new position 

        # add a new segment to snake's body 
        new_segment = turtle.Turtle() #create a new turle object
        new_segment.speed(0) #aniamtion speed of turtle 
        new_segment.shape("square")#set shape of segment
        new_segment.color("grey")#set color of segment 
        new_segment.penup()#prevent drawing lines
        segments.append(new_segment)# add segment to the list 

        #shorten delay to increase game speed
        delay -= 0.01

        # increase the score
        score += 10

        if score > high_score:#check if current score is greater than high score  
            high_score = score  #update the high score

        pen.clear()  #clear previous score display 
        pen.write("score: {} high score: {}".format(score, high_score), align="center", font=("courier", 24, "normal"))

    # move the segments in reverse order 
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()#get x-coordinate of previous segment
        y = segments[i - 1].ycor()#get y-coordinate of previous segment
        segments[i].goto(x, y)#move current segment to previous segemnt's position 

        
    #move segment 0 to position of the head
    if len(segments) > 0:
        x = head.xcor()#get x-coordinate of the head
        y = head.ycor()#get y-coordinate of the head
        segments[0].goto(x, y)#move segment 0 to the head's position

    move()#move the snake 

    # check for collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20: #check if the head collides with any segment
            time.sleep(1) #pause game for a second 
            head.goto(0, 0)#move head back the starting position 
            head.direction = "stop" #stop the head's movement

            # hide the body segments
            for segment in segments:
                segment.goto(1000, 1000)#move the segment off the screen 

            segments.clear()#clear the segment list 

            # reset the score and delay 
            score = 0
            delay =0.1

          #update score display 
            pen.clear()#clear previous score display
            pen.write("score: {} high score: {}".format(score, high_score), align="center", font=("courier", 24, "normal"))

    time.sleep(delay)#pause the loop to control the game speed 

wn.mainloop() #keep the window open 
