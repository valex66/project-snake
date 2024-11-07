from tools import syracuse, rand_cell

def test_syracuse():
    assert 2 == syracuse(4)


def test_random():
    a , b = rand_cell()
    assert (abs(a) + abs(b)) <= 38


