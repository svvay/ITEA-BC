from l_5_fun_practise_yeroshenko_4 import x_sum
from l_5_fun_practise_yeroshenko_4 import x_sum
from l_5_fun_practise_yeroshenko_1 import maxx

def test_x_sum():
    assert (1 + 2 + 3 + 33) == 39, "Should be 39"
    assert (1 + -2 + 3 + 33) == 35, "Should be 35"
    assert (-1 + -2 + -3 + -33) == -39, "Should be -39"
    print("success test_x_sum")

def test_the_mult():
    assert (-1 * -3 * 2 * 4) == 24, "Should be 24"
    assert (9 * 9 * 2) == 162, "Should be 162"
    assert (-2 * 3 * 5 * 7) == -210, "Should be -210"
    print("success test_the_mult")

def test_maxx():
    assert max(9, -89, 356, -799) == 356, "Should be 356"
    assert max(-3, -52, -365) == -3, "Should be -3"
    assert max(0, -55, -69) == 0, "Should be 0"
    print("success test_maxx")
