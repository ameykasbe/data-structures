# https://leetcode.com/problems/sort-characters-by-frequency/submissions/
# Not so useful - https://www.geeksforgeeks.org/sort-a-string-according-to-the-frequency-of-characters/

def frequencySort(s):
    hash_table = dict()
    for i in s:
        if i in hash_table:
            hash_table[i] += 1
        else:
            hash_table[i] = 1

    string = [(value, key) for key, value in hash_table.items()]
    string = sorted(string, reverse=True)
    string = [value*key for value, key in string]
    return "".join(string)


string = "tree"
print(frequencySort(string))
