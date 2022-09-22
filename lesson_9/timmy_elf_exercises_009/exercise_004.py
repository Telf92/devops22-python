# Circle

from math import pi #ii.

# 1.
# i.
class Circle:
    def __init__(self, diagonal):
        self.diagonal = diagonal
        self.color = 'grey'
        self.area = self.calc_area()
        self.circumference = self.calc_circumference()

    def calc_area(self): #iii. # v.
        return pi * (self.diagonal / 2) ** 2

    def calc_circumference(self): # iv.
        return self.diagonal * pi

    def set_color(self, color): # vi.
        self.color = color

def main():
    circle = Circle(2)
    print(circle.area)
    print(circle.circumference)
    print(circle.color)
    circle.set_color("red") #vii.
    print(circle.color)

if __name__ == '__main__':
    main()