class Hash:
    def __init__(self, max_size):
        self.max_size = max_size
        self.hash_table = [[0 for i in range(2)]
                           for j in range(self.max_size+1)]

    def insert(self, element):
        if element >= 0:
            self.hash_table[element][0] = 1
            return
        self.hash_table[abs(element)][1] = 1

    def search(self, element):
        if element >= 0:
            return self.hash_table[element][0] == 1
        return self.hash_table[abs(element)][1] == 1


if __name__ == "__main__":

    elements = [-1, 9, -5, -8, -5, -2]
    ht = Hash(10)

    for element in elements:
        ht.insert(element)

    print(ht.hash_table)

    print(ht.search(-8))
    print(ht.search(8))
