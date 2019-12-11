from homework.DefSumPR_4 import sums
from homework.FuncCharPR_3 import func
from homework.is_memberPR_5 import counts
from homework.overlappingPR_6 import overlapping
from homework.LengthPR2 import length
from homework.MaxMinHW import maxmin
from homework.MaxFiPR import maxi

############################################################################

def test_sums():
    assert sums([3, 1, 10, 0,5], 4, 1) == 14, 'Should be return 6'
def test_sums_t():
    assert sums([3, 3, 3], 3, 1) == 9, 'Should be return 9'

############################################################################


def test_func():
    assert func('A') == True, 'Should be return True'
def test_func_lower():
    assert func('a') == False, 'Should be return False'
def test_func_2():
    assert func('D') == False, 'Should be return False'
def test_func_3():
    assert func('3') == False, 'Should be return False'

#############################################################################


def test_counts():
    assert counts('a', 'a') == True, 'Should be return True'
def test_counts_upper():
    assert counts('A', 'a') == False, 'Should be return False'
def test_counts_int():
    assert counts('3', '9, 4, 5') == False, 'Should be return False'
def test_counts_int2():
    assert counts('3', '9, 4, 2, 3') == True, 'Should be return True'


##############################################################################


def test_overlapping():
    assert overlapping('a, b, c', 'b, c, f') == True, 'Should be return True'
def test_overlapping_upper():
    assert overlapping('A, B, C', 'b, c, f') == True, 'Should be return True'
def test_overlapping_f():
    assert overlapping('D', 'e, a, f') == False, 'Should be return False'


##############################################################################


def test_length_list():
    assert length('234') == 3, 'Should be True'
def test_length_str():
    assert length('asdf') == 4, 'Should be True'
def test_length_num():
    assert length('a, s, d') == 7, 'Should be True'


##############################################################################


def test_maxmin_max():
    assert maxmin([3, 4, 5]) == 5, 'Should be 5'
def test_maxmin_str():
    assert maxmin([3, 4, f]) == False, 'Should be False'
def test_maxmin():
    assert maxmin([3, 4, 5]) == 5, 'Should be False'


################################################################################


def test_maxi_max():
    assert maxi(4, 5) == 5, 'Should be 5'
def test_maxi_fa():
    assert maxi(4, 4) == True, 'Should be True'

###################################################################################



