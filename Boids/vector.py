import math
from typing import Self


class Vector:

    def __init__(self, dx=0.0, dy=0.0):
        self.dx = dx
        self.dy = dy

    def __repr__(self):
        return f"X: {self.dx}, Y: {self.dy}, "

    def __eq__(self, other) -> bool:
        if isinstance(other, Vector):
            other = (other.dx, other.dy)
        return self.dx == other[0] and self.dy == other[1]

    def __add__(self, other) -> Self:
        if isinstance(other, Vector):
            other = (other.dx, other.dy)
        return Vector((other[0] + self.dx), (other[1] + self.dy))

    def __sub__(self, other) -> Self:
        if isinstance(other, Vector):
            other = (other.dx, other.dy)
        return Vector((self.dx - other[0]), (self.dy - other[1]))

    def __mul__(self, other: float) -> Self:

        return Vector((self.dx * other), (self.dy * other))

    def __truediv__(self, other: float) -> Self:

        return Vector((self.dx / other), (self.dy / other))

    def set(self, x=0, y=0):
        self.dx = x
        self.dy = y

    def set_radians(self, radians):
        magnitude = self.get_magnitude()
        self.dx = math.cos(radians)
        self.dy = math.sin(radians)

        self.set_magnitude(magnitude)

    def get_radians(self):
        return math.atan2(self.dy, self.dx) % (2 * math.pi)

    def set_magnitude(self, magnitude):
        radians = self.get_radians()
        self.dx = math.cos(radians) * magnitude
        self.dy = math.sin(radians) * magnitude

    def get_magnitude(self):
        return math.sqrt(self.dx ** 2 + self.dy ** 2)

    def clamp_magnitude(self, cap):
        if self.get_magnitude() > cap:
            self.set_magnitude(cap)
        elif self.get_magnitude() < -cap:
            return self.set_magnitude(-cap)

    def get_opposite(self):
        return Vector(dx=-self.dx, dy=-self.dy)

    def rotate(self, angle):
        radians = (self.get_radians() + angle) % (2 * math.pi)
        self.set_radians(radians)

    @staticmethod
    def get_sum(vectors):
        vector_sum = Vector(0, 0)
        for vector in vectors:
            vector_sum += vector
        return vector_sum

    @staticmethod
    def get_average(vectors):
        vector_sum = Vector.get_sum(vectors)
        x = vector_sum.dx / len(vectors)
        y = vector_sum.dy / len(vectors)
        return Vector(x, y)
