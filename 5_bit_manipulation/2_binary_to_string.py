def binary_to_string(n):
    remainder = int(str(n)[2:])
    result = bin(remainder)
    if len(result) > 34:
        return "ERROR"
    return result

def test_simple():
    assert binary_to_string(0.2) == bin(0b10)