def bit_to_win(n):
    str_value = bin(n)[2:]

    result, index, count, last_zero_index = 0, 0, 0, 0,

    zero_found = False
    while len(str_value) > index:
        if str_value[index] == '1':
            count += 1
        elif not zero_found:
            last_zero_index = index
            zero_found = True
            count += 1
        elif count:
            result = max(count, result)
            count = 0
            index = last_zero_index
            zero_found = False

        index += 1

    return max(result, count)


def test_sample():
    assert bit_to_win(0b11011101111) == 8