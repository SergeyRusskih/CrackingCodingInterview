def next_number(n):
    index = len(n) - 1
    arr = list(n)

    smalest = None
    largest = None
    while arr[index] != 'b':
        if arr[index] == '0':
            if not smalest and index != len(n) - 1 and arr[index-1] == '1':
                smalest = swap(arr, index, index-1)
            if not largest and arr[index+1] == '1':
                largest = swap(arr, index, index+1)

        if smalest and largest:
            return smalest, largest

        index -= 1

    return smalest, largest

def swap(input, index1, index2):
    arr = input.copy()
    tmp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = tmp
    return "".join(arr)

def test_simple():
    smalest, largest = next_number('0b001011011')
    assert smalest == '0b001010111'
    assert largest == '0b001011101'