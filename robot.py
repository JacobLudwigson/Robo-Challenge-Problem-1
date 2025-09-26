class robot:
    def __init__(self, start_pos: tuple[int, int], goal_pos: tuple[int, int]) -> None:
        self.current_pos: tuple[int, int] = start_pos
        self.goal_pos: tuple[int, int] = goal_pos
        self.next_step: tuple[int, int] = self.__calculate_next_step()
        self.previous_pos: tuple[int, int] = start_pos

    def revert(self) -> None:
        self.current_pos = self.previous_pos

    def take_step(self) -> None:
        self.previous_pos = self.current_pos
        self.current_pos = self.next_step
        self.next_step = self.__calculate_next_step()
    
    def reached_goal(self) -> bool:
        return self.current_pos[0] == self.goal_pos[0] and self.current_pos[1] == self.goal_pos[1]

    def distance_to_goal(self) -> int:
        return abs(self.current_pos[0] - self.goal_pos[0]) + abs(self.current_pos[1] - self.goal_pos[1])
    
    def __calculate_next_step(self) -> tuple[int, int]:
        if self.goal_pos[0] > self.current_pos[0]:
            return (self.current_pos[0] + 1, self.current_pos[1])
        elif self.goal_pos[0] < self.current_pos[0]:
            return (self.current_pos[0] - 1, self.current_pos[1])
        elif self.goal_pos[1] > self.current_pos[1]:
            return (self.current_pos[0], self.current_pos[1] + 1)
        elif self.goal_pos[1] < self.current_pos[1]:
            return (self.current_pos[0], self.current_pos[1] - 1)
        return self.current_pos

class quadrotor(robot):
    def __init__(self, start_pos: tuple[int, int], goal_pos: tuple[int, int]) -> None:
        super().__init__(start_pos, goal_pos)

class differential_drive(robot):
    def __init__(self, start_pos: tuple[int, int], goal_pos: tuple[int, int]) -> None:
        super().__init__(start_pos, goal_pos)


class humanoid(robot):
    def __init__(self, start_pos: tuple[int, int], goal_pos: tuple[int, int]) -> None:
        super().__init__(start_pos, goal_pos)

