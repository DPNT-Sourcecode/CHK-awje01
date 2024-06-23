from solutions.CHK import checkout_solution


def test_chk_r1():
    skus = "AAABBC"
    assert checkout_solution.checkout(skus) == 195

