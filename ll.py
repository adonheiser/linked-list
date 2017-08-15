#!/usr/bin/python3
import random, sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data
        #return "foo"

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:

    def __init__(self):
        self.head = None
        self._index = None

    def isEmpty(self):
        return self._index == 0

    def clear(self):
        self.head = None
        self._index = 0

    def add(self, temp):
        temp = Node(temp)
        temp.setNext(self.head)
        self.head = temp
        if not self._index:
            self._index = 0
        self._index += 1

    def size(self):
        current = self.head
        sz = 0
        while current != None:
            sz += 1
            current = current.getNext()
        return sz

    def remove(self, needle):
        prev = None
        current = self.head
        found = False

        while not found:
            if current.getData() == needle:
                found = True
            else:
                prev = current
                current = current.getNext()
        if prev == None:    # head
            self.head = current.getNext()
        else:
            prev.setNext(current.getNext()) # dont modify to new head just skip over
        self._index -= 1

    def search(self, needle):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == needle:
                found = True
            else:
                current = current.getNext()
        return found

    # return node at position
    def getAtPos (self, pos):
        current = self.head
        i = 0
        if pos == None or pos < 0 or pos > self._index:
            raise ValueError
        while current != None and i <= self._index:
            if i == pos:
                return current
            else:
                current = current.getNext()
                i += 1
        return None


    def index(self, needle):
        current = self.head
        i = 0
        found = False
        while current != None and not found and i <= self._index:
            print(" ||||| " + current.getData())
            print(self._index)
            if current.getData() == needle:
                found = True
            else:
                current = current.getNext()
                i += 1
        return i if found else None

    """ insert and item"""
    def insert(self, _item, pos):
        i = 0
        item = Node(_item)
        prev = None
        current = self.head
        while current != None or i <= self._index:
            if i == pos:
                if pos == 0:
                    self.head = item
                    item.setNext(current)
                    self._index += 1
                    return 0
                else:
                    prev.setNext(item)
                    item.setNext(current)
                    self._index += 1
                    return 0
            else:
                prev = current
                current = current.getNext()
                i += 1
        return None

    # return rightmost node
    def pop(self):
        i = 0
        prev = None
        current = self.head
        while current != None or i < self._index:
            if i == self._index:
                prev.setNext(None)
                self._index -= 1
                return current
            else:
                prev = current
                current = current.getNext()
                i += 1
        return None

    # pos rotate right
    # neg rotate left
    # 0 do nothing
    def rotate(self, rotation):
        if rotation == 0 or rotation == self._index + 1:
            return 0

        if rotation > self._index:
            raise ValueError

        print("rotation " + str(rotation))

        ''' first go through and set the last node to head '''
        i = 0
        prev = None
        current = self.head
        while current != None and i <= self._index:
            if i == self._index:
                current.setNext(self.head)
                break
            current = current.getNext()
            i += 1
        ''' now go and set nodes for the rotation'''

        current = self.head
        j = 0
        while current != None and j <= self._index: # now swap nodes
            if rotation > 0:  # rotate right case
                if j == self._index - rotation:
                    if rotation == 1:
                        current.setNext(self.head) # set to existing head
                    self.head = current             # current is the head
                    prev.setNext(None)              # previous is now the end
                    break                           # all done setting new head and tail so break
                else:
                   prev = current
                   current = current.getNext()
                   j += 1
            else:
                if j == abs(rotation):  # get the absolute val of rotation since left is negative
                    # if rotation == 1:
                    #    self.head = current # set to existing head
                    self.head = current  # current is the head
                    prev.setNext(None)  # previous is now the end
                    break  # all done setting new head and tail so break
                else:
                    prev = current
                    current = current.getNext()
                    j += 1


    # make a temp  list, delete current and copy temp in to new
    def reverse(self):
        temp = list()
        current = self.head
        while current != None:
            temp.append(current.getData())
            current = current.getNext()
        self.clear()
        for l in temp:
            self.add(l)

