import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

win = turtle.Screen()
win.title("Snake")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

head = turtle.Turtle()
head.shape("square")
head.color("white")
head.up()
head.goto(0, 0)
head.direction = "Stop"

food = turtle.Turtle()
colors = random.choice(['red', 'orange', 'green'])
food.speed(0)
food.shape("square")
food.color(colors)
food.up()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0  High Score: 0", align="center",
          font=("arial", 24, "bold"))


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")

segments = []

while True:

    win.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:

        time.sleep(1)

        head.goto(0, 0)

        head.direction = "Stop"

        colors = random.choice(['red', 'blue', 'green'])

        for segment in segments:

            segment.goto(1000, 1000)

        segments.clear()

        score = 0

        delay = 0.1

        pen.clear()

        pen.write("Score: {} High Score: {} ".format(
            score, high_score), align="center", font=("arial", 24, "bold"))

    if head.distance(food) < 20:

        x = random.randint(-270, 270)

        y = random.randint(-270, 270)

        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.up()
        segments.append(new_segment)

        delay -= 0.001

        score += 1

        if score > high_score:

            high_score = score

        pen.clear()

        pen.write("Score: {} High Score: {} ".format(
            score, high_score), align="center", font=("arial", 24, "bold"))

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("arial", 24, "bold"))
    time.sleep(delay)


win.mainloop()
