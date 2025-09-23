class robot:
    def __init__(self, start_pos: tuple[int, int], goal_pos: tuple[int, int]) -> None:
        self.current_pos: tuple[int, int] = start_pos
        self.goal_pos: tuple[int, int] = goal_pos
        self.next_step = self.calculate_next_step()
    
    def get_next_step() -> tuple[int, int]:
        pass

    def take_step() -> None:
        pass
    
    def calculate_next_step() -> tuple[int, int]:
        pass

class quadrotor(robot):
    def __init__(self, start_pos: tuple[int, int], goal_pos: tuple[int, int]) -> None:
        pass

class differential_drive(robot):
    def __init__(self, start_pos: tuple[int, int], goal_pos: tuple[int, int]) -> None:
        pass

class humanoid(robot):
    def __init__(self, start_pos: tuple[int, int], goal_pos: tuple[int, int]) -> None:
        pass
