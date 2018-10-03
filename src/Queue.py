'''
Created on October 2, 2018
@author: Gana Natarajan
Create and use a Queue implemented using Linked Lists.

Usage:
a = Queue() creates an empty stack.

Methods
enque() - adds a node at the end of the queue.

deque() - removes a node from the beginning of the stack - FIFO.
deque will return the data to be stored in a variable.
If you do not provide a variable, the queue will still be dequeued,
and data will be lost in limbo forever :(

print() - prints the queue.

size() - returns the size of the queue.
'''

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self,new):
        self.data = new
    def set_next(self,new):
        self.next = new

class Queue():
    def __init__(self):
        self.head = None
        self.length = 0
        
    def is_empty(self):
        return self.head == None
    
    def enque(self,data):
        newNode = Node(data)
        newNode.set_next(self.head)
        self.head = newNode
        self.length+=1
        
    def deque(self):
        if self.is_empty():
            raise ValueError('Cannot delete from an empty queue')
            return
        head = self.head
        if self.length == 1:
            dqued = head.get_data()
            self.head = None
            self.length-=1
            return dqued
        while head.get_next().get_next():
            head = head.get_next()
        dqued = head.get_next().get_data()
        head.set_next(None)
        self.length-=1
        return dqued
    
    def print(self):
        if self.is_empty():
            print('Queue is empty')
            return
        temp = self.head
        while temp:
            print(temp.get_data())
            temp = temp.get_next()
            
    def size(self):
        return self.length

a = Queue()
a.enque(10)
a.enque(20)
a.enque(30)
a.print()
print("Queue size is:", a.size())
print()
b = a.deque()
print("Dequeued Element:", b)
print()
a.print()
print("Queue size is:", a.size())
