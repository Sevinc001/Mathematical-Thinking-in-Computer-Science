from solution import solve, GOAL, SIZE

DELTA = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}


def apply_moves(start, moves):
    state = list(start)
    for m in moves:
        blank = state.index(0)
        r, c = divmod(blank, SIZE)
        dr, dc = DELTA[m]
        nr, nc = r + dr, c + dc
        new_blank = nr * SIZE + nc
        state[blank], state[new_blank] = state[new_blank], state[blank]
    return tuple(state)


def test_already_solved():
    assert solve(list(GOAL)) == []

def test_one_move():
    start = [1, 2, 3, 4, 5, 6, 7, 0, 8]
    moves = solve(start)
    assert apply_moves(start, moves) == GOAL

def test_few_moves():
    start = [1, 2, 3, 4, 0, 6, 7, 5, 8]
    moves = solve(start)
    assert apply_moves(start, moves) == GOAL

def test_harder():
    start = [8, 1, 3, 4, 0, 2, 7, 6, 5]
    moves = solve(start)
    assert apply_moves(start, moves) == GOAL

def test_unsolvable():
    start = [1, 2, 3, 4, 5, 6, 8, 7, 0]
    assert solve(start) is None


if __name__ == "__main__":
    test_already_solved()
    test_one_move()
    test_few_moves()
    test_harder()
    test_unsolvable()
    print("all good")
