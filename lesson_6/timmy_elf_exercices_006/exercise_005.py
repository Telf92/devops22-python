# Named tuple

from collections import namedtuple

Coords = namedtuple('Coordinates', ['x', 'y']) # 1.

point_1 = Coords(1, 1) # 2.
point_2 = Coords(4, 5)

# Generate a board
board = [["-"]*10 for i in range(10)]

# mark x, y in board as *
board[point_1.x][point_1.y] = '*' #3.
board[point_2.x][point_2.y] = '*'


# Print board
for row in board:
    pass
    print(row)

x_distance = point_2.x - point_1.x
y_distance = point_2.y - point_1.y

print((x_distance**2 + y_distance**2) ** 0.5)