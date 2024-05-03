# A bouncing circle
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches


def set_axis():
    ax.set_title("A bouncing circle")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_aspect("equal")
    ax.grid()


def update(f):
    ax.cla()    # Clear ax
    set_axis()
    ax.text(x_min, y_max * 0.9, "Step=" + str(f))

    global p0, v0, r0, dr
    circle = patches.Circle(xy=p0, radius=r0, fill=False)
    ax.add_patch(circle)
    p0 = p0 + v0   # Change position
    # Reverse vector if out out of range
    if p0[0] > x_max or p0[0] < x_min:
        v0 = np.dot(reverse_h, v0)
    if p0[1] > y_max or p0[1] < y_min:
        v0 = np.dot(reverse_v, v0)
    r0 = r0 + dr     # Change radius
    if r0 > r_max or r0 < r_min:
        dr = -dr


# Global variables
x_min = -10.
x_max = 10.
y_min = -10.
y_max = 10.
w = x_max - x_min
h = y_max - y_min
r_max = 10.
r_min = 1.

reverse_h = np.array([[-1, 0],[0, 1]])  # Matrix of horizontal reverse
reverse_v = np.array([[1, 0],[0, -1]])  # Matrix of vertical reverse

r0 = np.random.rand() * w / 2 * 0.9 + 1.
dr = 0.1
p0 = np.array([np.random.rand() * w - w / 2, np.random.rand() * h - h / 2])     # Initial points of circles
theta0 = np.random.rand() * 2. * math.pi    # Angle of motion
s0 = 0.5    # Scalar of velocity
v0 = s0 * np.array([math.cos(theta0), math.sin(theta0)])    # Vector of circles

# Generate figure and axes
fig = plt.figure()
ax = fig.add_subplot(111)

# Draw animation
set_axis()
anim = animation.FuncAnimation(fig, update, interval=50, save_count=100)
plt.show()
