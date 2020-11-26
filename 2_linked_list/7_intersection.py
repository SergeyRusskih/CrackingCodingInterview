from singly_linked_list import SinglyLinkedList

def intersection(list1, list2):
    node_set = set()
    next = list1.tail
    while next:
        node_set.add(next)
        next = next.next

    next = list2.tail
    while next:
        if next in node_set:
            return next

        next = next.next

    return None

def test_simple():
    list1 = SinglyLinkedList(1)
    list1.add_node(2)
    list1.add_node(3)
    list1.add_node(4)

    list2 = SinglyLinkedList(1)
    list2.add_node(3)
    list2.head.next = list1.head

    result = intersection(list1, list2)
    assert result == list1.head