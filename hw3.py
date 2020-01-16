#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 23:13:35 2019

@author: ojasbardiya
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return '%d' % (self.data)
    def __repr__(self):
        return '%d' % (self.data)

class Linkedlist:
    def __init__(self, node_data):
        n_node = Node(node_data)
        self.first = n_node
        self.last = n_node
        self.n = 1
    def append(self, new_data):
        new_node = Node(new_data)
        self.last.next = new_node
        self.last = new_node
        self.last.next = None
        self.n = self.n + 1
    def __iter__(self):
        return self.generator()
    #def next(self):
        #if self.count == self.n:
            #raise StopIteration
        #val = self.first.data
        #self.first = self.first.next
        #self.count = self.count + 1
        #return val
    def generator(self):
        count = 0
        current_node = self.first
        while count < self.n:
            yield current_node
            current_node = current_node.next
            count += 1
    def __str__(self):
        return_string = "["
        node_values = []
        cur_node = self.first
        while cur_node is not None:
            node_values.append(str(cur_node.data))
            cur_node = cur_node.next
        for i in node_values:
            return_string = return_string + i + "->"
        return_string += "]"
        return return_string
    def __repr__(self):
        return "'" + str(self) + "'"
    def __len__(self):
        return self.n
    def __getitem__(self, index):
        if index < 0 or index >= self.n:
            raise IndexError
        cur_node = self.first
        count = 0
        while count < index:
            cur_node = cur_node.next
            count += 1
        return cur_node.data
    def __add__(self, value):
        list_copy = Linkedlist(self.first.data)
        cur_node = self.first.next
        while cur_node is not None:
            list_copy.append(cur_node)
            cur_node = cur_node.next
        list_copy.append(value)
        return list_copy

            
            
        
        
        
        
        
        
a = Linkedlist(0)
a.append(1)
a.append(2)
a.append(3)
a.append(4)
#print a[0]
#print len(a)
#print str(a)
#print repr(a)
#for n in a:
    #print n
a = a + 6
print a

#n = Node(10)
#print n
#print str(n)
#print repr(n)
