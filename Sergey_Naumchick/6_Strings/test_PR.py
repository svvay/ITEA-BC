from PR_06_01 import generate_n_chars
from PR_06_02 import is_palindrom
from PR_06_03 import overlaping
from PR_06_04 import first_word_string
from PR_06_05 import last_word_string
from PR_06_06 import found_first_2_let
from PR_06_07 import find_date

# 1. Practice lesson 6 ex. 1
def test_generate_n_chars():
    assert generate_n_chars(5, "s") == "sssss", "should be sssss"


def test_generate_n_chars1():
    assert generate_n_chars(10, "1") == "1111111111", "should be 1111111111"


# 2. Practice lesson 6 ex. 2

def test_is_palindrome():
    assert is_palindrom("asa") == "asa", 'should be "asa"'


def test_is_palindrome1():
    assert is_palindrom("РАДАР") == "радар", 'should be "asa"'


# 3. Practice lesson 6 ex. 3

def test_overlaping1():
    assert overlaping(["hello", "Mike", "John"], ["hello", "Mike", "Jon"]) == ["hello",
                                                                               "Mike"], 'Should be ["hello","Mike"]'


# 4. Practice lesson 6 ex. 4

def test_first_word_string():
    assert first_word_string("Hello, my name is Vasya") == ['Hello'], "should be ['Hello']"


# 5. Practice lesson 6 ex. 5

def test_last_word_string():
    assert last_word_string("Hello, my name is Vasya") == ['Vasya'], "should be ['Vasya']"


def test_last_word_string():
    assert last_word_string("my name is Ann") == ['Ann'], "should be ['Ann']"


# 5. Practice lesson 6 ex. 6

def test_found_first_2_let():
    assert found_first_2_let("This is the first day of new life") == ['Th', 'is', 'th', 'fi', 'da', 'of', 'ne',
                                                                      'li'], "must be ['Th', 'is','th','fi','da','of','ne','li']"

# 5. Practice lesson 6 ex. 7

def test_find_date():
    assert find_date('Amit 34-3456 12.05.2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009') == ['12.05.2007', '11-11-2011', '12-01-2009'], "should ba ['12.05.2007', '11-11-2011', '12-01-2009']"