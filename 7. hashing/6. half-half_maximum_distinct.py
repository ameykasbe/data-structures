# https://www.geeksforgeeks.org/equally-divide-into-two-sets-such-that-one-set-has-maximum-distinct-elements/

def distribution(arr):
    p1 = list()
    p2 = dict()
    n = len(arr)
    for i in arr:
        if len(p2) != n/2 and i not in p2:
            p2[i] = 1
        elif len(p1) != n/2:
            # Will be triggered only if i is in p2 or p2 is now full with distinct values. If length of p2 has reached half, then there is no chance p1 has also reached half as both have half capacity to that of arr.
            p1.append(i)
        else:
            # Will be triggered only if i is in p2 and p1 has reached max capacity of half.
            p2[i] += 1
    return sum(p2.values())


# Driver code
if __name__ == '__main__':
    arr = [1, 1, 2, 1, 3, 4, 1, 1, 1, 1]
    print(distribution(arr))
