import pytest
from common_word.commonWord import common_word

def test_common_word():
    p1 = "In a galaxy far far away"
    assert common_word(p1) == "far"

    p2 = "Taco cat ate a taco"
    assert common_word(p2) == "taco"

    p3 = "No. Try not. Do or do not. There is no try."
    assert common_word(p3) == "no"

    p4 = ""
    assert common_word(p4) == None