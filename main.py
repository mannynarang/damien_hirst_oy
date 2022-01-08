import turtle as t

import random
import colorgram

t.colormode(255)
timmy_the_turtle = t.Turtle()
list_of_colors = [(249, 248, 248), (237, 241, 245), (238, 246, 244), (249, 243, 247), (1, 12, 31), (53, 25, 17),
                  (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39)]


def draw_circle():

    timmy_the_turtle.speed("fastest")
    for x in range(-300, 300, 60):
        for y in range(-300, 300, 60):
            print(timmy_the_turtle.position())
            timmy_the_turtle.penup()
            timmy_the_turtle.setposition(x, y)
            timmy_the_turtle.fillcolor(random.choice(list_of_colors))

            timmy_the_turtle.pendown()
            timmy_the_turtle.dot(20,random.choice(list_of_colors))



draw_circle()
t.exitonclick()
