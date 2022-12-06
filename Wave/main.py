import numpy as np
import cv2
import matplotlib.pyplot as plt
from point import Point
from wave_1 import Wave


img = cv2.imread('Wave/karta-01.bmp', 0)
ret, thresh = cv2.threshold(img, 1, 255, cv2.THRESH_BINARY_INV)
matrix = list(thresh // 255)
start = Point(305, 165)
end = Point(690, 1290)

wave = Wave(matrix, start, end)

if wave.run():
    route = np.array(matrix)

    for point in wave.path:
        x = point.x
        y = point.y
        for m in range(1, 3):

            if x+m < route.shape[0]:
                route[x+m][y] = 10
            if x-m >= 0:
                route[x-m][y] = 10
            if y+m < route.shape[1]:
                route[x][y+m] = 10
            if y-m >= 0:
                route[x][y-m] = 10

        route[x][y] = 10

    plt.imshow(route)
    plt.show()
else:
    print("Path not found")
