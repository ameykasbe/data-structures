def print_all_triplets(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if arr[j] == (arr[i] + arr[k])/2:
                    print(f"{arr[i]}, {arr[j]}, {arr[k]}")


def print_all_triplets2(arr):
    n = len(arr)
    hash = set()
    for i in arr:
        hash.add(i)
    for i in range(n):
        for j in range(i+1, n):
            mid = (arr[i]+arr[j])/2
            if mid.is_integer() and mid in hash:
                print(f"{arr[i]}, {int((arr[i]+arr[j])/2)}, {arr[j]}")


def print_all_triplets3(arr):
    n = len(arr)
    for i in range(1, n-1):
        j = i-1
        k = i+1
        while(j >= 0 and k < n):
            mid = int(arr[j]+arr[k])/2
            if arr[i] == mid:
                print(f"{arr[j]}, {arr[i]}, {arr[k]}")
                j -= 1
                k += 1
            elif mid > arr[i]:
                j -= 1
            else:
                k += 1


# Driver code
arr = [2, 6, 9, 12, 17, 22, 31, 32, 35, 42]
print_all_triplets2(arr)
