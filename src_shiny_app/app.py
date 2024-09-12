from shiny.express import input, render, ui

import numpy as np
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
        if (angle != "" and velocity != "" and height != ""):
            angle = np.radians(int(angle))
            velocity = int(velocity)
            height = int(height)
        else:
            return plt.plot(0, 0)
        time_of_flight = 2 * velocity * np.sin(angle) / g
        time = np.linspace(0, time_of_flight, 100)
        x = velocity * np.cos(angle) * time
        y = height + velocity * np.sin(angle) * time - 0.5 * g * time**2
        plt.xlabel("Горизонтальное расстояние (м)")
        plt.ylabel("Высота (м)")
        plt.title("Баллистическая кривая")
        plt.grid(True)
        return plt.plot(x, y)
