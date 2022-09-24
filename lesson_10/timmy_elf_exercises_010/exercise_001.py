# Override

# 1.
class Bicycle:
    def __init__(self):
        self.speed = 2
    
    def accelerate(self):
        self.speed += 1

    def slow(self):
        self.speed -= 1

# 2.
class MTB(Bicycle):
    pass

# 3. 
class MTB(Bicycle):
    def slow(self):
        self.speed -=1.2

# 4.
bicycle = Bicycle()
bicycle.slow()
print(bicycle.speed)

mtb = MTB()
mtb.slow()
print(mtb.speed)