# Import Python libraries
from random import randint


# Class for pool of possible objects to be inserted in the maze
class Pool:
    def __init__(self):
        self.obstacles = []
        self.obstacles.append([[0, 0, 0, 0],
                               [0, 1, 1, 0],
                               [0, 1, 1, 0],
                               [0, 0, 0, 0]])

        self.obstacles.append([[0, 0, 0, 0, 0],
                              [0, 1, 1, 1, 0],
                              [0, 0, 0, 0, 0]])

        self.obstacles.append([[0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 1, 1, 1, 1, 0],
                               [0, 0, 0, 0, 0, 0, 0]])

        self.obstacles.append([[0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 1, 0, 0, 0],
                               [0, 0, 0, 1, 0, 0, 0],
                               [0, 0, 0, 1, 0, 0, 0],
                               [0, 1, 1, 1, 1, 1, 0],
                               [0, 0, 0, 0, 0, 0, 0]])

        self.obstacles.append([[0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0],
                               [0, 0, 1, 0, 0],
                               [0, 0, 0, 1, 0],
                               [0, 0, 0, 0, 0]])

        self.obstacles.append([[0, 0, 0, 0, 0],
                               [0, 0, 0, 1, 0],
                               [0, 0, 1, 0, 0],
                               [0, 1, 0, 0, 0],
                               [0, 0, 0, 0, 0]])

        self.obstacles.append([[0, 0, 0, 0, 0],
                               [0, 1, 0, 1, 0],
                               [0, 1, 0, 1, 0],
                               [0, 1, 0, 1, 0],
                               [0, 1, 0, 1, 0],
                               [0, 0, 0, 0, 0]])

    def get_obstacle(self):
        return self.obstacles[randint(0, len(self.obstacles) - 1)]