def argsort(points, p0=(1, 0)):
    x0 = p0[0]
    y0 = p0[1]

    class Point:
        def __init__(self, tup):
            self.x = x = tup[0]
            self.y = y = tup[1]
            self.rsq = x * x + y * y

            self.cross0 = cross0 = x0 * y - y0 * x
            self.inner0 = inner0 = x0 * x + y0 * y

            if inner0 >= 0:
                if x == 0 and y == 0:
                    self.quadrant = 0
                elif cross0 >= 0:
                    self.quadrant = 1
                else:
                    self.quadrant = 4
            else:
                if cross0 >= 0:
                    self.quadrant = 2
                else:
                    self.quadrant = 3

        def __eq__(self, other):
            return self.x == other.x and self.y == other.y

        def __lt__(self, other):
            if self.quadrant != other.quadrant:
                return self.quadrant < other.quadrant

            cross = self.x * other.y - self.y * other.x
            if cross == 0:
                return self.rsq < other.rsq

            return cross > 0

        def __str__(self):
            return str((self.x, self.y))

        def __repr__(self):
            return str(self)

    points.sort(key=Point)


N = int(input())
X = [tuple(map(int, input().split())) for _ in range(N)]
Q = int(input())
A = [tuple(map(int, input().split())) for _ in range(Q)]

x0, y0 = X[0]
X = [(x - x0, y - y0, -1) for x, y in X[1:]]
A = [(x - x0, y - y0, i) for i, (x, y) in enumerate(A)]

OUT = 0
IN = 1
ON = 2
ans = [OUT] * Q

points = X + A
argsort(points, X[0])

prevX = None
queue = []
for p in points:
    if p[2] == -1:
        if prevX is None:
            for _, _, i in queue:
                ans[i] = ON
        else:
            x0, y0, _ = prevX
            x1, y1, _ = p
            cross = x0 * y1 - x1 * y0
            for xq, yq, i in queue:
                # x0 t + x1 s = xq
                # y0 t + y1 s = yq
                # x0y1 t + x1y1 s = xqy1
                # x1y0 t + x1y1 s = x1yq
                # (x0y1 - x1y0) t = (xqy1 - x1yq)
                # x0y0 t + x1y0 s = xqy0
                # x0y0 t + x0y1 s = x0yq
                # (x1y0 - x0y1) s = (xqy0 - x0yq)
                # (x0y1 - x1y0) s = (x0yq - xqy0)
                # (x0y1 - x1y0) (t + s) = (xqy1 - x1yq) + (x0yq - xqy0)

                cross0 = x0 * yq - xq * y0
                cross1 = xq * y1 - x1 * yq
                diff = cross0 + cross1 - cross
                ans[i] = IN if diff < 0 else OUT if diff > 0 else ON

        queue = []
        prevX = p

    else:
        queue.append(p)

xl, yl, _ = X[-1]
for xp, yp, i in A:
    cross = xl * yp - xp * yl
    inner = xl * xp + yl * yp
    if cross == 0 and inner >= 0 and inner <= xl * xl + yl * yl:
        ans[i] = ON

for a in ans:
    print("IN" if a == IN else "OUT" if a == OUT else "ON")
