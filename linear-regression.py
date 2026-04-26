from time import sleep

import matplotlib.pyplot as plt
import numpy as np
import csv 
import sys

ITERATION_NUMBER = 10000
LEARNING_RATE = 1.690

if len(sys.argv) > 1:
    iteration_number = int(sys.argv[1])
else:
    iteration_number = ITERATION_NUMBER
if len(sys.argv) > 2:
    learning_rate = float(sys.argv[2])
else:
    learning_rate = LEARNING_RATE

data = np.loadtxt("data.csv", skiprows=1,delimiter=",")
x = data[:, 0]
y = data[:, 1]


theta0 = 0
theta1 = 0
error_sum = 0
weighted_error_sum = 0

fig, ax = plt.subplots()

line, = ax.plot(x, x*0 + 0)
ax.scatter(x, y)

x_margin = (x.max() - x.min()) * 0.05
y_margin = (y.max() - y.min()) * 0.05

ax.set_xlim(x.min() - x_margin, x.max() + x_margin)
ax.set_ylim(y.min() - y_margin, y.max() + y_margin)
ax.set_autoscale_on(False)

x_norm = x / max(x)
y_norm = y / max(y)

plt.ion()
for i in range(0, iteration_number):
    error_sum = 0
    weighted_error_sum = 0
    for j in range (0, len(x)):
        error_sum += (theta0 + theta1 * x_norm[j] - y_norm[j])
        weighted_error_sum += (theta0 + theta1 * x_norm[j] - y_norm[j]) * x_norm[j]

    gradiant0 = error_sum / len(x)
    gradiant1 = weighted_error_sum / len(x)

    delta0 = gradiant0 * learning_rate
    delta1 = gradiant1 * learning_rate 
    theta0 = theta0 - delta0
    theta1 = theta1 - delta1
    line.set_data(x_norm * max(x),( theta0 + theta1 * x_norm) * max(y))
    fig.canvas.draw_idle()
    plt.pause(0.001)

plt.ioff()

