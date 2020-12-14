def rabin_karp(string, substring):
    sums = []
    for i in range(len(string)):
        sums.append(ord(string[i]))

    for i in range(len(sums)-2, -1, -1):
        sums[i] += sums[i+1]

    substring_hash = get_string_hash(substring)
    for i in range(len(string) - len(substring)):
        current_hash = sums[i] - sums[i+len(substring)]
        if current_hash == substring_hash:
            if substring.__eq__(string[i:i+len(substring)]):
                return i
    return -1

def get_string_hash(string):
    string_hash = 0
    for _, item in enumerate(string):
        string_hash += ord(item)
    return string_hash

def test_example():
    assert rabin_karp("doe are hearing me", "ear") == 9