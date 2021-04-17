hash_table = set()

hash_table.add(1)
hash_table.add(2)
hash_table.add(3)

l = [1, 2, 3, 4, 5, 6, 7, 8]

for i in l:
    if i in hash_table:
        print("present {}".format(i))
    else:
        hash_table.add(i)

print(hash_table)
