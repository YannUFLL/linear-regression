import numpy as np
import sys


THETA0 = 8472.47449422059
THETA1 = -0.02119103328839867

data = np.loadtxt("data.csv", skiprows=1,delimiter=",")
x = data[:, 0]
y = data[:, 1]

predict = THETA0 + THETA1 * x


# determination coefficient (R2)

ss_res = np.sum((y - predict)**2)
ss_tot = np.sum((y - np.mean(y))**2)
r2 = 1 - ss_res / ss_tot

# Mean absolute error

mae = 1 / len(y) * np.sum(np.abs((y - predict)))

# Mean absolute percentage error

mape = 100 / len(y) * np.sum(np.abs((y - predict)/y))

print(f"R2 Score: {r2}")
print(f"Mean absolute error: {mae:.2f}")
print(f"Mean absolute percentage error: {mape:.2f}")