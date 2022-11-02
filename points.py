from random import randrange
from math import sqrt
# Generate 100 random points.

points = []
for i in range(100):
    p = (randrange(1000), randrange(1000))
    points.append(p)

# Determine which two points are farthest.
greatest = -1
p1 = None
p2 = None
for (px, py) in points:         # pattern matching
    for (qx, qy) in points:
        dist = sqrt((px - qx) ** 2 + (py - qy ** 2))
        if dist > greatest:
            greatest = dist
            p1 = (px, py)
            p2 = (qx, qy)

print(greatest)
print(f'p1 = {p1}, p2 = {p2}')