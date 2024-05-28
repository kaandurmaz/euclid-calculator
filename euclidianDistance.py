def euclidianDistance(p):
    x1, y1 = p[0]
    x2, y2 = p[1]
    return getSquareRoot((x2 - x1) ** 2 + (y2 - y1) ** 2)


def getSquareRoot(x):
    return x ** 0.5


points = [[(2, 2), (5, 6)], [(2, 2), (7, 14)]]
distances = [euclidianDistance(i) for i in points]

print(distances)
