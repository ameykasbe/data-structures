 def push(self, new_data):
      nn = Node(new_data)
       if self.head == None:
            self.head = nn
            return
        nn.next = self.head
        self.head.prev = nn
        self.head = nn


dll = DoublyLinkedList()
dll.push(50)
dll.push(40)
dll.push(30)
dll.push(20)
dll.push(10)
