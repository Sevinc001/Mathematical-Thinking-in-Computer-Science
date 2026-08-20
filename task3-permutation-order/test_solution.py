from solution import permutation_order


def test_identity():
    assert permutation_order([0, 1, 2, 3]) == 1

def test_single_swap():
    assert permutation_order([1, 0, 2, 3]) == 2

def test_lcm_case():
    assert permutation_order([1, 2, 0, 4, 3]) == 6

def test_given_example():
    assert permutation_order([1, 2, 0, 4, 3, 5, 7, 6]) == 6

def test_full_cycle():
    assert permutation_order([1, 2, 3, 4, 0]) == 5

def test_all_fixed():
    assert permutation_order([0, 1, 2, 3, 4, 5]) == 1


if __name__ == "__main__":
    test_identity()
    test_single_swap()
    test_lcm_case()
    test_given_example()
    test_full_cycle()
    test_all_fixed()
    print("all good")
