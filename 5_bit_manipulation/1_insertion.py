def insertion(n, m, i, j):
    mask = ((1 << 33) - 1 << j+1) | (1 << i) - 1
    return bin((n & mask) | (m << i))

def test_insertion():
    n = 0b10000100001
    m = 0b10011
    result = insertion(n, m, 2, 6)
    assert result == bin(0b10001001101)
    