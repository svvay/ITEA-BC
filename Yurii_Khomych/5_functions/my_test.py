import parser, test, unittest_example
import sys as library_sys

library_sys.path

sys = 1
# result = sum([1, 2, 3])
#
# assert sum([1, 2, 1]) == 6, "Should be 6"


def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_pow():
    assert pow(2, 2) == 4, "Should be 6"


test_sum()
test_pow()
print("Everything passed")

import unittest

