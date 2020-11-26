def loop_detection(list):
    item_set = set()
    next = list.tail
    while next:
        if next in item_set:
            return next
        
        item_set.add(next)
        next = next.next

    return None