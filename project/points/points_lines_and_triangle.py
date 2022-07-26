import json
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.point = (self.x, self.y)

    def __getitem__(self, item):
        return self.point[item]

    def __str__(self):
        return f'{self.point}'


class Tringle:
    def __init__(self, point1, point2, point3, pointcheck):
        self.x1 = point1[0]
        self.y1 = point1[1]
        self.x2 = point2[0]
        self.y2 = point2[1]
        self.x3 = point3[0]
        self.y3 = point3[1]
        self.pointcheck = pointcheck
        self.xp = pointcheck[0]
        self.yp = pointcheck[1]
        self.sectors = []
        self.counter = 0
        self.circumference = 0
        self.check_if_posible_flag = True
        self.sector_maker()
        self.check_if_posible(self.sectors[0], self.sectors[1], self.sectors[2])

    def sector_maker(self):
        AB = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        BC = math.sqrt(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
        CA = math.sqrt(((self.x1 - self.x3) ** 2) + ((self.y1 - self.y3) ** 2))

        self.sectors.append(AB)
        self.sectors.append(BC)
        self.sectors.append(CA)
        return self.sectors

    def check_if_posible(self, a, b, c):
        if a + b > c and b + c > a and c + a > b:
            return print('Trojkat mozliwy')
        else:
            self.check_if_posible_flag = False
            return print('Trojkat niemozliwy') and exit(0)

    def tringle_area(self, x1, y1, x2, y2, x3, y3):
        self.area_tringle_from_points = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
        return self.area_tringle_from_points

    def check_point_in_tringle(self):
        ABC = self.tringle_area(self.xp, self.yp, self.x2, self.y2,
                                self.x3,
                                self.y3)
        PAB = self.tringle_area(self.xp, self.yp, self.x2, self.y2,
                                self.x3,
                                self.y3)
        PBC = self.tringle_area(self.x1, self.y1, self.xp, self.yp,
                                self.x3,
                                self.y3)
        PCA = self.tringle_area(self.x1, self.y1, self.x2, self.y2,
                                self.xp,
                                self.yp)
        print(f"Pole trójkąta to: {ABC}")
        if ABC == (PAB + PBC + PCA):
            return print('punkt w trojkacie')
        else:
            return print('punkt nie w trojkacie')

    def tringleCircumference(self):
        for sector in self.sectors:
            self.circumference += sector
        return self.circumference



if __name__ == '__main__':
    point1 = Point(2, 3)
    point2 = Point(2, 5)
    point3 = Point(5, 3)
    pointcheck = Point(3, 3)
    tringle = Tringle(point1, point2, point3, pointcheck)
    tringle.check_point_in_tringle()
    print(tringle.tringleCircumference())
