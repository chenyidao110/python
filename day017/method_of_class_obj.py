class Triangle(object):

    def __init__(self, a, b, c):
        """init method"""
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    #classmethod
    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return ( p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

tria = Triangle(3, 4, 5)
print('perimeter is:%d ' % tria.perimeter())
print('area is: %d' % tria.area())
