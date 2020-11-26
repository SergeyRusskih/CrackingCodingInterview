from singly_linked_list import SinglyLinkedList

def palindrome(list1, list2):
    if not list1 or not list2:
        return False

    arr1 = []
    next = list1.tail
    while next:
        arr1.append(next.data)
        next = next.next
    
    arr2 = []
    next = list2.tail
    while next:
        arr2.append(next.data)
        next = next.next
    
    if len(arr1) != len(arr2):
        return False
        
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)

    res1 = "".join(str(s) for s in arr1)
    res2 = "".join(str(s) for s in arr2)

    return res1 == res2

def test_1():
    list1 = SinglyLinkedList(1)
    list1.add_node(2)
    list1.add_node(3)

    list2 = SinglyLinkedList(2)
    list2.add_node(1)
    list2.add_node(3)

    assert palindrome(list1, list2) == True