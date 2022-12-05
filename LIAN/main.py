from point import Point
import numpy as np
import matplotlib.pyplot as plt
from lian import LIAN
from function import getLinePoint
import cv2


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


def test2():
    matrix = np.zeros((50, 50))
    matrix[10:30, 15:35] = 1

    image = np.copy(matrix)
    start = Point(15, 0, Point(15, 0))
    end = Point(25, 49)
    delta = 5
    angle = 25.0

    return matrix, image, start, end, delta, angle

def maps():
    img = cv2.imread("LIAN/karta-01.bmp", 0)
    ret, thresh = cv2.threshold(img, 1, 255, cv2.THRESH_BINARY_INV)
    matrix = list(thresh//255)
    image = np.copy(matrix)
    start = Point(0, 0, Point(0, 0))
    end = Point(thresh.shape[0]-1, thresh.shape[1]-1)
    delta = 50
    angle = 30.0

    return matrix, image, start, end, delta, angle


matrix, image, start, end, delta, angle = test2()

lian = LIAN(matrix, start, end, delta, angle)
if lian.run():
    for i in range(len(lian.path) - 1):
        points = getLinePoint(lian.path[i], lian.path[i+1])
        for point in points:
            # image[point.x, point.y] = 0.5
            for m in range(0, 1):
                if point.x+m < image.shape[0]:
                    image[point.x+m][point.y] = 10
                if point.x-m >= 0:
                    image[point.x-m][point.y] = 10
                if point.y+m < image.shape[1]:
                    image[point.x][point.y+m] = 10
                if point.y-m >= 0:
                    image[point.x][point.y-m] = 10

plt.imshow(image)
plt.show()
