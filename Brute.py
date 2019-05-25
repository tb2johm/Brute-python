#!./venv/bin/python3
import inspect

from pluginbase import PluginBase

from models.board import *
from models.brick import *
import abstract_solver

plugin_base = PluginBase(package="solvers")
plugin_source = plugin_base.make_plugin_source(searchpath=['./solvers'])
solver_plugins = [plugin_source.load_plugin(solver) for solver in plugin_source.list_plugins()]
solvers = []
for name, obj in inspect.getmembers(solver_plugins[0], inspect.isclass):
    if issubclass(obj, abstract_solver.AbstractSolver):
        if not name == abstract_solver.AbstractSolver.__name__:
            solvers.append(obj)

def main():

    print("----Setup----")
    board = Board(2, 4)

    bricks = []
    bricks.append(Brick(1, [[1,1,1]]))
    bricks.append(Brick(2, [[1,1,1,1],
                           [1,0,0,0]]))

    print("----Playing----")

    solver = solvers[0](board, bricks)
    solver.solve()

    print(f"Final pattern\n{board}")
    if board.solved:
        print("YES!")
    else:
        print("Game over...")


if __name__ == "__main__":
    main()