import numpy as np

class Brick:
    def __init__(self, index, pattern):
        self.__index = index
        self.__pattern = np.array(pattern)

        print(f"Creating brick\n{self.__pattern * self.__index}")

    @property
    def index(self):
        return self.__index
    @property
    def pattern(self):
        return self.__pattern

    @property
    def width(self):
        return self.__pattern.shape[1] #columns
    
    @property
    def height(self):
        return self.__pattern.shape[0] #rows
