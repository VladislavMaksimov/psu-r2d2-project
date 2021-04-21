from field import Field
from robot import Robot

field = Field(10, 5)
field.print()
robot = Robot(field.field)
robot.go_right()