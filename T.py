from turtle import Turtle,Screen, color
import random
import turtle

tim = Turtle()











def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    color = (r, g, b)
    return color


tim.speed("fastest")
turtle.colormode(255)



def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)
        

draw_spirograph(5)



screen = Screen()
screen.exitonclick()
