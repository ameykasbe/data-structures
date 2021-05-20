import sys


class Heap:
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

    def get_min(self):
        if self.size <= 0:
            print("Heap empty.")
            return
        return self.heap[0]

    def extract_min(self):
        if self.size <= 0:
            print("Heap empty.")
            return
        if self.size == 1:
            self.size -= 1
            return self.harr[0]

        root = self.harr[0]
        self.harr[0] = self.harr[self.size - 1]
        self.size -= 1
        self.min_heapify(0)
        return root

    def min_heapify(self, index):
        smallest = index
        l = self.left(index)
        r = self.right(index)
        if l < self.size and self.harr[smallest] > self.harr[l]:
            smallest = l
        if r < self.size and self.harr[smallest] > self.harr[r]:
            smallest = r
        if smallest != index:
            self.harr[index], self.harr[smallest] = self.harr[smallest], self.harr[index]
            self.min_heapify(smallest)

    def insert(self, key):
        if self.size >= self.capacity:
            print("Heap overflow.")
            return

        i = self.size
        self.harr[i] = key
        self.size += 1

        while(i > 0 and self.harr[i] < self.harr[self.parent(i)]):
            self.harr[i], self.harr[self.parent(
                i)] = self.harr[self.parent(i)], self.harr[i]
            i = self.parent(i)

    def decrease_key(self, index, new_value):
        if index >= self.size:
            print("Index out of bound.")
            return

        self.harr[index] = new_value
        while(index > 0 and self.harr[index] < self.harr[self.parent(index)]):
            self.harr[index], self.harr[self.parent(
                index)] = self.harr[self.parent(index)], self.harr[index]
            index = self.parent(index)

    def delete_key(self, index):
        self.decrease_key(index, -sys.maxsize)
        self.extract_min()


if __name__ == "__main__":
    heap = Heap(10)
    heap.insert(3)
    heap.insert(1)
    heap.insert(15)
    heap.insert(5)
    heap.insert(4)
    heap.insert(45)
    heap.insert(10)

    print(heap.harr[:heap.size])

    heap.decrease_key(3, 2)

    print(heap.harr[:heap.size])
    print(heap.extract_min())
    print(heap.extract_min())
    print(heap.extract_min())

    print(heap.harr[:heap.size])
    heap.delete_key(2)
    print(heap.harr[:heap.size])
