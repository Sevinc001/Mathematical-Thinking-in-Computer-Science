# 8-Puzzle Solver

The classic 3x3 sliding puzzle. State is a flat list of 9 numbers
(row by row), 0 marks the blank tile.

Goal state:
```
1 2 3
4 5 6
7 8 0
```

Write `solve(start)` that returns the shortest sequence of moves to
reach the goal, where each move is the direction the *blank* slides
(`"up"`, `"down"`, `"left"`, `"right"`). Return `None` if the puzzle
isn't solvable.

```
solve([1, 2, 3, 4, 5, 6, 7, 0, 8]) -> ["right"]
```

Use A* with the Manhattan distance heuristic - this is a general
search-based solver, not the row-by-row manual technique used for the
15-puzzle.
