from turtle import Turtle,Screen
import random


color = ["red","blue","green","orange","firebrick","yellow","pink"]

tim = Turtle()
tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random.choice(color))
        tim.circle(100)
        tim.setheading(tim.heading()  + size_of_gap)



draw_spirograph(5)



screen = Screen()
screen.exitonclick()