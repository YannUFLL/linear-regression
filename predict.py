
import sys 

THETA0 = 8472.47449422059
THETA1 = -0.02119103328839867

if __name__ == "__main__":
    try: 
        km = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Please provide a valid km value", file=sys.stderr)
        sys.exit(1)
    estimated_price = THETA0 + THETA1 * km
    print("Estimated price: ", estimated_price)











