def dict_implementation(nums):
    count_hash_table = dict()
    for i in nums:
        if i in count_hash_table:
            count_hash_table[i] += 1
        else:
            count_hash_table[i] = 1

    for key, value in count_hash_table.items():
        print(key, value)


if __name__ == "__main__":
    nums = [1, 1, 2, 4, 8, 3, 1, 2, 3]
    dict_implementation(nums)
