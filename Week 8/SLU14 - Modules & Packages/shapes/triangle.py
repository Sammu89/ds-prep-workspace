class Triangle:

    def __init__(self,base,height):
        self.base = base
        self.height = height

    def get_area(self):
        area = (self.base * self.height) / 2
        return area


def is_equilateral (a,b,c):
    if a==b==c:
        return True
    else:
        return False

description="this is a module named triangle"