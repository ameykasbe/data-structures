# https://leetcode.com/problems/number-of-good-pairs/
# https://www.geeksforgeeks.org/count-index-pairs-equal-elements-array/

def num_good_pairs(nums):
    count_hash_table = dict()
    for i in nums:
        if i in count_hash_table:
            count_hash_table[i] += 1
        else:
            count_hash_table[i] = 1

    total = 0
    for key, value in count_hash_table.items():
        if value > 1:
            total += value * (value - 1) / 2

    return total


if __name__ == "__main__":
    nums = [1, 2, 3, 1, 1, 3]
    print(num_good_pairs(nums))
