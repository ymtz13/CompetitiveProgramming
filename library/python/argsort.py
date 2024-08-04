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


points = [
    (0, 0, 0),
    (1, 0, 1),
    (5, 0, 2),
    (3, 1, 3),
    (6, 2, 4),
    (4, 4, 5),
    (5, 5, 6),
    (1, 2, 7),
    (2, 4, 8),
    (0, 1, 9),
    (0, 3, 10),
    (-1, 2, 11),
    (-2, 4, 12),
    (-1, 1, 13),
    (-2, 2, 14),
    (-3, 1, 15),
    (-6, 2, 16),
    (-1, 0, 17),
    (-6, 0, 18),
    (-3, -1, 19),
    (-6, -2, 20),
    (-1, -1, 21),
    (-5, -5, 22),
    (-1, -2, 23),
    (-3, -6, 24),
    (0, -1, 25),
    (0, -2, 26),
    (1, -4, 27),
    (2, -8, 28),
    (2, -2, 29),
    (5, -5, 30),
    (2, -1, 31),
    (6, -3, 32),
]

argsort(points)
print(points)
