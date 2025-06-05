from linear_search import linear_search_global


# tests for linear_search_global
def test_global_search_multiple_chars():
    assert linear_search_global("a", ["b", "a", "n", "a", "n", "a", "s"]) == [1, 3, 5]

def test_global_search_single_char():
    assert linear_search_global("s", ["b", "a", "n", "a", "n", "a", "s"]) == [6]

def test_global_search_duplicate_char():
    assert linear_search_global("n", ["b", "a", "n", "a", "n", "a", "s"]) == [2, 4]