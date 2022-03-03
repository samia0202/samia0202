# TENNIS- FINAL DRAFT
# Score variables
import os
import time
import turtle
import turtle as t

from easygui import buttonbox

# splash screen
image = "starterupdated.gif"

title = "Tennis! - The Game"

msg = "Hello Player! Welcome to Tennis! :) HOW TO PLAY: USE KEYS TO MOVE THE TENNIS RACKET( A, S , UP AND DOWN KEYS) . IF YOU MISS THE BALL THE OTHER PLAYER SCORES AND VICE VERSA. TO PLAY ANOTHER ROUND CLICK THE 'X' BUTTON. *******PLEASE MAKE SURE THE CAPS LOCK IS OFF.********* "

choices = ["♡START GAME♡"]
reply = buttonbox(msg=msg, title=title, choices=choices, image=image)

# score variable

# timer_clock = 0
player_a_score = 0
player_b_score = 0

sc = t.Screen()  # window

sc.title("Tennis!")  # Giving name
sc.bgcolor('#77dd77')  # background colour

sc.setup(width=900, height=600)  # setup window
sc.tracer(0)  # which speed up the game.
sc.register_shape('leftracket.gif', None)
sc.register_shape('rightracket.gif')
# building the tennis net
middle_net = t.Turtle()
middle_net.shape("square")
middle_net.color('white')
middle_net.shapesize(stretch_wid=50, stretch_len=0.5)
middle_net.goto(0, 0)  # position of net

print(turtle.getshapes())

# left paddle
paddle_left = t.Turtle()
paddle_left.shape('leftracket.gif')
paddle_left.speed(10)  # speed of paddle
paddle_left.color('white')
paddle_left.shapesize(stretch_wid=-1, stretch_len=1)  # size of paddle
paddle_left.penup()
paddle_left.goto(-320, 0)  # position of paddle

# Creating a right paddle for the game
paddle_right = t.Turtle()
paddle_right.speed(10)
paddle_right.shape('rightracket.gif')
paddle_right.shapesize(stretch_wid=-1, stretch_len=1)
paddle_right.color('white')
paddle_right.penup()
paddle_right.goto(320, 0)

# Creating a pong ball for the game

ball = t.Turtle()
ball.speed(10)
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.goto(0, 0)
ball_dx = 1  # Setting up the pixels for the ball movement.
ball_dy = 1

# Creating a pen for updating the Score


pen = t.Turtle()
pen.speed(0)
pen.color("pink")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write('Player A: 0                Player B: 0 ', align="center", font=('Monaco', 24, "normal"))


def paddle_left_up():
    y = paddle_left.ycor()
    y = y + 30  # paddle speeds
    paddle_left.sety(y)


# Moving the left paddle down

def paddle_left_down():
    y = paddle_left.ycor()
    y = y - 30
    paddle_left.sety(y)


# Moving the right paddle up

def paddle_right_up():
    y = paddle_right.ycor()
    y = y + 30
    paddle_right.sety(y)


# Moving right paddle down

def paddle_right_down():
    y = paddle_right.ycor()
    y = y - 30
    paddle_right.sety(y)


# Keyboard binding

sc.listen()

sc.onkeypress(paddle_left_up, "a")
sc.onkeypress(paddle_left_down, "s")
sc.onkeypress(paddle_right_up, "Up")
sc.onkeypress(paddle_right_down, "Down")

while True:
    # Game code here

    sc.update()

    # Moving the ball

    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # setting up the border
    if ball.ycor() > 290:  # Right top paddle Border
        ball.sety(290)
        ball_dy = ball_dy * -1

    if ball.ycor() < -290:  # Left top paddle Border
        ball.sety(-290)
        ball_dy = ball_dy * -1

    # timer_clock = timer_clock + 1
    # pen.clear()
    # pen.write("Timer: {} ".format(timer_clock),
    # align="center", font=('Monaco', 24, "normal"))

    if ball.xcor() > 340:  # right width paddle Border
        ball.goto(0, 0)
        ball_dx *= -1
        time.sleep(1)
        player_a_score += 1
        pen.clear()
        pen.write("Player A: {}             Player B: {} ".format(player_a_score, player_b_score), align="center",
                  font=('Monaco', 24, "normal"))

    if (ball.xcor()) < -340:  # Left width paddle Border
        ball.goto(0, 0)
        ball_dx *= -1
        time.sleep(1)
        player_b_score += 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score, player_b_score),
                  align="center", font=('Monaco', 24, "normal"))

    # Handling the collisions with paddles.

    if (ball.xcor() > 320) and (ball.xcor() < 340) and (
            paddle_right.ycor() + 100 > ball.ycor() > paddle_right.ycor() - 100):
        ball.setx(320)
        ball_dx = ball_dx * -1
        os.system("afplay tennissound.wav")

    if (ball.xcor() < -320) and (ball.xcor() > -340) and (
            paddle_left.ycor() + 100 > ball.ycor() > paddle_left.ycor() - 100):
        ball.setx(-320)
        ball_dx = ball_dx * -1
        os.system("afplay tennissound.wav")
