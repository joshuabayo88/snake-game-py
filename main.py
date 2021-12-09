import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
# screen.bgpic("screenshot.png")
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
segments = []

start_positions = [(0, 0), (-20, 0), (-40, 0)]
for positions in start_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(positions)
    segments.append(new_segment)

game_is_on = True
while(game_is_on):
    screen.update()
    for seg in segments:
        seg.forward(20)
        time.sleep(0.08)

screen.exitonclick()