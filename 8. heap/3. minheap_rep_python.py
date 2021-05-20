from heapq import heappush, heappop, heapify
import sys


class MinHeap:
    def __init__(self):
        self.harr = []

    def parent(self, i):
        return (i-1)//2

    def get_min(self):
        return self.heap[0]

    # Change
    def extract_min(self):
        return heappop(self.harr)

    # Change
    # def min_heapify(self, index):
    #     smallest = index
    #     l = self.left(index)
    #     r = self.right(index)
    #     if l < self.size and self.harr[smallest] > self.harr[l]:
    #         smallest = l
    #     if r < self.size and self.harr[smallest] > self.harr[r]:
    #         smallest = r
    #     if smallest != index:
    #         self.harr[index], self.harr[smallest] = self.harr[smallest], self.harr[index]
    #         self.min_heapify(smallest)

    # Change
    def insert(self, key):
        heappush(self.harr, key)

    def decrease_key(self, index, new_value):
        self.harr[index] = new_value
        while(index > 0 and self.harr[index] < self.harr[self.parent(index)]):
            self.harr[index], self.harr[self.parent(
                index)] = self.harr[self.parent(index)], self.harr[index]
            index = self.parent(index)

    def delete_key(self, index):
        self.decrease_key(index, -sys.maxsize)
        self.extract_min()


if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(3)
    heap.insert(1)
    heap.insert(15)
    heap.insert(5)
    heap.insert(4)
    heap.insert(45)
    heap.insert(10)

    print(heap.harr)

    heap.decrease_key(3, 2)

    print(heap.harr)
    print(heap.extract_min())
    print(heap.extract_min())
    print(heap.extract_min())

    print(heap.harr)
    heap.delete_key(2)
    print(heap.harr)
