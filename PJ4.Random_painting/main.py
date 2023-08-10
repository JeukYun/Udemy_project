import colorgram

# image 에서 랜덤 색상 추출
rgb_colors = []
colors = colorgram.extract('image.jpeg', 20)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

color_list = [(225, 159, 65), (156, 64, 34), (246, 157, 50),
              (235, 62, 109), (169, 186, 2), (174, 21, 65),
              (63, 40, 56), (252, 211, 12), (251, 86, 41),
              (240, 125, 168), (82, 168, 213), (2, 97, 81),
              (3, 168, 203), (34, 60, 136), (252, 210, 0),
              (193, 35, 54), (65, 41, 39), (51, 79, 168)]

import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for i in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle.Screen()
screen.exitonclick()
