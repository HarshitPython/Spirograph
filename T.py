







from turtle import Turtle,Screen, color
import random
import turtle

tim = Turtle()





'''Draw a dashed line'''

# for i in range(15):

#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

'''Draw different shapes'''

# colours = ["red", "blue", "green", "yellow", "pink", "brown", "orange", "coral"]

# def draw_shape(number_of_sides):
#     angle = 360/number_of_sides
#     for _ in range(number_of_sides):
#         tim.forward(80)
#         tim.right(angle)

# for shape_side_n in range(3,11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

'''Draw a random walk'''

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
