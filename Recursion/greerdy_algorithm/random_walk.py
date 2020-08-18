import random

position = 0
walk = [position]
steps = 100

for step in range(steps):
    dist = 1 if random.randint(0,1) else -1
    position = position + dist
    walk.append(position)

print(walk)