#Name:Wai Jia Hao
#Matriculation No.: 16SIS064D
#Subject: Lab 1 Submission

import collections

class MyQueue:
    def __init__(self):
        self._data = collections.deque([])

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        return self._data.popleft()

    def isEmpty(self):
        #---------------Enter your source code here----------------#
        #Return True if the queue is empty, False otherwise
        if len(self._data)==0:
            return True
        else:
            return False
        #pass

    def size(self):
        #---------------Enter your source code here----------------#
        #return the number of elements in the queue
        return len(self._data)
        #pass

