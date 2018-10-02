'''
Created on September 17, 2018
@author: Gana Natarajan
Create and use a doubly connected linked list.

Usage:
a = DLL() creates an empty Doubly Linked List instance.

Methods
push () - adds a node at the beginning of the linked list.

append () - adds a node at the end of the linked list.

insert(index) - adds a node at the index mentioned. Default index is 0.
insert() results in push behavior.

delete(index) - deletes a node at the index mentioned. Default index is 0.
delete() results in a pop behavior - deletes from beginning of list

reverse(recurse = False) - reverses the linked list in place.
recurse = True uses the recursive method. Default is iterative method.

print(reverse = False) - prints the linked list.
reverse = True will print the linked list in reverse order.
Default is forward.

size() returns the size of the linked list.
'''
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def get_prev(self):
        return self.prev
    def set_data(self,new):
        self.data = new
    def set_next(self,new):
        self.next = new
    def set_prev(self,new):
        self.prev = new

class DLL():
    def __init__(self):
        self.head = None
        self.length = 0
        
    def is_empty(self):
        return self.head == None

    def push(self,data):
        newNode = Node(data)
        newNode.set_next(self.head)
        newNode.set_prev(None) #This is redundant, but left in for symmetry
        if self.head != None:
            self.head.set_prev(newNode)
        self.head = newNode
        self.length+=1

    def append(self,data):
        newNode = Node(data)
        temp = self.head
        if temp:
            while temp.get_next():
                temp = temp.get_next()
            temp.set_next(newNode)
            newNode.set_prev(temp)
        else:
            self.head = newNode
        self.length+=1

    def insert(self, data, index = None):
        if index == 0 or index == None:
            self.push(data)
            return
        if index == self.length:
            self.append(data)
        if index > self.length:
            raise ValueError('The given index exceeds list length')
            return
        newNode = Node(data)
        temp = self.head
        for i in range(0,index-1):
            temp = temp.get_next()
        newNode.set_next(temp.get_next())
        temp.get_next().set_prev(newNode)
        newNode.set_prev(temp)
        temp.set_next(newNode)
        self.length+=1

    def delete(self, index = None):
        if self.is_empty():
            raise ValueError('Cannot delete from an empty list')
            return
        temp = self.head
        if index == 0 or index ==  None:
            self.head = temp.get_next()
            temp.get_next().set_prev(None)
            self.length-=1
            return
        if index>self.length:
            raise ValueError('The given index exceeds the list length')
            return
        for i in range(0,index-1):
            temp = temp.get_next()
        if index == self.length-1:
            temp.set_next(None)
            self.length-=1
            return
        temp.get_next().get_next().set_prev(temp)
        temp.set_next(temp.get_next().get_next())
        self.length-=1

    def reverse(self, recurse=False):
        if self.is_empty():
            raise ValueError('Cannot reverse an empty list')
            return
        if self.length == 1:
            return
        if recurse == False:
            current = self.head
            prev = None
            while current:
                prev = current.get_prev()
                current.set_prev(current.get_next())
                current.set_next(prev)
                current = current.get_prev()
            self.head = prev.get_prev()
        elif recurse == True:
            self._reverse(self.head)

    def _reverse(self,head):
        if head.get_next() == None:
            self.head = head
            return
        self._reverse(head.get_next())
        head.get_next().set_next(head)
        head.set_prev(head.get_next())
        head.set_next(None)
        
    def print(self, reverse = False):
        if reverse:
            self._reverse_print(self.head)
        else:
            self._print(self.head)
        
    def _print(self, head):
        while head:
            print(head.get_data())
            head = head.get_next()
            
    def _reverse_print(self,head):
        while head.get_next():
            head = head.get_next()
        while head:
            print(head.get_data())
            head = head.get_prev()

    def size(self):
        return self.length

##Test Run
a = DLL()
a.append(5)
a.push(2)
a.push(3)
a.append(4)
a.insert(8,2)
a.insert(10)
a.delete(2)
a.print()
print()
a.print(True)
print('Size of list is: ', a.size())
print()
a.reverse()
a.print()
print()
a.reverse(True)
a.print()
