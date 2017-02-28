"""
用单链表实现堆栈 先进后出
Introduction: Implement a linked list as a class, and use it as a stack (LIFO)
__author__ = v1siuol
__date__ = 2017.02.28
* Test cases provide at the bottom
"""


class stackUsingLinkedList:
    class Node:  # an element of data structure containing value and a pointer to next element
        __slots__ = "_value", "_next"  # save list memory

        def __init__(self, v, n):  # constructor for a Node
            self._value = v
            self._next = n

    def __init__(self):
        """
        constructor for an empty linkedlist
        """
        self._head = None
        self._size = 0

    def push(self, value):
        """
        add a value in constant time
        """
        self._head = self.Node(value, self._head)
        self._size += 1

    def pop(self):
        """
        retrieve last insertion in constant time
        """
        if not self.is_empty():
            valuePopOut = self._head._value
            self._head._value = None  # clear up the value
            self._head = self._head._next
            self._size -= 1
            return valuePopOut
        else:  # pop when linkedlist is empty
            raise IndexError

    def __iter__(self):
        """
        iterator function with yield statement
        """
        currentPointer = self._head
        while currentPointer is not None:
            yield str(currentPointer._value)
            currentPointer = currentPointer._next
        raise StopIteration

    def top(self):
        """
        return last insertion, without removal
        """
        if self.is_empty():
            raise AttributeError
        return self._head._value

    def is_empty(self):
        """
        identify whether list is empty
        """
        return self._size == 0

    def __len__(self):
        """
        return number of elements in list
        """
        return self._size

    def __str__(self):
        """
        represent entire list as a string
        """
        return " ".join(list(iter(self)))

# ------------------test case---------------------
if __name__ == "__main__":
    if True:
        testLst = stackUsingLinkedList()

        print("Linkedlist displays:", testLst)
        print("The list is empty:", testLst.is_empty())
        print("The length (size) of linkedlist:", testLst.__len__())

        print()

        testLst.push(9)
        testLst.push(6)
        # 6 9
        print("The top of the linkedlist:", testLst.top())
        print("Linkedlist displays:", testLst)
        print("The list is empty:", testLst.is_empty())
        print("The length (size) of linkedlist:", testLst.__len__())

        print()

        print("The value poped out:", testLst.pop())
        # 9
        print("The top of the linkedlist:", testLst.top())
        print("Linkedlist displays:", testLst)
        print("The list is empty:", testLst.is_empty())
        print("The length (size) of linkedlist:", testLst.__len__())
