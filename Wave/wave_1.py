from collections import deque
from point import Point

class Wave():

    row = [-1, 0, 0, 1, -1, 1, 1, -1]
    col = [0, -1, 1, 0, -1, -1, 1, 1]
    queue = deque()
    path = []
    dist = 1000000

    def __init__(self, matrix, start, end):
        self.matrix = matrix
        self.start = start
        self.end = end

        self.width = len(self.matrix)
        self.height = len(self.matrix[0])
        self.visited = [[False for _ in range(self.height)] for _ in range(self.width)]
        self.visited[self.start.x][self.start.y] = True
        
    def run(self):
        self.queue.append((self.start, 0, []))

        while self.queue:
            point, dist, path = self.queue.popleft()

            if point == self.end:
                self.dist = dist
                self.path = path
                break

            for k in range(8):
                if self.checkPoint(point.x + self.row[k], point.y + self.col[k]):

                    self.visited[point.x + self.row[k]][point.y + self.col[k]] = True
                    newPoint = Point(point.x + self.row[k], point.y + self.col[k])

                    newPath = path.copy()
                    newPath.append(newPoint)
                    self.queue.append((newPoint, dist + 1, newPath))

        if self.dist != 1000000:
            return True
        else:
            return False

    def checkPoint(self, x, y):
        return (x >= 0) and (x < self.width) and (y >= 0) and (y < self.height) and \
                self.matrix[x][y] == 0 and not self.visited[x][y]
