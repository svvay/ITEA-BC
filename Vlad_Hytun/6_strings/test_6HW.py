import sys
sys.path.append("D:/ITEA-BC/Vlad_Hytun/6_strings/hw")
sys.path.append("D:/ITEA-BC/Vlad_Hytun/6_strings/practice")
print(sys.path)
from P62_Hytun_Vlad import is_polindrome
from P63_Hytun_Vlad import overlapping
from HW61_Hytun_Vlad import list_to_int

def test_list_to_int():
    assert list_to_int('a','bb','ccc') == [1, 2, 3], 'Should be right'


def test_is_palindrome():
    assert is_polindrome('radar') == True, 'Should be True'
    assert is_polindrome('metro') == False, 'Should be False'


def test_overlapping():
    assert overlapping([1, 2, 3], [3, 4, 5]) == True, 'Should be True'
    assert overlapping([1, 2, 3], [6, 4, 5]) == False, 'Should be False'

test_list_to_int()
test_is_palindrome()
test_overlapping()