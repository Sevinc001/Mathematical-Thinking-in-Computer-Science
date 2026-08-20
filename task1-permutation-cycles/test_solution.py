from solution import cycle_decomposition, min_swaps_to_sort


def test_basic():
    assert cycle_decomposition([2, 0, 1, 3]) == [[0, 2, 1], [3]]

def test_identity():
    assert cycle_decomposition([0, 1, 2, 3]) == [[0], [1], [2], [3]]

def test_one_big_cycle():
    assert cycle_decomposition([1, 2, 3, 0]) == [[0, 1, 2, 3]]

def test_swaps_identity():
    assert min_swaps_to_sort([0, 1, 2, 3]) == 0

def test_swaps_basic():
    assert min_swaps_to_sort([2, 0, 1, 3]) == 2

def test_swaps_full_cycle():
    assert min_swaps_to_sort([1, 2, 3, 0]) == 3

def test_swaps_two_transpositions():
    assert min_swaps_to_sort([1, 0, 3, 2]) == 2


if __name__ == "__main__":
    test_basic()
    test_identity()
    test_one_big_cycle()
    test_swaps_identity()
    test_swaps_basic()
    test_swaps_full_cycle()
    test_swaps_two_transpositions()
    print("all good")
