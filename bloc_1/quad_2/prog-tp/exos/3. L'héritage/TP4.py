import math

class Point:
    def __init__(self, x=0., y=0.):
        self.__x = x
        self.__y = y

    @property
    def getX(self):
        return self.__x

    @property
    def getY(self):
        return self.__y

    def distance_from_xy(self, x: float, y: float):
        return math.sqrt((x - self.__x)**2 + (y - self.__y)**2)

    def distance_from_point(self, point):
        if isinstance(point, Point):
            return math.sqrt((point.getX - self.__x)**2 + (point.getY - self.__y)**2)
        else:
            return None


class Triangle:
    def __init__(self, point1: Point, point2: Point, point3: Point):
        self.__points = [point1, point2, point3]

    def perimeter(self):
        side1 = self.__points[0].distance_from_point(self.__points[1])
        side2 = self.__points[1].distance_from_point(self.__points[2])
        side3 = self.__points[2].distance_from_point(self.__points[0])

        return side1 + side2 + side3


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())