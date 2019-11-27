from hw.ex1 import max_in_list


def test_max_in_list_tuples():
    assert max_in_list((1, 2, 3)) == 3, "Should be 3"


def test_max_in_list():
    assert max_in_list([1, 2, 3, 3]) == 3, "Should be 3"

def test_max_in_list_failed():
    assert max_in_list(1) == None, "Should be 3"
