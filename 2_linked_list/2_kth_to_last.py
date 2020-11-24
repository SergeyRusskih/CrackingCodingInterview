from singly_linked_list import SinglyLinkedList

def kth_to_last(list, i):
    next = list.tail
    arr = []
    while next:
        arr.append(next)
        next = next.next

    return arr[len(arr) - (i + 1)]

def test_2_from_last():
    list_under_test = SinglyLinkedList(1)
    list_under_test.add_node(9)
    list_under_test.add_node(3)
    list_under_test.add_node(8)
    list_under_test.add_node(7)

    assert kth_to_last(list_under_test, 2).data == 3