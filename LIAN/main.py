from point import Point
import numpy as np
import matplotlib.pyplot as plt
from lian import LIAN
from function import getLinePoint

def test1():
    matrix = np.zeros((50, 50))
    matrix[3:25, 8:25] = 1
    matrix[3:20, 28:40] = 1
    matrix[25:32, 28:40] = 1


    image = np.copy(matrix)
    start = Point(45, 5, Point(45, 5))
    end = Point(5, 48)
    delta = 10
    angle = 25.0

    return matrix, image, start, end, delta, angle

matrix, image, start, end, delta, angle = test1()

lian = LIAN(matrix, start, end, delta, angle)
if lian.run():
    for i in range(len(lian.path) - 1):
        points = getLinePoint(lian.path[i], lian.path[i+1])
        for point in points:
            image[point.x, point.y] = 0.5

        image[lian.path[i].x, lian.path[i].y] = 0.3

image[start.x, start.y] = 0.8
image[end.x, end.y] = 0.9

plt.imshow(image)
plt.show()
