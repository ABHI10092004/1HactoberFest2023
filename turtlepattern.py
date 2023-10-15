#username-ABHI10092004
#date-15-10-2023
#aim-show implimentation od turtle in phyton
import turtle
fred=turtle.Turtle()
fred.speed(0)

length=500
angle=91

for side in range(length):
    fred.forward(side)
    fred.left(angle)

turtle.exitonclick()
