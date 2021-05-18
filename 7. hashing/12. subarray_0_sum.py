def sub_array_exists(arr):
    n = len(arr)
    hash = set()
    sum = 0
    for i in arr:
        sum += i
        if sum == 0 or sum in hash:
            return True
        hash.add(sum)
    return False


if __name__ == "__main__":
    arr = [-3, 2, 1, 3, 1, 6]
    if sub_array_exists(arr):
        print("Found a sunbarray with 0 sum")
    else:
        print("No Such sub array exits!")
