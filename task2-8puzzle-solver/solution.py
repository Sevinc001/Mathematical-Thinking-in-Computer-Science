import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
SIZE = 3
MOVES = [(-1, 0, "up"), (1, 0, "down"), (0, -1, "left"), (0, 1, "right")]


def is_solvable(state):
    tiles = [x for x in state if x != 0]
    inv = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                inv += 1
    return inv % 2 == 0


def manhattan(state):
    dist = 0
    for i, v in enumerate(state):
        if v == 0:
            continue
        r, c = divmod(i, SIZE)
        gr, gc = divmod(v - 1, SIZE)
        dist += abs(r - gr) + abs(c - gc)
    return dist


def neighbors(state):
    blank = state.index(0)
    r, c = divmod(blank, SIZE)
    for dr, dc, name in MOVES:
        nr, nc = r + dr, c + dc
        if 0 <= nr < SIZE and 0 <= nc < SIZE:
            new_blank = nr * SIZE + nc
            s = list(state)
            s[blank], s[new_blank] = s[new_blank], s[blank]
            yield tuple(s), name


def solve(start):
    start = tuple(start)
    if not is_solvable(start):
        return None
    if start == GOAL:
        return []

    counter = 0
    heap = [(manhattan(start), counter, start)]
    g = {start: 0}
    parent = {}
    closed = set()

    while heap:
        _, _, cur = heapq.heappop(heap)
        if cur in closed:
            continue
        if cur == GOAL:
            path = []
            while cur in parent:
                cur, move = parent[cur]
                path.append(move)
            path.reverse()
            return path
        closed.add(cur)

        for nxt, move in neighbors(cur):
            if nxt in closed:
                continue
            new_g = g[cur] + 1
            if new_g < g.get(nxt, float("inf")):
                g[nxt] = new_g
                parent[nxt] = (cur, move)
                counter += 1
                heapq.heappush(heap, (new_g + manhattan(nxt), counter, nxt))

    return None


if __name__ == "__main__":
    start = [1, 2, 3, 4, 5, 6, 7, 0, 8]
    print(solve(start))
