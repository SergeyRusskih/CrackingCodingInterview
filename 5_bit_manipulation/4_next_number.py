def next_number(n):
    index = len(n) - 1
    arr = n.split()
    while arr[index] != b:
        pass


def test_simple():
    smalest, largest = next_number('0b001011011')
    assert smalest == '0b001010111'
    assert largest == '0b001011101'