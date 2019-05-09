from math import degrees, radians, hypot, cos, sin, atan2
import numbers
from pyx import unit

class Point:
    def __init__(self, *args, **kwargs):
        #self._x = self._y = 0

        if len(args) == 2:
            if kwargs.get('polar', False):
                r, th = args[0], radians(args[1])
                self._x = r * cos(th)
                self._y = r * sin(th)
            else:
                self._x = args[0]
                self._y = args[1]

    def __iter__(self):
        return iter([self._x, self._y])

    def __getitem__(self, i):
        return self._x if i == 0 else self._y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self._x + other.x, self._y + other.y)

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self._x - other.x, self._y - other.y)

    def __neg__(self):
        return Point(-self._x, -self._y)

    def __abs__(self):
        return hypot(self._x, self._y)

    def __str__(self):
        return "Point({0}, {1})".format(self._x, self._y)
        
    def __eq__(self, other):
        return (self._x == other.x) and (self._y == other.y)

    def __ne__(self, other):
        return (self._x != other.x) or (self._y != other.y)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @property
    def xy(self):
        return self._x, self._y

    @xy.setter
    def xy(self, xy):
        self._x, self._y = xy

    @property
    def r(self):
        return hypot(self._x, self._y)

    @r.setter
    def r(self, r):
        th = self.th
        self._x = r * cos(th)
        self._y = r * sin(th) 

    @property
    def th(self):
        return atan2(self._y, self._x)

    @th.setter
    def th(self, th):
        self._x = self.r * cos(th)
        self._y = self.r * sin(th)
    
    @property
    def a(self):
        return degrees(self.th)
    
    @a.setter
    def a(self, a):
        self.th = radians(a)



class PPoint(Point):
    def __init__(self, *args):
        super().__init__(*args, polar=True)
