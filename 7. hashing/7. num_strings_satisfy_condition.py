# https://www.geeksforgeeks.org/number-of-strings-that-satisfy-the-given-condition/

import sys


def count_strings(s):
    hash = set()
    for position in range(len(s[0])):
        max_number = -sys.maxsize
        for index in range(len(s)):
            if int(s[index][position]) > max_number:
                max_number = int(s[index][position])

        for index in range(len(s)):
            if int(s[index][position]) == max_number:
                hash.add(s[index])
    return hash


# Driver code
s = ["223", "232", "112"]
s = ["999", "112", "232"]
print(count_strings(s))
