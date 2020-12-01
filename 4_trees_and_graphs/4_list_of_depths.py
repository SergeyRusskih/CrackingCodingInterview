class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def list_of_depths(tree, index):
    nodes = []
    nodes.append(Node(tree[index-1]))

    indexes = []
    indexes.append(index)
    while indexes:
        children = []

        node = Node(0)
        for _, i in enumerate(indexes):
            left = get_left(i)
            if left < len(tree):
                children.append(left)
                node.next = Node(tree[left])
                node = node.next
                

            right = get_right(i)
            if right < len(tree):
                children.append(right)
                node.next = Node(tree[right])
                node.

        nodes.append(node)
        inexes = children

def get_left(index):
    return index ** 2

def get_right(index):
    return (index ** 2) + 1

def test_simple():
    arr = [ 1, 
            2, 3, 
            4, 5, 6, 7, 
            8, 9, 10, 11, 12, 13, 14, 15 ]
    res = list_of_depths(arr, 1)
    assert res != None