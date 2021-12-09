from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
# screen.bgpic("screenshot.png")
screen.bgcolor("black")
screen.title("Snake Game")

start_positions = [(0, 0), (-20, 0), (-40, 0)]
for positions in start_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    print(positions)
    new_segment.goto(positions)

screen.exitonclick()