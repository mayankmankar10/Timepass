from src.math_operations import add, subtract

def test_add():
    assert add(1, 2) == 3
    assert add(1, 3) == 4
    assert add(1, 5) == 6


def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(3, 1) == 2
    assert subtract(5, 1) == 4

    
