# The Euclidean Algorithm
def gcd(a, b):
    if a == 0 or b == 0:
        return 0

    c = a % b
    if c == 0:
        return b

    return gcd(b, c)
    

def test_first_zero():
    assert gcd(0, 5) == 0

def test_second_zero():
    assert gcd(5, 0) == 0

def test_simple():
    assert gcd(252, 105) == 21