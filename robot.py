from matplotlib.pyplot import get
import numpy as np

NUM_OF_ROBOTS = 10

class Robot:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
    v = 1 #robot speed
    isAwake = False #robot state 0 if asleep 1 if awake
    aim = -1
    isAimed = False
    distance_from_robots = []

def set_robot_aim(robot,aimed_robot):
    robot.aim = aimed_robot.id

def set_robot_speed(robot, v):
    robot.v = v

def distance_between(robot1, robot2):
    return np.sqrt((robot1.x - robot2.x)**2 + (robot1.y - robot2.y)**2)

#saaat i in range
def set_robot_distance(robots):
    for first_robot in robots:
        for second_robot in robots:
            first_robot.distance_from_robots.append([distance_between(first_robot, second_robot), second_robot.isAimed])




robot1 = Robot(0, -1, -1)
robot2 = Robot(1, 2, 0)
robot3 = Robot(2, 1, 1)
robot4 = Robot(3, 0, 2)
robot5 = Robot(4, 2, 2)


set_of_robots= [robot1, robot2, robot3, robot4, robot5]
set_robot_distance(set_of_robots)
print(robot1.distance_from_robots)

def minimal_distance_id(robot):
    min_id = 0
    min = robot.distance_from_robots[1][0]
    for i in range(len(robot.distance_from_robots)):
        d = robot.distance_from_robots[i]
        if  (min > d[0] and d[0] != 0 and not (d[1])):
                min = d[0]
                min_id = i
    return min_id

def get_awake_robots(robots):
    if (len(robots) == 0):
        return np.array([])
    elif (robots[0].isAwake):
        return np.append(np.array([robots[0]]),get_awake_robots(robots[1:]))
    else:
        return get_awake_robots(robots[1:])


def get_sleepy_robots(robots):
    if (len(robots) == 0):
        return np.array([])
    elif not (robots[0].isAwake):
        return np.append(np.array([robots[0]]),get_sleepy_robots(robots[1:]))
    else:
        return get_sleepy_robots(robots[1:])
    
def get_robot_by_id(robots, id):
    for robot in robots:
        if (robot.id == id):
            return robot
    return False

def all_sleepy_robots_aimed(sleepy_robots):
    for robot in sleepy_robots:
        if (not (robot.isAimed)):
            return False
    return True

def set_aimed_robots(robots):
    sleepy_robots = get_sleepy_robots(robots)
    awake_robots = get_awake_robots(robots)
    N = 10
    k = 0
    while(len(awake_robots) < len(robots) and not (all_sleepy_robots_aimed(sleepy_robots)) and k < N):
        set_robot_distance(robots)
        awake_robots = get_awake_robots(robots)
        sleepy_robots = get_sleepy_robots(robots)
        for i in range(len(awake_robots)):
            first_robot = awake_robots[i]
            min_id = minimal_distance_id(first_robot)
            aimed_robot = get_robot_by_id(sleepy_robots, min_id)
            first_robot.aim = min_id
            print(min_id)
            aimed_robot.isAimed = True
            d1 = distance_between(first_robot, aimed_robot)
            
            for j in range (i + 1, len(awake_robots)):
                second_robot = awake_robots[j]
                d2 = distance_between(second_robot,aimed_robot)
                if( d2 < d1 ):
                    first_robot.aim = -1
                    second_robot.aim = min_id
        k += 1

                    

set_of_robots= [robot1, robot2, robot3, robot4, robot5]
robot1.isAwake = True
robot1.isAimed = True
robot2.isAwake = True
robot2.isAimed = True

set_aimed_robots(set_of_robots)
print(robot1.aim, robot2.aim)