from abc import ABC, abstractmethod

class AbstractSolver(ABC):
    def __init__(self, board, bricks):
        self.board = board
        self.bricks = bricks

    @abstractmethod
    def solve(self):
        pass