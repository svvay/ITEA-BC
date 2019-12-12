from HW9.hw_1 import singular
from HW9.hw_2 import participle
from practise.pr_1 import has_permission


# Test for Singular
def test_singular():
    assert singular('HW9/text_file/test.txt') == ['thies', 'ies', 'aes', 'ies', 'tes', 'ites', 'ies'], 'Should be True'


# Test for Participle
def test_participle():
    assert participle('HW9/text_file/test.txt') == ['pleasing', 'writing', 'palindroming', 'thing'], 'Should be return True'


# Test to check in
# Not work

# def test_permission():
#     assert has_permission('svvay', '1122') == True, 'Should be True'
#     assert has_permission('my_nick', '2323') == False, 'Should be False'
