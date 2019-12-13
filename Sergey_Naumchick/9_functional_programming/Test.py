import pytest
from HW_01 import make_3sg_form
from HW_02 import make_ing_form


# Test for HW_01:

def test_make_3_form():
    assert make_3sg_form("try") == "tries", "must be tries"


def test_make_3_form1():
    assert make_3sg_form("brush") == "brushes", "must be brushes"


def test_make_3_form2():
    assert make_3sg_form("run") == "runs", "must be runs"


def test_make_3_form3():
    assert make_3sg_form("fix") == "fixes", "must be fixes"

#Test for HW_02:

def test_making_ing_form():
    assert make_ing_form("hug") == "hugging", "must be hugging"


def test_making_ing_form1():
    assert make_ing_form("lie") == "lying", "must be lying"

def test_making_ing_form2():
    assert make_ing_form("see") == None, "must be None"

def test_making_ing_form3():
    assert make_ing_form("move") == "moving", "must be moving"