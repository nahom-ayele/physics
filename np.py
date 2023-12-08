import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

def plot_motion(displacement_function, time_range):
    dt = 0.01 
    time = np.arange(time_range[0], time_range[1], dt)
    displacement = displacement_function(time)
    velocity = np.gradient(displacement, dt)
    acceleration = np.gradient(velocity, dt)
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 8))
    fig.suptitle('Motion Animation')
    ax1.set_xlim(time[0], time[-1])
    ax1.set_ylim(np.min(displacement), np.max(displacement))
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Displacement')
    line1, = ax1.plot([], [], 'b-', lw=2)
    ax2.set_xlim(time[0], time[-1])
    ax2.set_ylim(np.min(velocity), np.max(velocity))
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Velocity')
    line2, = ax2.plot([], [], 'r-', lw=2)
    ax3.set_xlim(time[0], time[-1])
    ax3.set_ylim(np.min(acceleration), np.max(acceleration))
    ax3.set_xlabel('Time')
    ax3.set_ylabel('Acceleration')
    line3, = ax3.plot([], [], 'g-', lw=2)
    
    
    def update(frame):
        line1.set_data(time[:frame], displacement[:frame])
        line2.set_data(time[:frame], velocity[:frame])
        line3.set_data(time[:frame], acceleration[:frame])
        return line1, line2, line3
    animation = FuncAnimation(fig, update, frames=len(time), interval=50, blit=True)
    plt.show()
displacement_function_str = input("Enter the displacement function as a mathematical expression (e.g. sin(time), time**2 +3... follofing the python rules): ")
displacement_function = lambda time: eval(displacement_function_str, {'np': np, 'sin': np.sin, 'time': time})


start_time = float(input("Enter the start time: "))
end_time = float(input("Enter the end time: "))
time_range = (start_time, end_time)

plot_motion(displacement_function, time_range)