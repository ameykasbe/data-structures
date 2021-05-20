def max_heapify(arr, index, size):
    largest = index
    l = 2 * index + 1
    r = 2 * index + 2

    if l < size and arr[largest] < arr[l]:
        largest = l
    if r < size and arr[largest] < arr[r]:
        largest = r
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        max_heapify(arr, largest, size)


def heap_sort(arr):
    n = len(arr)

    # Convert the array to heap - Heapify the entire array
    parent_last = (n-1-1)//2
    for i in range(parent_last, -1, -1):
        max_heapify(arr, i, n)

    # Swap the largest element to the end of array. Heapify the element received on top.
    for i in range(n-1, 0, -1,):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, 0, i)

    # Return the array
    return arr


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    arr = heap_sort(arr)
    print(arr)
