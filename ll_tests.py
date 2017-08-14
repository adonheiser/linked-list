import unittest, random, sys
import ll   # this is the class to be tested

class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self._initSize = 10
        self._pre = 'foo'
        random.seed(None)
        self._llist = ll.UnorderedList()
        for x in range(self._initSize):
            self._llist.add(self._pre + str(x))

    def tearDown(self):
        del self._llist

    # test size
    def testSize(self):
        print('test size()')
        self.assertEqual(self._llist.size(), self._initSize)

    def testClear(self):
        print("testClear()")
        self._llist.clear()
        self.assertEqual( self._llist._index, 0)

    def testAdd(self):
        self._llist.clear()
        self.assertEqual(self._llist.clear(), None)
        for x in range(self._initSize):
            with self.subTest():
                self._llist.add(self._pre + str(x))
                self.assertTrue(self._llist.search(self._pre + str(x)))
        self.assertEqual(self._llist.size(), self._initSize)

    def testIsEmpty(self):
        self._llist.clear()
        self.assertTrue(self._llist.isEmpty())

    def testRemoveStart(self):
        print('test remove() start')
        self.assertEqual(self._llist.size(), self._initSize)
        self.assertEqual(self._llist._index, self._initSize -1)
        self._llist.remove(self._pre +str(0))
        self.assertEqual(self._llist.size(), self._initSize -1)
        self.assertEqual(self._llist._index, self._initSize - 2)

    def testRemoveMiddle(self):
        print('test remove() middle')
        middle = self._initSize // 2
        self.assertEqual(self._llist.size(), self._initSize)
        self.assertEqual(self._llist._index, self._initSize -1)
        self._llist.remove(self._pre +str(middle))
        self.assertEqual(self._llist.size(), self._initSize -1)
        self.assertEqual(self._llist._index, self._initSize - 2)

    def testRemoveEnd(self):
        print('test remove() end')
        self.assertEqual(self._llist.size(), self._initSize)
        self.assertEqual(self._llist._index, self._initSize -1)
        self._llist.remove(self._pre +str(self._initSize -1))
        self.assertEqual(self._llist.size(), self._initSize -1)
        self.assertEqual(self._llist._index, self._initSize - 2)

    def testRemove(self):
        for x in reversed(range(self._llist._index)):
            with self.subTest():
                self.assertTrue(self._llist.search(self._pre + str(x)))
                self._llist.remove(self._pre + str(x))
                self.assertFalse(self._llist.search(self._pre + str(x)))

    def testSearch(self):
        for x in range(self._llist._index):
            with self.subTest():
                self.assertTrue(self._llist.search(self._pre + str(x), ))

    # gen a random number
    def testSearchNotFound(self):
        n = random.randint(0, sys.maxsize )
        print ("test search() NotFound "  + str(n))
        self.assertFalse(self._llist.search(self._pre  + str(n)))

    def testGetAtPosFront(self):
        print("testGetAtPosFront()")
        target = 0
        current = self._llist.head
        i = 0
        node = None
        while current != None:
            if i == target:
                node = current
                print(node.getData())
                break
            else:
                current = current.getNext()
                i += 1
        self.assertEqual(node, self._llist.getAtPos(target))

    def testGetAtPosBack(self):
        target = self._llist._index
        current = self._llist.head
        i = 0
        node = None
        while current != None:
            if i == target:
                node = current
                print(node.getData())
                break
            else:
                current = current.getNext()
                i += 1
        self.assertEqual(node, self._llist.getAtPos(target))

    def testGetAtPosNotExist(self):
        target = self._llist._index + 1
        with  self.assertRaises(ValueError):
            self._llist.getAtPos(target)

    def testInsert100(self):
        n = 100
        for x in range(n):
            self._llist.insert(str, 0)
        self.assertEqual(self._llist.size(), self._initSize + n)
        self.assertEqual(self._llist._index, self._initSize + n - 1)

    def testPop(self):
        print("testPop()")
        target = self._llist._index
        current = self._llist.head
        i = 0
        node = None
        while current != None:
            if i == target:
                node = current
                break
            else:
                current = current.getNext()
                i += 1
        self.assertEqual(node, self._llist.pop())
        self.assertEqual(self._llist._index, self._initSize - 2)
        self.assertFalse(self._llist.search(node))

    def testIndexFront(self):
        print("test indexFront()")
        target = self._pre +  str(self._llist._index)
        self.assertEqual(0, self._llist.index(target))

    def testIndexBack(self):
        print("test indexBack()")
        target = self._pre + "0"
        self.assertEqual(self._llist._index, self._llist.index(target))

    def testIndexLoop(self):
        for x in range(self._initSize):
            target = self._pre + str(x)
            with self.subTest():
                self.assertEqual(self._llist._index -x, self._llist.index(target))

    # make anad return a refrence list and rotate it by shift
    def rotateReferenceList(self, shift, left = None):
        #print(shift)
        newList = list()
        # make a list
        for x in reversed(range(self._initSize)):
            newList.append(self._pre + str(x))
        if left:
            pre = newList[shift : len(newList)]
            post = newList[0 : shift]
        else: # right
            pre = newList[len(newList) - shift : len(newList)]
            post = newList[0 : len(newList) - shift]
        return pre + post

    # helper for replacing hte _llist with a fresh one
    def refreshTheList(self):
        self._llist.clear()
        for x in range(self._initSize):
            self._llist.add(self._pre + str(x))

    # check rotated list against against a copy with the same shift
    def testRotateRight(self):
        for shift in range(self._llist._index):
            llist = self.rotateReferenceList(shift) # generate a rotated reference list for compare
            i = 0
            self.refreshTheList()                   # make a new list so the shift doesnt cumulatively drift
            self._llist.rotate(shift)               # rotate this list
            current = self._llist.head
            while current != None:
                with self.subTest():                # compare ref and self
                    self.assertEqual(current.getData(), llist[i])
                i +=1
                current = current.getNext()

    #check rotated list against against a copy with the same shift
    def testRotateLeft(self):
        for shift in range(self._llist._index):
            llist = self.rotateReferenceList(shift, 1) # generate a rotated reference list for compare
            i = 0
            self.refreshTheList()                   # make a new list so the shift doesnt cumulatively drift
            self._llist.rotate(-shift)               # rotate this list
            current = self._llist.head
            while current != None:
                print(current.getData())
                current = current.getNext()
            current = self._llist.head
            while current != None:
                with self.subTest():                # compare ref and self
                    self.assertEqual(current.getData(), llist[i])
                i +=1
                current = current.getNext()

    def testReverse(self):
        self._llist.reverse()
        current = self._llist.head
        while current != None:
            print("---- " + current.getData())
            current = current.getNext()
        current = self._llist.head
        for x in range(self._llist._index):
            with self.subTest():
                self.assertEqual(self._pre + str(x), current.getData())
                current = current.getNext()
        self.assertNotEqual(0, self._llist._index)

if __name__ == '__main__':
    unittest.main()
