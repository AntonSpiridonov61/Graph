from point import Point

# MidPoint
def getCirclePoint(point, delta, width, height):
    def addPoint(x, y):
        if x >= 0 and y >= 0 and x < width and y < height:
            result.append(Point(x, y, point))

    result = []
    X = point.x
    Y = point.y

    addPoint(X, Y+delta)
    addPoint(X, Y-delta)
    addPoint(X-delta, Y)
    addPoint(X+delta, Y)

    x = 0
    y = delta
    p = 1 - delta

    while x < y:
        if p < 0:
            p += 2 * x + 1
        else:
            p += 1 - 2 * y + 2 * x
            y -= 1
        x += 1

        if y < x:
            break

        addPoint(x+X, y+Y)
        addPoint(-x+X, y+Y)
        addPoint(x+X, -y+Y)
        addPoint(-x+X, -y+Y)

        if y != x:
            addPoint(y+X, x+Y)
            addPoint(-y+X, x+Y)
            addPoint(y+X, -x+Y)
            addPoint(-y+X, -x+Y)

    return result

# функция для вычисления нуль-траектории между точками
def getLinePoint(a, b):
    points = []

    dx = b.x - a.x
    dy = b.y - a.y

    sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
    sign_y = 1 if dy > 0 else -1 if dy < 0 else 0

    if dx < 0:
        dx = -dx
    if dy < 0:
        dy = -dy

    if dx > dy:
        pdx, pdy = sign_x, 0
        es, el = dy, dx
    else:
        pdx, pdy = 0, sign_y
        es, el = dx, dy

    x, y = a.x, a.y

    error, t = el / 2, 0

    points.append(Point(x, y))

    while t < el:
        error -= es
        if error < 0:
            error += el
            x += sign_x
            y += sign_y
        else:
            x += pdx
            y += pdy
        t += 1
        points.append(Point(x, y))

    return points
