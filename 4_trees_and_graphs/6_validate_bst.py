def validate_bst(bst, i):
    if i > len(bst):
        return True
        
    root = bst[i-1]
    left = get_left(i)
    if left <= len(bst) and bst[left-1] and bst[left-1] > root:
        return False

    right = get_right(i)
    if right <= len(bst) and bst[right-1] and bst[right-1] <= root:
        return False

    return validate_bst(bst, left) and validate_bst(bst, right)

def get_left(i):
    return i * 2

def get_right(i):
    return (i * 2) + 1

def test_validate_should_return_true():
    bst = [
        6,
        4, 8,
        2, None, 7, 10
    ]

    assert validate_bst(bst, 1)

def test_validate_should_return_false():
    bst = [
        6,
        7, 8,
        2, None, 7, 10
    ]

    assert validate_bst(bst, 1) == False