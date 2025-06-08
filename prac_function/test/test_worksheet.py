from prac_function.worksheet import *

def test_one_armstrong_func():
    assert check_armstrong_func(999) ==  [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
def test_two_armstrong_func():
    assert check_armstrong_func(8) == [1, 2, 3, 4, 5, 6, 7]

def test_one_anagramI_func():
    assert anagramI_func("taco", "cato") == True
def test_two_anagramI_func():
    assert anagramI_func("34cde", "3cDe4") == True


