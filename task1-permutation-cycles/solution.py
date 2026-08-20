def cycle_decomposition(p):
    n = len(p)
    seen = [False] * n
    cycles = []

    for start in range(n):
        if seen[start]:
            continue
        cyc = []
        i = start
        while not seen[i]:
            seen[i] = True
            cyc.append(i)
            i = p[i]
        cycles.append(cyc)

    return cycles


def min_swaps_to_sort(p):
    total = 0
    for cyc in cycle_decomposition(p):
        total += len(cyc) - 1
    return total


if __name__ == "__main__":
    p = [2, 0, 1, 3]
    print(p, "->", cycle_decomposition(p))
    print("swaps needed:", min_swaps_to_sort(p))
