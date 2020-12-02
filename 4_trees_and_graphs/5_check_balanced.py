class Node:
    def __init__(self, left, right):
        self.right = right
        self.left = left

def check_balanced(tree):
    nodes = []
    nodes.append(tree) 
    not_balanced_count = 0
    balanced = True
    while nodes:
        children = []
        for i, item in enumerate(nodes):
            if item.left:
                children.append(item.left)
            if item.right:
                children.append(item.right)

            if not item.left or not item.right:
                balanced = False
        else:
            nodes = children
            if not_balanced_count > 1:
                return False
            if not balanced:
                not_balanced_count += 1

    return True

def test_check_perfectly_balanced():
    tree = Node(
      Node(Node(None, None), Node(None, None)),
      Node(Node(None, None), Node(None, None))
    )

    assert check_balanced(tree)

def test_check_one_difference():
    tree = Node(
      Node(Node(None, None), None),
      Node(Node(None, None), Node(None, None))
    )

    assert check_balanced(tree)

def test_check_two_difference():
    tree = Node(
      None,
      Node(Node(None, None), Node(None, None))
    )

    assert check_balanced(tree) == False

