import sys 
import json

if __name__ == "__main__":
    
    try: 
        with open("thetas.json", "r") as thetas_file: 
            thetas = json.load(thetas_file)
        theta0 = thetas["theta0"]
        theta1 = thetas["theta1"]
        if len(sys.argv) > 1:
            line = sys.argv[1]
        else: 
            line = input("Please enter a mileage: ")
        km = float(line)
        if km < 0:
            raise ValueError
        estimated_price = max(0, theta0 + theta1 * km)
        print("Estimated price: ", estimated_price)
    except (IndexError, ValueError):
        print("Please provide a valid mileage", file=sys.stderr)
        sys.exit(1)
    except (EOFError, KeyboardInterrupt):
        print("\n Prediction cancelled.")
        sys.exit(0)













