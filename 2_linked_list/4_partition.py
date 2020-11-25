from singly_linked_list import SinglyLinkedList

def partition(list, item):
    head = list.tail

    left = None
    right = None
    while head:
        if head.data < item:
            if left:
                left.add_node(head.data)
            else:
                left = SinglyLinkedList(head.data)
        else:
            if right:
                right.add_node(head.data)
            else:
                right = SinglyLinkedList(head.data)

        head = head.next

    if not left:
        return right
    if not right:
        return left
    
    left.head.next = right.tail
    return left

def test_simple():
    test_list = SinglyLinkedList(3)
    test_list.add_node(5)
    test_list.add_node(8)
    test_list.add_node(5)
    test_list.add_node(10)
    test_list.add_node(2)
    test_list.add_node(1)

    expectd = SinglyLinkedList(3)
    expectd.add_node(2)
    expectd.add_node(1)
    expectd.add_node(5)
    expectd.add_node(8)
    expectd.add_node(5)
    expectd.add_node(10)

    result = partition(test_list, 5)
    assert result.__eq__(expectd)
