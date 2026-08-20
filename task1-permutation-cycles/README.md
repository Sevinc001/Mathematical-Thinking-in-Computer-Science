# Permutation Cycles

Given a permutation `p` of `0..n-1` (a list where `p[i]` is the value
sitting at position `i`), write two functions.

### cycle_decomposition(p)

Split the permutation into its cycles. Return a list of lists - each
inner list is one cycle, starting from its smallest element. Order the
cycles by their first element. Fixed points (length-1 cycles) count too.

```
cycle_decomposition([2, 0, 1, 3])
-> [[0, 2, 1], [3]]
```
(0 -> p[0]=2 -> p[2]=1 -> p[1]=0, back where we started. 3 maps to itself.)

### min_swaps_to_sort(p)

How many swaps (not necessarily adjacent elements) does it take to sort
`p` into `0, 1, 2, ..., n-1`? A cycle of length `k` needs `k-1` swaps,
so just sum that over all cycles.

```
min_swaps_to_sort([2, 0, 1, 3]) -> 2
```

Run `python test_solution.py` to check.
