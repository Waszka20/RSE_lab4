import random

def estimate_pi(num_samples=1000000):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.random()  # random number in [0,1)
        y = random.random()
        
        # Check if the point is inside the unit quarter circle
        if x**2 + y**2 <= 1:
            inside_circle += 1

    # Ratio of points inside circle to total points
    return 4 * inside_circle / num_samples

