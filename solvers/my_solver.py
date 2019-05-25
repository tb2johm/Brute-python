from abstract_solver import AbstractSolver

class MySolver(AbstractSolver):
    def solve(self):
        self.board.place(self.bricks[0],1,1)
        self.board.place(self.bricks[1],0,0)
        self.board.undo()
        self.board.place(self.bricks[1],0,0)