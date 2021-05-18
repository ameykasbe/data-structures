# https://www.geeksforgeeks.org/find-repetitive-element-1-n-1/

def find_repeating1(arr, n):
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                return arr[i]
    return None


def find_repeating2(arr, n):
    arr = sorted(arr)
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            return arr[i]
    return None


def find_repeating3(arr, n):
    hash = set()
    for i in arr:
        if i in hash:
            return i
        hash.add(i)
    return None


def find_repeating4(arr, n):
    diff = sum(arr) - int(n*(n+1)/2)
    if not diff:
        return None
    return n+diff


def find_repeating5(arr, n):
    res = 0
    for i in range(1, n+1):
        res ^= i
    for i in arr:
        res ^= i
    res ^= n
    if res == n:
        return None
    return res


def find_repeating6(arr, n):
    for i in range(n):
        if arr[abs(arr[i])-1] < 0:
            return abs(arr[i])
        arr[abs(arr[i])-1] *= -1
    return None

    # Driver Code
arr = [9, 8, 2, 6, 1, 10, 5, 3, 4, 7]
n = len(arr)
print(find_repeating1(arr, n))
print(find_repeating2(arr, n))
print(find_repeating3(arr, n))
print(find_repeating4(arr, n))
print(find_repeating5(arr, n))
print(find_repeating6(arr, n))
