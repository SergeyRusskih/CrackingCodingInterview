def debugger(n):
    return ((n & (n - 1)) == 0)

def test_2():
    assert debugger(2)

def test_3():
    assert not debugger(3)

def test_4():
    assert debugger(4)

def test_6():
    assert not debugger(6)

def test_8():
    assert debugger(8)