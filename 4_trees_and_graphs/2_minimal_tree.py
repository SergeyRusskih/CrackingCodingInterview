from graph import Graph, Node

class Node:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

def minimal_tree(arr, start, end):
    if end == start:
        return None

    middle = start + ((end - start) // 2)
    node = Node(arr[middle])
    node.left = minimal_tree(arr, start, middle)
    node.right = minimal_tree(arr, middle+1, end)

    return node
    

def test_tree():
    arr = [1, 2, 3, 4, 5, 6, 7]
    middle = len(arr) // 2
    res = minimal_tree(arr, 0, len(arr))
    assert res != None