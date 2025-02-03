import sys

angles = []
angle_types = 0
for angle in sys.stdin.readlines():
    angle = int(angle)
    if angle not in angles:
        angle_types += 1
    angles.append(angle)

if sum(angles) != 180:
    print("Error")
elif angle_types == 1:
    print("Equilateral")
elif angle_types == 2:
    print("Isosceles")
else:
    print("Scalene")
