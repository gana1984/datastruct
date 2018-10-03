'''
Created on October 2, 2018
@author: Gana Natarajan
Create and use a Stack implemented using Linked Lists.

Usage:
a = Stack() creates an empty stack.

Methods
push () - adds a node at the beginning of the stack.

pop() - removes a node from the beginning of the stack - LIFO.
pop will return the data to be stored in a variable.
If you do not provide a variable, the stack will still be popped,
and data will be lost in limbo forever :(

print() - prints the stack.

size() - returns the size of the stack.
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

class Stack():
    def __init__(self):
        self.head = None
        self.length = 0
        
    def is_empty(self):
        return self.head == None
    
    def push(self,data):
        newNode = Node(data)
        newNode.set_next(self.head)
        self.head = newNode
        self.length+=1
        
    def pop(self):
        if self.is_empty():
            raise ValueError('Cannot delete from an empty stack')
            return
        head = self.head
        popped = head.get_data()
        self.head = head.get_next()
        self.length-=1
        return popped
    
    def print(self):
        temp = self.head
        while temp:
            print(temp.get_data())
            temp = temp.get_next()
            
    def size(self):
        return self.length

## Test Run
a = Stack()
a.push(10)
a.push(5)
a.push(15)
a.push(20)
a.print()
print("The size of the stack is:",a.size())
print()
b = a.pop()
print("The popped element:",b)
print()
a.print()
print("The size of the stack is:",a.size())
