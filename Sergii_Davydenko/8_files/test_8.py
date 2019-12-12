from HW.hw_1 import semordnilap
from HW.hw_2 import popular
from PR.pr_2 import sto

# Test overlaping semordnilap


def test_overlapping():
    assert semordnilap('HW/file_txt/test.txt') == ['asa'], 'Should be True'


# Test popular string
# NOT WORK

# def test_popular():
#     assert popular('HW/file_txt/test.txt') == '[("you'll", 3), ('the', 3), ('to', 3), ('of', 2), ('that', 2)]'
#

