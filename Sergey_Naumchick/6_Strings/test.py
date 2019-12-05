from hw_06_01 import num_let_word
from hw_6_02 import find_longest_word
from hw_06_03 import filter_long_words
from hw_06_05 import check_numb
from hw_06_06 import mail_return_domain
from hw_06_04 import delim_words


# Test for HW lesson 6 ex. 1
def test_num_let_word():
    assert num_let_word(["aaa", "11", "b"]) == [3, 2, 1], "should be [3, 2, 1]"
    assert num_let_word(["a", "11111", "ba"]) == [1, 5, 2], "should be [1, 5, 2]"


def test_num_let_list():
    assert num_let_word([["asdfcx", "aassd"], ["qqq"], ["z"]]) == [2, 1, 1], "should be [2, 1, 1]"


def test_num_let_tuple():
    assert num_let_word(("1asad", "sasadsadasd", "sadsadsda")) == [5, 11, 9], "should be [5, 11, 9]"


# Test for HW lesson 6 ex. 2


def test_find_longest_word():
    assert find_longest_word(["mbddsfd", "1234567890", "asdasds"]) == 10, "Should be 10"


def test_find_longest_list():
    assert find_longest_word([["sadasd", "mbddsfd"], ["1234"], ["asdasds", "asdsad", "asdsadsad"]]) == 3, "Should be 3"


# Test for HW lesson 6 ex. 3
def test_filter_longest_word():
    assert filter_long_words(2, ['1111', "1", "2"]) == ['1111'], "should be ['1111']"
    assert filter_long_words(4, ['1111', "12222", "2"]) == ['12222'], "should be ['12222']"


def test_filter_longest_word():
    assert filter_long_words(2, ['1111', "1", "2"]) == ['1111'], "should be ['1111']"
    assert filter_long_words(4, ['1111', "12222", "2"]) == ['12222'], "should be ['12222']"


def test_filter_longest_word():
    assert filter_long_words(2, ['', "1", "2"]) == [], "should be []"
    assert filter_long_words(4, ['1111', "12222", "2"]) == ['12222'], "should be ['12222']"


# Test for HW lesson 6 ex. 4

def test_delim_words1():
    assert delim_words("dasd.dsf asdasd/asdasd ias") == ['dasd', 'dsf', 'asdasd', 'asdasd', 'ias'], "must be "


def test_delim_words2():
    assert delim_words("akjdh,aksdjh aaa/asd/as/asd;1") == ['akjdh', 'aksdjh', 'aaa', 'asd', 'as', 'asd',
                                                            '1'], "must be "


# Test for HW lesson 6 ex. 5

def test_check_numb():
    assert check_numb(["+380971236789", "+380809123232", "99999x9999"]) == ["+380971236789",
                                                                            "+380809123232"], 'Should be "+380971236789", "+380809123232"'


def test_check_numb1():
    assert check_numb(["0971236789", "+38080912", "99999x9999"]) == ["0971236789"], 'Should be "0971236789"'


def test_check_numb2():
    assert check_numb(["09712367", "+38080912", "99999x9999"]) == [], 'Should be []'


def test_check_numb2():
    assert check_numb(["09712367", "+38080912", "99999x9999"]) == [], 'Should be []'


# Test for HW lesson 6 ex. 6

def test_mail_return_domain():
    assert mail_return_domain(['1221', 'sergey@gmail.com', 'koko@i.ua']) == ['', 'gmail.com', 'i.ua'], "asdsa"
    assert mail_return_domain(['1221@ukr.net', 'sergey@gmail.com', 'koko@i.ua']) == ['ukr.net', 'gmail.com',
                                                                                     'i.ua'], "asdsa"
