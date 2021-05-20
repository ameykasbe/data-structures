import sys


class MaxHeap:
    def __init__(self, capacity):
        self.harr = [None]*capacity
        self.capacity = capacity
        self.size = 0

    def parent(self, i):
        return (i-1)//2

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def get_max(self):
        if self.size <= 0:
            print("Heap empty.")
            return
        return self.heap[0]

    def extract_max(self):
        if self.size <= 0:
            print("Heap empty.")
            return
        if self.size == 1:
            self.size -= 1
            return self.harr[0]

        root = self.harr[0]
        self.harr[0] = self.harr[self.size - 1]
        self.size -= 1
        self.max_heapify(0)
        return root

    def max_heapify(self, index):
        largest = index
        l = self.left(index)
        r = self.right(index)
        if l < self.size and self.harr[largest] < self.harr[l]:
            largest = l
        if r < self.size and self.harr[largest] < self.harr[r]:
            largest = r
        if largest != index:
            self.harr[index], self.harr[largest] = self.harr[largest], self.harr[index]
            self.max_heapify(largest)

    def insert(self, key):
        if self.size >= self.capacity:
            print("Heap overflow.")
            return

        i = self.size
        self.harr[i] = key
        self.size += 1

        while(i > 0 and self.harr[i] > self.harr[self.parent(i)]):
            self.harr[i], self.harr[self.parent(
                i)] = self.harr[self.parent(i)], self.harr[i]
            i = self.parent(i)

    def increase_key(self, index, new_value):
        if index >= self.size:
            print("Index out of bound.")
            return

        self.harr[index] = new_value
        while(index > 0 and self.harr[index] > self.harr[self.parent(index)]):
            self.harr[index], self.harr[self.parent(
                index)] = self.harr[self.parent(index)], self.harr[index]
            index = self.parent(index)

    def delete_key(self, index):
        self.increase_key(index, sys.maxsize)
        self.extract_max()

    def heapify_tree(self):
        n = self.size
        parent_last = (n-1-1)//2
        for i in range(parent_last, -1, -1):
            self.max_heapify(i)


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]

    maxheap = MaxHeap(len(arr))
    maxheap.harr = arr
    maxheap.size = len(arr)

    maxheap.heapify_tree()
    print(maxheap.harr)

    # [13, 11, 12, 5, 6, 7]
