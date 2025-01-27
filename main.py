import time
import pygame
from turtle import Screen, Turtle

pygame.mixer.init()

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

def set_background(image_path):
    try:
        screen.bgpic(image_path)
        print("Background image loaded successfully.")
    except Exception as e:
        print(f"Error loading background image: {e}")

bounce_sound = pygame.mixer.Sound("bounce.mp3")
point_scored_sound = pygame.mixer.Sound("point_scored.mp3")

def draw_dividing_line():
    divider = Turtle()
    divider.color("white")
    divider.penup()
    divider.goto(0, 300)
    divider.setheading(270)
    divider.pendown()
    
    for _ in range(30):
        divider.pendown()
        divider.forward(20)
        divider.penup()
        divider.forward(10)

    divider.hideturtle()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

set_background("bg_resized.png")
draw_dividing_line()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280: 
        bounce_sound.play()
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        bounce_sound.play()

    if ball.xcor() > 380:
        point_scored_sound.play()
        ball.reset_position()
        scoreboard.left_point()

    if ball.xcor() < -380:
        point_scored_sound.play()
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
