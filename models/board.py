import numpy as np

from .brick import Brick

class Board:
    def __init__(self, height, width):
        if height < 1: raise ValueError("height must be > 0")
        if width < 1: raise ValueError("width must be > 0")

        self.__height = height
        self.__width = width
        self.__board = np.zeros((height, width), dtype=int)

        self.__placements = []
        self.__placed = 0

        print(f"Creating board:\n{self.__board}")
    
    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    def place(self, brick, x, y):
        if not type(brick) is Brick: raise ValueError("Bad brick")
        if x < 0 or \
            y < 0 or \
            x >= self.width or \
            y >= self.height or \
            x + brick.width > self.__width or \
            y + brick.height > self.__height : raise ValueError("Bad position")

        repa = brick.pattern.copy() #repa = resized_pattern
        for _ in range(x):
            repa = np.insert(repa, 0, 0, axis=1)
        for _ in range(y):
            repa = np.insert(repa, 0, 0, axis=0)
        for _ in range(self.width - brick.width - x):
            repa = np.insert(repa, repa.shape[1], 0, axis=1)
        for _ in range(self.height - brick.height - y):
            repa = np.insert(repa, repa.shape[0], 0, axis=0)

        if self.__placed > 0:
            result = np.add(self.__placements[self.__placed - 1].pattern, repa)
        else:
            result = repa.copy()

        if np.amax(result) > 1:
            print(f"Overlapping!\n{result}")
            return False
        else:
            self.__placed += 1
            self.__placements.append(Placement(brick, x, y, repa, result))
            print(f"Successful placement!\n{self}")
            return True

    def undo(self):
        if self.__placed < 1: raise ValueError("Can't undo what isn't done...")

        self.__placements.pop()
        self.__placed -= 1
        
        print(f"Removed last brick, ramaining board\n{self}")

    @property
    def solved(self):
        if self.__placed < 1: return False
        return np.size(self.__placements[self.__placed - 1].pattern) == np.sum(self.__placements[self.__placed - 1].pattern)

    @property
    def current(self):
        if self.__placed < 1: return self.__board
        return self.__placements[self.__placed - 1].pattern

    def __str__(self):
        board = self.__board.copy()
        for placement in self.__placements:
            board = np.add(placement.repa * placement.brick.index, board)

        return str(board)


class Placement:
    def __init__(self, brick, x, y, repa, pattern):
        self.__brick = brick
        self.__x = x
        self.__y = y
        self.__repa = repa
        self.__pattern = pattern
    
    @property
    def brick(self):
        return self.__brick

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def repa(self):
        return self.__repa
    @property
    def pattern(self):
        return self.__pattern