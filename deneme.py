import math

ask = "y"
points = []
while ask == 'y':
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    points.append((x,y))
    ask = input("Enter 'y' to continue adding points: ")

def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)


min_distance = min(distances)

print(f"Minimum distance: {min_distance : .2f}")