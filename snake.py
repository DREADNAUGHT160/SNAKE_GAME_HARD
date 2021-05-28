from turtle import Turtle

MOVE_PACE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.sequence = []

        self.build_snake()
        self.head = self.sequence[0]

    def build_snake(self):

        for i in range(3):
            self.add_segment(i)

    def add_segment(self, i):
        x = 0
        i = Turtle("square")
        i.penup()
        i.goto(x, 0)
        i.color("blue")
        x += 20
        self.sequence.append(i)

    def snake_move(self):

        for pos in range(len(self.sequence) - 1, 0, -1):
            x_corn = self.sequence[pos - 1].xcor()
            y_corn = self.sequence[pos - 1].ycor()
            self.sequence[pos].goto(x_corn, y_corn)
        self.head.forward(MOVE_PACE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self, ):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self, ):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self, ):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_segment(self.sequence[-1].position())
