# Order of a Permutation

The order of a permutation is the smallest positive `k` such that
applying it `k` times gets you back to the identity. It turns out this
equals the LCM of all its cycle lengths.

Example: `p = [1, 2, 0, 4, 3]` has cycles `(0 1 2)` and `(3 4)`, lengths
3 and 2, so the order is `lcm(3, 2) = 6`.

## Question 1

Is the order of `[1, 2, 0, 4, 3, 5, 7, 6]` equal to 6?

- Yes
- No

(cycles: (0 1 2), (3 4), (5), (6 7) -> lengths 3, 2, 1, 2 -> lcm = 6 -> **Yes**)

## Question 2

Write `permutation_order(p)`.

```python
def permutation_order(p):
    ...
```

```
permutation_order([0, 1, 2, 3]) -> 1
permutation_order([1, 0, 2, 3]) -> 2
permutation_order([1, 2, 0, 4, 3]) -> 6
```
