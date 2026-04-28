import numpy as np
import sys
import json 

if __name__ == "__main__":

    with open("thetas.json", "r") as thetas_file: 
        thetas = json.load(thetas_file)

    theta0 = thetas["theta0"]
    theta1 = thetas["theta1"]
    data = np.loadtxt("data.csv", skiprows=1,delimiter=",")
    x = data[:, 0]
    y = data[:, 1]

    predict = theta0 + theta1 * x

    # determination coefficient (R2)

    ss_res = np.sum((y - predict)**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r2 = 1 - ss_res / ss_tot

    # Mean absolute error

    mae = 1 / len(y) * np.sum(np.abs((y - predict)))

    # Mean absolute percentage error

    mape = 100 / len(y) * np.sum(np.abs((y - predict)/y))

    # Mean squared error 

    mse = np.mean((y - predict)**2)

    # Root mean squared error

    rmse = np.sqrt(mse)

    print(f"R2 Score: {r2}")
    print(f"Mean absolute error: {mae:.2f}")
    print(f"Root mean squared error: {rmse:.2f}")
    print(f"Mean absolute percentage error: {mape:.2f}")