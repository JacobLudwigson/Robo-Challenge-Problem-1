from warehouse import warehouse
from robot import differential_drive, quadrotor, humanoid
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Setup ---
gridSize = 5
numRobots = 10
warehouseobj = warehouse(gridSize, numRobots)

# --- Color mapping for robot types ---
type_colors = {
    "quadrotor": "red",
    "differential_drive": "green",
    "humanoid": "blue"
}

# --- Setup the plot ---
fig, ax = plt.subplots(figsize=(12, 8))  # Larger plot for better clarity
ax.set_xlim(-0.5, gridSize - 0.5)
ax.set_ylim(-0.5, gridSize - 0.5)
ax.set_xticks(range(gridSize))
ax.set_yticks(range(gridSize))
ax.grid(True)
ax.set_title("Robot Grid Navigation", fontsize=14)

# --- Static goal positions ---
goal_scat = ax.scatter(
    [r.goal_pos[0] for r in warehouseobj.robots],
    [r.goal_pos[1] for r in warehouseobj.robots],
    c=[type_colors[r.__class__.__name__] for r in warehouseobj.robots],
    marker="s", s=100, label="Goals"
)

# --- Update function ---
def update(frame):
    ax.clear()
    ax.set_xlim(-0.5, gridSize - 0.5)
    ax.set_ylim(-0.5, gridSize - 0.5)
    ax.set_xticks(range(gridSize))
    ax.set_yticks(range(gridSize))
    ax.grid(True)
    ax.set_title(f"Robot Grid Navigation — Timestep {frame}", fontsize=14)

    # Step robots
    warehouseobj.timeStep()

    if len(warehouseobj.robots) == 0:
        anim.event_source.stop()
        return

    # Draw robots, goals, and lines
    for r in warehouseobj.robots:
        robot_type = r.__class__.__name__
        color = type_colors[robot_type]

        # Robot current position (circle)
        ax.scatter(r.current_pos[0], r.current_pos[1], c=color, marker="o", s=100)

        # Robot goal position (square)
        ax.scatter(r.goal_pos[0], r.goal_pos[1], c=color, marker="s", s=100)

        # Line from robot to goal
        ax.plot(
            [r.current_pos[0], r.goal_pos[0]],
            [r.current_pos[1], r.goal_pos[1]],
            linestyle="dotted", color=color, alpha=0.5
        )

    # Add legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='red', label='Quadrotor'),
        Patch(facecolor='green', label='DifferentialDrive'),
        Patch(facecolor='blue', label='Humanoid')
    ]
    ax.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1, 0.5))

# --- Run animation ---
anim = FuncAnimation(fig, update, frames=30, interval=3000, blit=False, repeat=False)
plt.show()
