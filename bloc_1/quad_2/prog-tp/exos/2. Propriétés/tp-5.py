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


if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(1, 1)
    print(p1.distance_from_point(p2))
    print(p2.distance_from_xy(2, 0))