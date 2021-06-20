class Heap():
    def __init__(self, lista):
        self.data = lista
        self.heap_size = len(lista)
        #self.build_max_heap()
    
    parent = lambda s, i: i//2
    left = lambda s, i: 2*i
    right = lambda s, i: 2*i +1

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        largest = i
        if l < self.heap_size:
            if self.data[l] > self.data[i]:
                largest = l
        if r < self.heap_size:
            if self.data[r] > self.data[largest]:
                largest = r

        if largest != i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.max_heapify(largest)
            
    def build_max_heap(self):
        for i in reversed(range(self.heap_size//2+1)):
            self.max_heapify(i)
    
    def heapsort(self):
        self.build_max_heap()
        for i in reversed(range(1, len(self.data))):
            self.data[0], self.data[i] = self.data[i], self.data[0]
            self.heap_size -= 1
            self.max_heapify(0)
        
        return self.data

class DinamicSet():
    def __init__(self, n:int=16):
        self.data = [None]*n

    @staticmethod
    def insert(data, value, index):
        data[index] = value
        return data

    @staticmethod
    def delete(data, index):
        value, data[index] = data[index],  None
        return (data, value)

class Stack(DinamicSet):
    def __init__(self, n:int=16):
        super().__init__(n)
        self.top = -1

    def push(self, value):
        self.top +=1
        self.data = super().insert(self.data, value, self.top)
        
    def pop(self):
        if self.stack_empty():
            raise IndexError('Underflow')
        
        self.data, value = super().delete(self.data, self.top)
        self.top -= 1

        return value
    
    def stack_empty(self):
        return self.top < 0

class Queue(DinamicSet):
    def __init__(self, n:int=16):
        super().__init__(n)
        self.tail = 0
        self.head = 0
    
    def enqueue(self, value):
        self.data = super().insert(self.data, value, self.tail)
        self.tail += 1

    def dequeue(self):
        self.data, value = super().delete(self.data, self.head)
        self.data = [*self.data[1:], None]
        self.tail -=1

        return value

class Node():
    def __init__(self, key=None, prev:object=None, next:object=None, index=0) -> None:
        self.key = key
        self.prev = prev
        self.next = next
        self.index = index

    def __str__(self):
        return str(self.key)

    __repr__ = __str__

class Dbl_Linked_List():
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None

    def append(self, value):
        self.length += 1
        if self.head == None:
            self.head = Node(key=value)
            self.tail = self.head
            
        else:
            a = self.head
            while a.next:
                a = a.next
            
            a.next = Node(key=value, prev=a)
            self.tail = a

    def pop(self):
        if self.tail == None:
            raise IndexError('Cannot pop 0 length list')

        self.length -= 1
        a = self.tail
        self.tail = self.tail.prev 
        if self.tail:
            self.tail.next = None
        return a

    def search(self, value) -> Node:
        a = self.head
        while a.next or a == self.tail:
            if a.key == value:
                return a
            a = a.next
    
    def delete(self, index):
        if self.length <= index or self.length == 0:
            raise IndexError('Cannot delete from list')
        
        self.length -=1
        
        if index == 0:
            self.head = self.head.next
        if index == self.length-1:
            self.tail = self.tail.prev
        else:
            a = self.head
            for _ in range(index):
                a = a.next

            a_prev = a.prev
            a_next = a.next
            a_prev.next = a_next
            a_next.prev = a_prev

class Tree_Node():
    def __init__(self, key=None, r_child:object=None, l_child:object=None) -> None:
        self.key = key
        self.right = r_child
        self.left = l_child

    def __str__(self):
        return str(self.key)

    __repr__ = __str__

class Binary_Tree():
    def __init__(self):
        self.root = None
    
    def tree_insert(self, value):
        x = self.root
        y = None
        while x != None:
            y = x # Guarda valor antes do None
            x = x.left if x.key < value else x.right

        # x == None
        if y == None: # Tree was empty
            self.root = Tree_Node(key=value)
        elif y.key < value:
            y.right = Tree_Node(key=value)
        else:
            y.left = Tree_Node(key=value)
    
    def tree_delete(self, value):
        pass
    
    def tree_search(self, value):
        pass
