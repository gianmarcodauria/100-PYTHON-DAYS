
from turtle import Turtle, Screen
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

  def __init__(self):
    self.body = []
    self.create_snake()


  def create_snake(self):
    for square in STARTING_POSITIONS:
      new_snake = Turtle(shape="square")
      new_snake.color("white")
      new_snake.penup()
      new_snake.goto(square)
      self.body.append(new_snake)

  def move_snake(self):
    for square in range(len(self.body) - 1 , 0 , -1):
      new_x = self.body[square - 1].xcor()
      new_y = self.body[square - 1].ycor()
      self.body[square].goto(new_x, new_y)
    self.body[0].forward(MOVE_DISTANCE)


  def up(self):
    if self.body[0].heading() != DOWN:
      self.body[0].setheading(UP)

  def right(self):
    if self.body[0].heading() != LEFT:
      self.body[0].setheading(RIGHT)

  def left(self):
    if self.body[0].heading() != RIGHT:
      self.body[0].setheading(LEFT)

  def down(self):
    if self.body[0].heading() != UP:
      self.body[0].setheading(DOWN)




    
#move a snake automatically