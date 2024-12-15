import turtle
import time

window = turtle.Screen()
window.title("PaddleGame")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Generic Variables
player_score = 0
cpu_score = 0

DEBUG = True

# Paddle A
a_paddle = turtle.Turtle()
a_paddle.speed(0)
a_paddle.shape("square")
a_paddle.shapesize(stretch_wid=5, stretch_len=1)
a_paddle.color("white")
a_paddle.penup()
a_paddle.goto(-350, 0)

# Paddle B
b_paddle = turtle.Turtle()
b_paddle.speed(0)
b_paddle.shape("square")
b_paddle.shapesize(stretch_wid=5, stretch_len=1)
b_paddle.color("white")
b_paddle.penup()
b_paddle.goto(340, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

pen = turtle.Turtle()
pen.color("white")
pen.hideturtle()  # Nascondi la tartaruga (opzionale)
pen.penup()       # Non vogliamo che lasci tracce mentre si muove
pen.goto(0, 240)
pen.write(f"{player_score}  -  {cpu_score}", align="center", font=("Arial", 30, "bold"))

# Debug lines ---------------------------------------------------
if DEBUG:
    # Dx Game over line
    mid_red = turtle.Turtle()
    mid_red.speed(0)
    mid_red.shape("square")
    mid_red.shapesize(stretch_wid=100, stretch_len=0.01)
    mid_red.color("red")
    mid_red.penup()
    mid_red.goto(0, 0)

    # Dx Game over line
    go_dx_red = turtle.Turtle()
    go_dx_red.speed(0)
    go_dx_red.shape("square")
    go_dx_red.shapesize(stretch_wid=100, stretch_len=0.01)
    go_dx_red.color("red")
    go_dx_red.penup()
    go_dx_red.goto(340, 0)

    # Sx Game over line
    go_sx_red = turtle.Turtle()
    go_sx_red.speed(0)
    go_sx_red.shape("square")
    go_sx_red.shapesize(stretch_wid=100, stretch_len=0.01)
    go_sx_red.color("red")
    go_sx_red.penup()
    go_sx_red.goto(-350, 0)

    # Dx Paddle collision line
    pad_dx_red = turtle.Turtle()
    pad_dx_red.speed(0)
    pad_dx_red.shape("square")
    pad_dx_red.shapesize(stretch_wid=100, stretch_len=0.01)
    pad_dx_red.color("red")
    pad_dx_red.penup()
    pad_dx_red.goto(330, 0)

    # Sx Paddle collision line
    pad_sx_red = turtle.Turtle()
    pad_sx_red.speed(0)
    pad_sx_red.shape("square")
    pad_sx_red.shapesize(stretch_wid=100, stretch_len=0.01)
    pad_sx_red.color("red")
    pad_sx_red.penup()
    pad_sx_red.goto(-340, 0)

# End Debug lines ---------------------------------------------

# Functions ---------------------------------------------------

def a_paddle_up():
    if a_paddle.ycor() < 250:
        a_paddle.sety(a_paddle.ycor() + 20)

def a_paddle_down():
    if a_paddle.ycor() > -240:
        a_paddle.sety(a_paddle.ycor() - 20)

def b_paddle_up():
    if b_paddle.ycor() < 250:
        b_paddle.sety(b_paddle.ycor() + 20)

def b_paddle_down():
    if b_paddle.ycor() > -240:
        b_paddle.sety(b_paddle.ycor() - 20)

def update_score():
    pen.clear()  # Cancella il vecchio testo
    pen.write(f"{player_score}  -  {cpu_score}", align="center", font=("Arial", 30, "bold"))

# End Functions ---------------------------------------------------

window.listen()

# a_paddle UP/DOWN
window.onkeypress(a_paddle_up, "w")
window.onkeypress(a_paddle_up, "W")
window.onkeypress(a_paddle_down, "s")
window.onkeypress(a_paddle_down, "S")

# b_paddle UP/DOWN
window.onkeypress(b_paddle_up, "Up")
window.onkeypress(b_paddle_down, "Down")

#Main game loop
while True:
    window.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Board checking -----------------------------------------------

    # Vertical check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Horizontal check
    if ball.xcor() > 340:
        ball.setx(0)
        ball.sety(0)
        player_score += 1
        update_score()  
        time.sleep(0.5)
        ball.dx *= -1

    if ball.xcor() < -350:
        ball.setx(0)
        ball.sety(0)
        cpu_score += 1
        update_score()  
        time.sleep(0.5)
        ball.dx *= -1
    
    # End Board checking -----------------------------------------------

    if ball.xcor() > 330 and (ball.ycor() < b_paddle.ycor() + 55 and ball.ycor() > b_paddle.ycor() - 55):
        ball.setx(330)
        ball.dx *= -1
        
    if ball.xcor() < -340 and (ball.ycor() < a_paddle.ycor() + 55 and ball.ycor() > a_paddle.ycor() - 55):
        ball.setx(-340)
        ball.dx *= -1

    time.sleep(0.01)