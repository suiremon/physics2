from shiny.express import input, render, ui

import numpy as np

def find_t(h,v,a):
    d = v**2*np.sin(a)**2+4*9.81/2*h
    t1=(-v*np.sin(a)+np.sqrt(d))/(-9.81)
    t2=(-v*np.sin(a)-np.sqrt(d))/(-9.81)
    return [t1,t2]

    
ui.input_text("angle", label="Введите угол:")
ui.input_text("velocity", label="Введите скорость:")
ui.input_text("height", label="Введите высоту:")

with ui.card(full_screen=True):
    g = 9.81
    @render.plot
    def plot():
        import matplotlib.pyplot as plt
        angle = input.angle()
        velocity = input.velocity()
        height = input.height()
        if (angle != "" and velocity != "" and height != "" and int(height) >=0):
            velocity = float(velocity)
            height = float(height)
            angle = np.radians(float(angle))
            time_of_flight = find_t(height, velocity, angle)[1]
        else:
            return plt.plot(0, 0)
        #time_of_flight = 2 * velocity * np.sin(angle) / g
        time = np.linspace(0, time_of_flight, 100)
        x = velocity * np.cos(angle) * time
        y = height + velocity * np.sin(angle) * time - 0.5 * g * time**2

        plt.xlabel("Горизонтальное расстояние (м)")
        plt.ylabel("Высота (м)")
        plt.title("Баллистическая кривая")
        plt.grid(True)
        return plt.plot(x, y)
