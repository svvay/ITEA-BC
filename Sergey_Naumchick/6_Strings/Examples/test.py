from hw_06_01 import num_let_word


def test_num_let_word():
    assert num_let_word(["aaa", "11", "b"]) == [3, 2, 1], "should be [3, 2, 1]"


def test_num_let_words():
    assert num_let_word(["asdfcx", "qqq", "z"]) == [6, 3, 1], "should be [6, 3, 1]"


from hw_6_02 import num_longest_word


def test_num_longest_word():
    assert num_longest_word(["mbddsfd", "1234567890", "asdasds"]) == 10, "Should be 10"


def test_num_longest_word2():
    assert num_longest_word(["mbddsfd", "1234", "asdasds"]) == 7, "Should be 7"


from hw_06_03 import filter_long_words


def test_filter_longest_word():
    assert filter_long_words(2, ['1111', "1", "2"]) == ['1111'], "should be ['1111']"

def test_filter_longest_words():
    assert filter_long_words(4, ['1111', "12222", "2"]) == ['12222'], "should be ['12222']"
