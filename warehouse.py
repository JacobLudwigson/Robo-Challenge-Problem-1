import numpy as np
import random
from robot import robot, differential_drive, quadrotor, humanoid


class warehouse:
    robots = []
    numRobots = 0
    def __init__(self,gridSize, numRobots) -> None:
        self.numRobots = numRobots
        self.gridSize = gridSize
        self.grid = [[[] for _ in range(gridSize)] for _ in range(gridSize)]
        all_positions = [(x, y) for x in range(gridSize) for y in range(gridSize)]
        random.shuffle(all_positions)
        start_positions = all_positions[:numRobots]

        for startX, startY in start_positions:
            goalX, goalY = random.randint(0, gridSize - 1), random.randint(0, gridSize - 1)
            robotType = random.randint(1, 3)

            if robotType == 1:
                self.robots.append(quadrotor((startX, startY), (goalX, goalY)))
            elif robotType == 2:
                self.robots.append(differential_drive((startX, startY), (goalX, goalY)))
            else:
                self.robots.append(humanoid((startX, startY), (goalX, goalY)))

    def willCollide(self, robot1, robot2):
        type1, type2 = type(robot1).__name__, type(robot2).__name__

        if type1 == "quadrotor" and type2 == "quadrotor":
            return True
        
        if (type1 == "differential_drive" and type2 == "humanoid") or \
        (type1 == "humanoid" and type2 == "differential_drive") or \
        (type1 == "humanoid" and type2 == "humanoid") or \
        (type1 == "differential_drive" and type2 == "differential_drive"):
            return True

        return False

    def monitor(self):
        violations = []

        # Compare every pair of robots
        for i in range(self.numRobots):
            for j in range(i + 1, self.numRobots):
                r1, r2 = self.robots[i], self.robots[j]

                # They share a position (potential collision)
                if r1.current_pos == r2.current_pos:
                    if self.willCollide(r1, r2):
                        violations.append((r1, r2))

        # Report results
        if violations:
            print("Collision rule violations detected:")
            for r1, r2 in violations:
                print(f"[X] COLLISION {type(r1).__name__} at {r1.current_pos} collided with {type(r2).__name__} at {r2.current_pos}")
        else:
            print("[] No collision rule violations detected.")

    # def timeStep(self):
    #     # Phase 1: Propose moves
    #     proposals = []
    #     for i in range(self.numRobots):
    #         currDist = self.robots[i].distance_to_goal()
    #         takeStep = True

    #         # Check "Has any other robot I will collide with beat me to this square?"
    #         for k in range(i):
    #             if self.robots[k].current_pos == self.robots[i].next_step:
    #                 if self.willCollide(self.robots[k], self.robots[i]):
    #                     takeStep = False
    #                     break

    #         # Check "Do future robots want this square?"
    #         for j in range(i + 1, self.numRobots):
    #             if not self.willCollide(self.robots[j], self.robots[i]):
    #                 continue
    #             if self.robots[j].next_step == self.robots[i].next_step:
    #                 jDist = self.robots[j].distance_to_goal()
    #                 if currDist < jDist:
    #                     takeStep = False
    #                     break
    #                 elif currDist == jDist:
    #                     takeStep = bool(random.randint(0, 1))
    #                     break

    #         # Save proposal (either move or wait)
    #         if takeStep:
    #             proposals.append(self.robots[i].next_step)
    #         else:
    #             proposals.append(self.robots[i].current_pos)

    #     # Phase 2: Resolve conflicts
    #     conflicts = {}
    #     for i, pos in enumerate(proposals):
    #         conflicts.setdefault(pos, []).append(i)

    #     for pos, ids in conflicts.items():
    #         if len(ids) == 1:
    #             # Only one robot wants this square
    #             self.robots[ids[0]].take_step()
    #         else:
    #             # Conflict: pick a winner
    #             # Use shortest distance-to-goal as priority, tie-break randomly
    #             bestDist = min(self.robots[r].distance_to_goal() for r in ids)
    #             candidates = [r for r in ids if self.robots[r].distance_to_goal() == bestDist]
    #             winner = random.choice(candidates)
    #             self.robots[winner].take_step()
    #             # Others stay put (do nothing)

    #     # Phase 3: Clean up
    #     self.monitor()
    #     self.robots = [r for r in self.robots if not r.reached_goal()]
    #     self.numRobots = len(self.robots)
    def timeStep(self):
        proposals = []
        for i in range(0, self.numRobots):
            currDist = self.robots[i].distance_to_goal()
            takeStep = True

            #Check "Has any other robot I will colide with beat me to this square on this timestep"
            for k in range(0, i-1):
                if (self.robots[k].current_pos == self.robots[i].next_step):
                    if self.willCollide(self.robots[k], self.robots[i]):
                        takeStep = False
                        break
            
            #Check "Can I take this square on this timestep or are there future robots that have a large distance that want to go here" 
            for j in range(i+1,self.numRobots):
                if (not self.willCollide(self.robots[j], self.robots[i])):
                    continue
                if (self.robots[j].next_step == self.robots[i].next_step):
                    jDist = self.robots[j].distance_to_goal()
                    if (currDist < jDist):
                        takeStep = False
                        break
                    elif (currDist == jDist):
                        takeStep = bool(random.randint(0,1))
                        break
            if takeStep:
                proposals.append(self.robots[i].next_step)
            else:
                proposals.append(self.robots[i].current_pos)

        #Is there anyone that plans to wait on the square I want to go to, if so, Ill wait too.
        for i in range (0, self.numRobots):
            if proposals[i] == self.robots[i].next_step:
                if proposals.count(proposals[i]) > 1:
                    print("Overlapping proposals!")
                    continue
                self.robots[i].take_step()
        self.monitor()
        
        self.robots = [robot for robot in self.robots if not robot.reached_goal()]
        self.numRobots = len(self.robots)

# r = robot((5,5), (5,5))