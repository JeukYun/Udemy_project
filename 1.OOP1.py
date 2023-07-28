from turtle import Turtle, Screen
# turtle 모듈에서 Turtle class를 불러 옴

timmy = Turtle()

# Turtle class 에서 ()를 붙여 활성화 후 timmy 객체에 저장
# class의 경우 파스칼 표기법을 따른다
# -> ex) data_frame -> DataFrame (첫 글자를 대문자로)
# 실생활의 예 ex) Car 클래스를 이용해 SUV 객체를 만든것.

print(timmy)
# <turtle.Turtle object at 0x000001EF54821D30>

timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)
# 메서드(수행 할 동작)
# shape("turtle") : timmy 객체가 화살표 -> 거북이로 변환하는 동작 수행
# color("red") : timmy 객체의 색을 변경 -> 색을 변환하는 동작 수행
# forward(100) : timmy 객체를 100걸음 이동 -> 이동하는 동작 수행

my_screen = Screen()
my_screen.canvheight
# 속성
# .canvheight : my_screen 객체에 할당 할 속성
print(my_screen.canvheight)
# 300 출력 -> my_screen의 canvheight 속성(높이)은 300

my_screen.exitonclick()
# exitonclick() : 메서드 -> 객체가 기진 동작
# 실행 시 창이 나타나며 클릭을 할 때 까지 계속 떠있음 -> 동작 수행

