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
    aim = False
    distance_from_robots = np.array([])

def set_robot_aim(robot,aimed_robot):
    robot.aim = aimed_robot.id

def set_robot_speed(robot, v):
    robot.v = v

def distance_between(robot1,robot2):
    return np.sqrt((robot1.x - robot2.x)**2 + (robot1.y - robot2.y)**2)
  


def set_robot_distance(robots):
    for first_robot in robots:
        for second_robot in robots:
            first_robot.distance_from_robots = np.append(first_robot.distance_from_robots, distance_between(first_robot, second_robot) )




robot1 = Robot(0, 0, 0)
robot2 = Robot(1, 2, 0)
robot3 = Robot(2, 1, 1)
robot4 = Robot(3, 0, 2)
robot5 = Robot(4, 2, 2)


set_of_robots= [robot1, robot2, robot3, robot4, robot5]

set_robot_distance(set_of_robots)

def minimal_distance_id(robot):
    min_id = 0
    min = robot.distance_from_robots[1]
    for i in range(len(robot.distance_from_robots)):
        if ( min > robot.distance_from_robots[i] and robot.distance_from_robots[i] != 0):
            min = robot.distance_from_robots[i]
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
    
# def get_robot_by_id(robots, id):
#     for robot in robots:
#         if (robot.id == id):
#             return robot
#     return False


# def Wake_robots(robots):

#     set_robot_distance(robots)
#     awake_robots = get_awake_robots(robots)
#     sleeping_robots = get_sleepy_robots(robots)
    
#     for robot in awake_robots:
#         aimed_robot = get_robot_by_id(robots, minimal_distance_id(robot))

robot1.isAwake = True
robot4.isAwake = True
        
print(get_awake_robots(set_of_robots))