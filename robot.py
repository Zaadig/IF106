import numpy as np

NUM_OF_ROBOTS = 10

class robot:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
    v = 1 #robot speed
    state = 0 #robot state 0 if asleep 1 if awake
    aim = False

def set_robot_aim(robot,aimed_robot):
    robot.aim = aimed_robot.id

def set_robot_speed(robot, v):
    robot.v = v
