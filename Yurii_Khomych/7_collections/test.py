from hw.ex1 import main as hw_main

from examples import my_func


def test_myfunc():
    assert my_func("Word my") == True
