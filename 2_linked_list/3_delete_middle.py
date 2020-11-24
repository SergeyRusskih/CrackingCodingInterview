from singly_linked_list import SinglyLinkedList

def delete_middle(list: SinglyLinkedList, node):
    current = list.tail
    while current.next:
        if current.next.data == node:
            current.next = current.next.next
            break
        current = current.next

def test_simple():
    test = SinglyLinkedList(1)
    test.add_node(2)
    test.add_node(3)
    test.add_node(4)

    delete_middle(test, 3)

    result = SinglyLinkedList(1)
    result.add_node(2)
    result.add_node(4)

    assert test == result