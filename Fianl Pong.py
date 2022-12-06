import turtle

wn = turtle.Screen()
wn.title("World Cup Pong")
wn.bgpic('field.gif')
wn.tracer(0) #stops the windows from updating

player_a_country = input('player a choose your country')
player_b_country = input('plater b choose your country')

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350,0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.dx = .1
ball.dy = .1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("{}: 0 {}: 0".format(player_a_country, player_b_country), align = "center", font = ("Courier", 24, "normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# keyboard bidning
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#main game loop
while True:
    wn.update()
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 254:
        ball.sety(254)
        ball.dy *= -1
        
    if ball.ycor() < -254:
        ball.sety(-254)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("{}: {} {}: {}".format(player_a_country, score_a, player_b_country, score_b), align = "center", font = ("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("{}: {} {}: {}".format(player_a_country, score_a, player_b_country, score_b), align = "center", font = ("Courier", 24, "normal"))

    if score_a >= 7 or score_b >= 7:
        pen.clear()
        pen.goto(0, 0)
        pen.write("{} wins!".format(player_a_country if score_a >= 7 else player_b_country), align="center", font=("Courier", 48, "normal"))

    # Player A celebration
    if score_a >= 7:
        paddle_a.shape("turtle")
        paddle_a.color("yellow")
        paddle_a.goto(-300, 0)
        paddle_a.stamp()

    # Player B celebration
    if score_b >= 7:
        paddle_b.shape("turtle")
        paddle_b.color("yellow")
        paddle_b.goto(-300, 0)
        paddle_b.stamp()

    # Paddle and ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
