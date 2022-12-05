from queue import PriorityQueue
from point import Point, dist
from vector import angle
from function import *
import matplotlib.pyplot as plt


class LIAN():
    def __init__(self, matrix, start, end, delta, angle):
        self.matrix = matrix
        self.map = matrix
        self.start = start
        self.end = end
        self.delta = delta
        self.angle = angle

        self.open = PriorityQueue()
        self.open.put((self.start.weight, self.start))

        self.closed = []
        self.path = []

    def run(self):
        print("run")
        while not self.open.empty():
            a = self.open.get()[1]
            if a == self.end:
                self.getPath(a)
                return True
            if a not in self.closed:
                self.closed.append(a)
                self.expand(a)
            #     self.map[a.x][a.y] = 2
            # if len(self.closed) % 2000 == 0:
            #     plt.imshow(self.map)
            #     plt.show()
        print(self.closed)
        return False
 
    def expand(self, point):
        SUCC = getCirclePoint(point, self.delta, len(self.matrix), len(self.matrix[0]))

        if dist(point, self.end) <= self.delta and angle(point.linkPoint, point, point, self.end) <= self.angle:
            SUCC.append(Point(self.end.x, self.end.y, point))

        for item in SUCC:
            isVisit = False
            isImpassable = False

            if self.matrix[item.x][item.y] == 1:
                continue

            if point != self.start and angle(point.linkPoint, point, point, item) > self.angle:
                continue

            for p in getLinePoint(point, item):
                if self.matrix[p.x][p.y] == 1:
                    isImpassable = True
                    break
            if isImpassable:
                continue
            for close in self.closed:
                if item.linkPoint is not None and item == close and item.linkPoint == close.linkPoint:
                    isVisit = True
                    break
            if isVisit:
                continue

            item.weight = point.weight + dist(item, self.end)
            self.open.put((item.weight, item))
            # self.map[item.x][item.y] = 0.4

    def getPath(self, point):
        if point.linkPoint is not None:
            self.getPath(point.linkPoint)
            self.path.append(point)