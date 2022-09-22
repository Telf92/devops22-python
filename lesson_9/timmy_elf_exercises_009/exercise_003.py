# methods

# 1.
# i.
class Square:
    def __init__(self, side):
        self.side = side
    
# ii.
# a.    
    def area(self):
        return float(self.side ** 2) # b.
    
# iii.    
    def circumference(self): # a.
        return 4.0 * self.side # b.

def main():
    square_one = Square(2)
    print(square_one.area())
    print(square_one.circumference())

    square_two = Square (3.5)
    print(square_two.area())
    print(square_two.circumference())

if __name__ == '"__main__':
    main()

# Example how to instantinate and call methods
# class MyClass:
    # Your code

# if __name__ == '__main__':
#    my_object = MyClass("args")
#    print(my_class.my_method())
#
#    my_another_object = MyClass("args")
#    print(my_another_object.my_method())