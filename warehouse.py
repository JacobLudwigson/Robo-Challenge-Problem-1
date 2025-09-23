import numpy as np
import random
import robot

class warehouse:
    robots = []
    numRobots = 0
    def __init__(self,gridSize, numRobots) -> None:
        self.numRobots = numRobots
        self.gridSize = gridSize
        self.grid = [[0] * gridSize]*gridSize
        for i in range(0, numRobots):
            #Get a random position and regenerate if not
            startX,startY = random.randint(1, gridSize), random.randint(1, gridSize)
            while (gridSize[startX][startY]):
                startX,startY = random.randint(1, gridSize), random.randint(1, gridSize)
            
            goalX,goalY = random.randint(1, gridSize), random.randint(1, gridSize)
            robotType = random.randint(1,3)
            if robotType == 1:
                self.robots.append(quadrotor((startX,startY), (goalX,goalY)))
            elif robotType == 2:
                self.robots.append(differential_drive((startX,startY), (goalX,goalY)))
            else:
                self.robots.append(humanoid((startX,startY), (goalX,goalY)))

    def timeStep(self):
        nextSteps = []
        for i in self.robots:
            nextSteps.append(i.next_step)
        for i in self.robots:
        
            

        

