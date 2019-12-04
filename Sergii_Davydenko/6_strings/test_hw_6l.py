
from Pw.Pw_3 import overlapping
from Pw.Pw_2 import palindrom
from HW.longest_word_2 import find_longest_word
from HW.Filter_3 import filter_long_words

###################################################################

def test_overlapping():
    assert overlapping('asd', 'sdf') == True, 'Should be True'
    assert overlapping('ASD', 'sdf') == False, 'Should be False'


#####################################################################

def test_palindrom():
    assert palindrom('ada') == True, 'Should be True'
    assert palindrom('toshiba') == False, 'Should be False'

#####################################################################

def test_longest_word_2():
    assert find_longest_word(['sdfghj', 'bvcx', 'qwe'], 0) == 6, 'Should be 6'
    assert find_longest_word(['DFG/./', 'bvcx', 'qwe'], 0) == 6, 'Should be 6'

#########################################################################

def test_filter_long_words():
    assert filter_long_words(['qwer', 'asdf', 'zxcvb'], 4) == ['zxcvb'], 'Should be [zxcvb]'
    assert filter_long_words(['qw', 'asdf', 'zxcvb'], 2) == ['asdf', 'zxcvb'], 'Should be [asdf, zxcvb]'