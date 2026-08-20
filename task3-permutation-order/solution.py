from math import gcd


def cycle_lengths(p):
    n = len(p)
    seen = [False] * n
    lengths = []
    for start in range(n):
        if seen[start]:
            continue
        length = 0
        i = start
        while not seen[i]:
            seen[i] = True
            i = p[i]
            length += 1
        lengths.append(length)
    return lengths


def permutation_order(p):
    order = 1
    for length in cycle_lengths(p):
        order = order * length // gcd(order, length)
    return order


if __name__ == "__main__":
    p = [1, 2, 0, 4, 3, 5, 7, 6]
    print(p, "-> order", permutation_order(p))
