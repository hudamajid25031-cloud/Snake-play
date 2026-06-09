import turtle
import time
import random

class Snake:
    def __init__(self):
        self.segments = []
        for i in range(3):
            self.add((0 - i*20, 0))
        self.head = self.segments[0]

    def add(self, pos):
        s = turtle.Turtle("circle") # تم تعديل الشكل إلى دائري هنا
        s.color("white")            # لون الثعبان أبيض
        s.penup()
        s.goto(pos)
        self.segments.append(s)

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].goto(self.segments[i-1].pos())
        self.head.forward(20)

    def extend(self):
        self.add(self.segments[-1].pos())

    def reset(self):
        for s in self.segments:
            s.goto(1000, 1000)
        self.__init__()

    def up(self): 
        if self.head.heading() != 270: self.head.setheading(90)
    def down(self): 
        if self.head.heading() != 90: self.head.setheading(270)
    def left(self): 
        if self.head.heading() != 0: self.head.setheading(180)
    def right(self): 
        if self.head.heading() != 180: self.head.setheading(0)


# ---------- Food ----------
class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red") # لون الأكل أحمر
        self.penup()
        self.shapesize(0.6, 0.6)
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))


# ---------- Score ----------
class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.color("black") # لون النقاط (الخط) أسود
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.value}", align="center", font=("Arial", 16, "bold"))

    def inc(self):
        self.value += 1
        self.update()

    def reset(self):
        self.value = 0
        self.update()


# ---------- Game Controller ----------
class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(600, 600)
        self.screen.bgcolor("pink") # لون الشاشة وردي
        self.screen.title("Snake OOP")
        self.screen.tracer(0)

        self.snake = Snake()
        self.food = Food()
        self.score = Score()

        self.bind_keys()

    def bind_keys(self):
        self.screen.listen()
        self.screen.onkey(self.snake.up, "Up")
        self.screen.onkey(self.snake.down, "Down")
        self.screen.onkey(self.snake.left, "Left")
        self.screen.onkey(self.snake.right, "Right")
        self.screen.onkey(self.restart, "r")

    def restart(self):
        self.snake.reset()
        self.score.reset()

    def run(self):
        while True:
            self.screen.update()
            time.sleep(0.1)
            self.snake.move()

            # التحقق من أكل الطعام
            if self.snake.head.distance(self.food) < 15:
                self.food.refresh()
                self.snake.extend()
                self.score.inc()

            # الجدران والاصطدام بها
            if abs(self.snake.head.xcor()) > 280 or abs(self.snake.head.ycor()) > 280:
                self.restart()

            # الاصطدام بالجسم
            for s in self.snake.segments[1:]:
                if self.snake.head.distance(s) < 10:
                    self.restart()
                    break

# تشغيل اللعبة
game = Game()
game.run()
