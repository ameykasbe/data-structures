# https://leetcode.com/problems/contains-duplicate-ii/
# Solutions check in OneNote ==> Questions

def duplicate_within_k(nums, k):
    hash_table = dict()
    for i in range(len(nums)):
        if (nums[i] in hash_table) and (i - hash_table.get(nums[i]) <= k):
            return True
        else:
            hash_table[nums[i]] = i

    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(duplicate_within_k(nums, 3))
