# In order to run this program WITHOUT A FLAW you need to install the matplotlib library and the flask library!! Also you need to create a folder named templates and save the HTML file there. Plus, you need to READ all the comments to help you understand the full function of the code.
# run the code "pip install matplotlib" on your command prompt or in your terminal to install the matplotlib library
# run the code "pip install flask" on your command prompt or in your terminal to install the flask library
# you also need to store the html file in a folder called 'templates'

import numpy as np
from matplotlib.animation import FuncAnimation
import time
import matplotlib.pyplot as plt #importing a library that plots coordinate points
from mpl_toolkits.mplot3d import Axes3D #importing the 3D plotter from the library as our vectors are 3D
import os #importing a routine to make it portable between different paths
from flask import Flask, request, render_template # flask is a program that enables us to run our Python code as an app between two different languages: Python & HTML
motion = Flask(__name__) #assigning a variable to be run as an app
@motion.route('/')#Decorate the view function to register it with the given URL
def index():
    return render_template('motionsource.html') #when this function is called it returns the html file as an output or display
@motion.route('/plot-the-motion', methods=['POST'])#routes to the URL calculate-vectors
def plot_the_motion(displacement_function, time_range):
    dt = 0.01 
    time = np.arange(time_range[0], time_range[1], dt)
    displacement = displacement_function(time)
    velocity = np.gradient(displacement, dt)
    acceleration = np.gradient(velocity, dt)
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 8))
    fig.suptitle('Motion Animation')
    choice_1 = request.form['choice_1']#traces back what the user chose
    if choice_1=="dis":
        ax1.set_xlim(time[0], time[-1])
        ax1.set_ylim(np.min(displacement), np.max(displacement))
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Displacement')
        line1, = ax1.plot([], [], 'b-', lw=2)
    elif choice_1=="vel":
       
       ax2.set_xlim(time[0], time[-1])
       ax2.set_ylim(np.min(velocity), np.max(velocity))
       ax2.set_xlabel('Time')
       ax2.set_ylabel('Velocity')
       line2, = ax2.plot([], [], 'r-', lw=2)
    elif choice_1=="acc":
       ax3.set_xlim(time[0], time[-1])
       ax3.set_ylim(np.min(acceleration), np.max(acceleration))
       ax3.set_xlabel('Time')
       ax3.set_ylabel('Acceleration')
       line3, = ax3.plot([], [], 'g-', lw=2)
    else:
       return "Error"
    displ = request.form['disp1']
    t1 = float(request.form['t1'])
    t2= float(request.form['t2'])
    def update(frame):
        line1.set_data(time[:frame], displacement[:frame])
        line2.set_data(time[:frame], velocity[:frame])
        line3.set_data(time[:frame], acceleration[:frame])
        return line1, line2, line3
    animation = FuncAnimation(fig, update, frames=len(time), interval=50, blit=True)
    plt.show()
    displ = request.form['disp1']
    t1 = request.form['t1']
    t2= request.form['t2']
    t1=float(t1)
    t2=float(t2)
    displacement_function_str = displ
    time_range = (t1, t2)
    displacement_function = lambda time: eval(displacement_function_str, {'np': np, 'sin': np.sin, 'time': time})
    return plot_the_motion(displacement_function, time_range)
if __name__ == '__main__':#if the assigned name above is the app being run, it checks whether there is any static named folder created to store the images created, if there is not, it will create one
    if not os.path.exists('static'):#if there is no path by the name 'static'
        os.makedirs('static')#make a path by the name'static'
motion.run(debug=True, port=5000, host='0.0.0.0')#it runs the app finally by enabling debugging




#What this code claims to do is take the the displacement function and plot the graph if matplotlib is installed
#Group seven
#Members{Israel Tilahun, Michael Hailu, Fraol Girma,Nahom Ayele, Nahom Girma,Tsion Hailu, Yerosen Birhanu, Yeabsira Demmisew, Yonas Alemayehu, Yohannes Getu }
#QED!
