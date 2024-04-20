import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def draw_pressure_bar():
    file_data = pd.read_csv("data.csv")
    mass = file_data.iloc[:,0]
    max_pressure = file_data.iloc[:,1]
    print(mass)
    print(max_pressure)
    plt.bar(mass, max_pressure)
    plt.xlabel('Mass')
    plt.ylabel('Max Pressure')
    plt.title('Mass vs Max Pressure')
    plt.xticks(mass)
    plt.show()

if __name__ == '__main__':
    draw_pressure_bar()