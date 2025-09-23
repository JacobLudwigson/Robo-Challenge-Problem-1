import numpy as np
import random
import robot, quadrotor, differential_drive, humanoid

class warehouse:
    robots = []
    numRobots = 0
    def __init__(self,gridSize, numRobots) -> None:
        self.numRobots = numRobots
        self.gridSize = gridSize
        self.grid = [[0] * gridSize]*gridSize
        for i in range(0, numRobots):
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
        takeStep = False
        for i in range(0, self.numRobots):
            if (self.robots[i].reached_goal):
                continue
            currDist = self.robots[i].distance_to_goal()
            takeStep = True
            for j in range(i,self.numRobots):
                if (self.robots[i].reached_goal):
                    continue
                if self.robots[i] is quadrotor and (not self.robots[j] is quadrotor):
                    continue
                if (self.robots[j].next_step == self.robots[i].next_step):
                    jDist = self.robots[j].distance_to_goal()
                    if (currDist < jDist):
                        takeStep = False
                        break
            if (takeStep): self.robots[i].take_step()
