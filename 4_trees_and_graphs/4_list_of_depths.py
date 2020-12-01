class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, node):
        next = self
        while next.next:
            next = next.next
        next.next = node

def list_of_depths(tree, index):
    nodes = []
    nodes.append(Node(tree[index-1]))

    indexes = []
    indexes.append(index)
    while indexes:
        children = []

        node = None
        for _, i in enumerate(indexes):
            left = get_left(i)
            if left <= len(tree):
                children.append(left)
                if not node:
                    node = Node(tree[left-1])
                else:
                    node.append(Node(tree[left-1]))
                

            right = get_right(i)
            if right <= len(tree):
                children.append(right)
                if not node:
                    node = Node(tree[right-1])
                else:
                    node.append(Node(tree[right-1]))                    

        if node:
            nodes.append(node)
        indexes = children

    return nodes

def get_left(index):
    return index * 2

def get_right(index):
    return (index * 2) + 1

def test_simple():
    arr = [ 1, 
            2, 3, 
            4, 5, 6, 7, 
            8, 9, 10, 11, 12, 13, 14, 15 ]
    res = list_of_depths(arr, 1)
    assert res != None