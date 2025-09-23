from warehouse import warehouse


gridSize = 5
numRobots = 10

warehouseobj = warehouse(gridSize, numRobots)
from robot import differential_drive, quadrotor, humanoid

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Setup the plot ---
fig, ax = plt.subplots()
ax.set_xlim(-0.5, gridSize - 0.5)
ax.set_ylim(-0.5, gridSize - 0.5)
ax.set_xticks(range(gridSize))
ax.set_yticks(range(gridSize))
ax.grid(True)

# Robots (blue circles) and Goals (red squares)
robot_scat = ax.scatter([], [], c="blue", marker="o", s=100)
goal_scat = ax.scatter(
    [r.goal_pos[0] for r in warehouseobj.robots],
    [r.goal_pos[1] for r in warehouseobj.robots],
    c="red", marker="s", s=100
)
anim: FuncAnimation | None

# --- Update function called every timestep ---
def update(frame):
    warehouseobj.timeStep()  # move robots one step

    if len(warehouseobj.robots) == 0 and not anim == None:
      anim.event_source.stop()
      return

    xs = [r.current_pos[0] for r in warehouseobj.robots]
    ys = [r.current_pos[1] for r in warehouseobj.robots]

    robot_scat.set_offsets(list(zip(xs, ys)))
    ax.set_title(f"Timestep {frame}")
    return robot_scat, goal_scat

# --- Run animation ---
anim = FuncAnimation(fig, update, frames=20, interval=1000, blit=False, repeat=False)
plt.show()
