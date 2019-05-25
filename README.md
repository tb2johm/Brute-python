# Brute-python
This is the brute puzzle.

The task is to create a solver plugin that solves the puzzle.

This is an early version, where it's very easy to just hard code a solver. However, the task is
to create a solver that solves the pussle automatically.

### Rules
* All bricks need too be placed
* A brick can only be used once
* No other files other than then *my_solver.py* is allowed to be changed

## Requirements
* Python3
* pip3
* virtualenv

## Instructions
* Clone the repo
* Setup the virtual environment
  `pip3 virtualenv venv && source venv/bin/activate && pip3 install -r requirements.txt`
* Look in the *Brute.py* file to see all the bricks
* Look in the *solvers/my_solver.py* file to undertand how to place the bricks on the board
* Modify the *solve* function in *solvers/my_solver.py*
* Run `python3 Brute.py`

