"""print("Hello World")
x=5
y="Johnny"
print(x)
print(y)
z=str(2)
k=float(2)
m=int(2)
print(z)
print(k)
print(m)
print(type(x))
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x,y,z)
import math
print(math.pi)"""
import random
def monte_carlo_pi(num_points):
    inside_circle = 0
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    pi_approx = 4 * (inside_circle / num_points)
    return pi_approx

num_points = 10000000000
pi_approx = monte_carlo_pi(num_points)
print(f"Approximation of pi using Monte Carlo method with {num_points} points: {pi_approx}") 

