import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")

# # 정사각형 그리기
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)
# # 귀여움 주의
#
# # 점선 그리기
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# # 다각형 도형 여러개 3~10각형 까지 그리기

# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(360 / num_sides)
#
#
# for i in range(3,11):
#     draw_shape(i)

# # 무작위 이동
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
#            "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
#
# tim.pensize(10)
# tim.speed('fastest')
#
# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# # 랜덤색상 생성하기 (튜플)
turtle.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color


# tim.pensize(10)
# directions = [0, 90, 180, 270]
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

tim.speed("fastest")

def draw_spirograph(size):
    for _ in range(int(360 / size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size)

draw_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()


# import heroes # 표준 라이브러리가 아니라 오류로 표기. -> 설치하기
# print(heroes.gen())

