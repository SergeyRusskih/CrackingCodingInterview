from singly_linked_list import SinglyLinkedList

def sum_list(list1, list2):
    next1 = list1.tail
    next2 = list2.tail

    increase_next = False
    result = []
    while next1 or next2:
        val1 = 0
        if next1:
            val1 = next1.data
        val2 = 0
        if next2:
            val2 = next2.data

        combined = val1 + val2
        if increase_next:
            combined += 1

        if combined > 9:
            combined %= 10
            increase_next = True
        else:
            increase_next = False

        result.insert(0, combined)

        if next1:
            next1 = next1.next
        if next2:
            next2 = next2.next

    if increase_next:
        result.insert(0, 1)

    return int("".join(str(s) for s in result))


def test_example():
    list1 = SinglyLinkedList(7)
    list1.add_node(1)
    list1.add_node(9)

    list2 = SinglyLinkedList(5)
    list2.add_node(9)
    list2.add_node(2)

    assert sum_list(list1, list2) == 1212

def test_1_sorter():
    list1 = SinglyLinkedList(7)
    list1.add_node(1)

    list2 = SinglyLinkedList(5)
    list2.add_node(9)
    list2.add_node(2)

    assert sum_list(list1, list2) == 312

def test_2_sorter():
    list1 = SinglyLinkedList(7)
    list1.add_node(1)
    list1.add_node(5)

    list2 = SinglyLinkedList(5)
    list2.add_node(9)

    assert sum_list(list1, list2) == 612