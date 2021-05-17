def set_implementation(nums):
    hash_table = set()

    hash_table.add(1)
    hash_table.add(2)
    hash_table.add(3)

    for i in nums:
        if i in hash_table:
            print("present {}".format(i))
        else:
            hash_table.add(i)


if __name__ == "__main__":
    nums = [1, 1, 2, 4, 8, 3, 1, 2, 3]
    set_implementation(nums)
