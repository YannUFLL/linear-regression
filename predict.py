
import sys 

THETA0 = 8472.47449422059
THETA1 = -0.02119103328839867

if __name__ == "__main__":
    try: 
        if len(sys.argv) > 1:
            line = sys.argv[1]
        else: 
            line = input("Please enter a mileage: ")
        km = float(line)
        if km < 0:
            raise ValueError
        estimated_price = max(0, THETA0 + THETA1 * km)
        print("Estimated price: ", estimated_price)
    except (IndexError, ValueError):
        print("Please provide a valid mileage", file=sys.stderr)
        sys.exit(1)
    except (EOFError, KeyboardInterrupt):
        print("\n Prediction cancelled.")
        sys.exit(0)













