
from prac_function.roman_numerals import to_roman
from prac_function.linear_search import linear_search_global


def test_global_search_multiple_chars():
    assert linear_search_global("a", ["b", "a", "n", "a", "n", "a", "s"]) == [1, 3, 5]

def test_global_search_single_char():
    assert linear_search_global("s", ["b", "a", "n", "a", "n", "a", "s"]) == [6]

def test_global_search_duplicate_char():
    assert linear_search_global("n", ["b", "a", "n", "a", "n", "a", "s"]) == [2, 4]

    
def test_01_a_single_number():
    assert to_roman(1) == "I"

def test_02_multiple_entries():
    assert to_roman(3) == 'III'

def test_03_odd_numerals():
    assert to_roman(4) == 'IV'

def test_04_all_edge_cases():
    assert to_roman(944) == 'CMXLIV'

def test_05_wrong_format():
    assert to_roman(64) == 'LXIV'