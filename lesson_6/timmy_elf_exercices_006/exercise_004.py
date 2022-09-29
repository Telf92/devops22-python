# Queue

from collections import deque
from random import randint

names = ["pelle", "lisa", "olle", "tove", "petter"] * 10
queue = deque(maxlen=19)

while len(names):
    random_number = randint(0, 10)
    for i in range(random_number):
        if len(queue):
            print(queue.popleft())

    for i in range(random_number):
        if len(names):
            queue.append(names.pop())