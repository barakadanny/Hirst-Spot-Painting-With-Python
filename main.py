from turtle import Turtle, Screen
import random

t = Turtle()
t.penup()
t.setpos(-200, 200)

color_list = [(253, 252, 248), (248, 254, 251), (252, 244, 249), (242, 249, 252), (237, 230, 96), (13, 115, 170), (166, 79, 46), (188, 12, 63), (213, 157, 87), (129, 181, 203), (234, 76, 46), (33, 139, 83), (5, 34, 91), (146, 167, 35), (76, 40, 21), (110, 187, 165), (167, 47, 91), (227, 117, 147), (14, 170, 212), (59, 160, 89), (6, 95, 51), (219, 71, 119), (95, 21, 69), (240, 162, 190), (147, 205, 224), (12, 87, 106), (211, 222, 10), (248, 170, 145), (9, 45, 127), (7, 75, 41)]


def hirst_spot():
    for x in range(1, 10):
        for y in range(1, 10):
            random_color = random.choice(color_list)

            red = random_color[0] / 255
            green = random_color[1] / 255
            blue = random_color[2] / 255

            rgb = (red, green, blue)

            t.dot(20, rgb)
            t.penup()
            t.forward(50)
            t.pendown()

        t.penup()
        t.backward(450)
        t.right(90)
        t.forward(50)
        t.left(90)


hirst_spot()


screen = Screen()
screen.exitonclick()
