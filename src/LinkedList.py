'''
Created on September 10, 2018
@author: Gana Natarajan
Create and use a singly connected linked list.

Usage:
a = LinkedList() creates an empty Linked List instance.

Methods
push () - adds a node at the beginning of the linked list.

append () - adds a node at the end of the linked list.

insert(index) - adds a node at the index mentioned. Default index is 0.
insert() results in push behavior.

delete(index) - deletes a node at the index mentioned. Default index is 0.
delete() results in a pop behavior - deletes from beginning of list

reverse(recurse = False) - reverses the linked list in place.
recurse = True uses the recursive method. Default is iterative method.

print(reverse = False, recurse = False) - prints the linked list.
reverse = True will print the linked list in reverse order.
recurse = True will use the recursive method to print.
Default is forward, non-recursive.

size() returns the size of the linked list.
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

class LinkedList():
    def __init__(self):
        self.head = None
        self.length = 0
        
    def is_empty(self):
        return self.head == None
    
    def push(self,data):
        temp = Node(data)
        temp.set_next(self.head)
        self.head = temp
        self.length+=1
   
    def append(self,data):
        temp = self.head
        if temp:
            while temp.get_next() != None:
                temp = temp.get_next()
            temp.set_next(Node(data))
        else:
            self.head = Node(data)
        self.length+=1
        
    def insert(self,data,index=None):
        if index == 0 or index == None:
            self.push(data)
            return
        if index>self.length:
            raise ValueError('The given index exceeds list length')
            return
        temp1 = Node(data)
        temp2 = self.head
        for i in range(0,index-1):
            temp2 = temp2.get_next()
        temp1.set_next(temp2.get_next())
        temp2.set_next(temp1)
        self.length+=1

    def delete(self,index = None):
        if self.is_empty():
            raise ValueError('Cannot delete from an empty list')
            return
        temp = self.head
        if index == 0  or index == None:
            self.head = temp.get_next()
            self.length-=1
            return
        if index>self.length:
            raise ValueError('The given index exceeds the list length')
            return
        for i in range(0,index-1):
            temp = temp.get_next()
        temp.set_next(temp.get_next().get_next())
        self.length-=1
        
    def reverse(self,recurse=False):
        if self.is_empty():
            raise ValueError('Cannot reverse an empty list')
            return
        if self.length == 1:
            return
        if recurse == False:
            current = self.head
            prev = None
            while current != None:
                nxt =  current.get_next()
                current.set_next(prev)
                prev = current
                current = nxt
            self.head = prev
        elif recurse == True:
            self._reverse(self.head)

    def _reverse(self,head):
        if head.get_next() == None:
            self.head = head
            return
        self._reverse(head.get_next())
        head.get_next().set_next(head)
        head.set_next(None)
        
    def print(self, reverse = False, recurse = False):
        if reverse == False:
            if recurse == False:
                self._print(self.head)
            else:
                self._recprint(self.head)
        else:
            if recurse == False:
                self._rev_print(self.head)
            else:
                self._rev_print_rec(self.head)

    def _print(self, head):
        while head:
            print(head.get_data())
            head = head.get_next()
            
    def _print_rec(self, head):
        if head == None:
            return
        print(head.get_data())
        self._print_rec(head.get_next())
        
    def _rev_print(self, head):
        temp = list()
        while head:
            temp.append(head.get_data())
            head = head.get_next()
        for i in reversed(temp):
            print(i)
            
    def _rev_print_rec(self,head):
        if head == None:
            return
        self._rev_print_rec(head.get_next())
        print(head.get_data())
        
    def size(self):
        return self.length
      
##Test Run        
new = LinkedList()
new.append(2)
new.append(4)
new.insert(3,1)
new.append(5)

new.print()
print()
new.print(True)
print()
new.print(True,True)

new.delete(2)
print()
new.print()

    
