from solutions.CHK import checkout_solution


def test_chk_r1():
    skus = "AAABB"
    assert checkout_solution.checkout(skus) == 175

    skus = "AAAA"
    assert checkout_solution.checkout(skus) == 180

    skus = "AAAAA"
    assert checkout_solution.checkout(skus) == 230

    skus = "BBB"
    assert checkout_solution.checkout(skus) == 75
