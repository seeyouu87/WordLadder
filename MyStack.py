#Name:Wai Jia Hao
#Matriculation No.: 16SIS064D
#Subject: Lab 1 Submission

class MyStack:
    def __init__(self):
        self._data = []
        self._top = -1

    def push(self, value):
        self._data.append(value)
        self._top += 1

    def pop(self):
        return self._data.pop()

    def peek(self):
        #---------------Enter your source code here----------------#
        #Return the value of the element at the top of the stack without removing it from the stack
        return self._data[self._top]
        #pass

    def peekAt(self,i):
        #---------------Enter your source code here----------------#
        #Return the value of the element at index i without removing it from the stack
        return self._data[i]
        #pass

    def size(self):
        #---------------Enter your source code here----------------#
        #Return the number of elements in the stack
        return len(self._data)
        #pass

    def copyFrom(self, aStack):
        #---------------Enter your source code here----------------#
        #Copy all the elements from the input stack aStack to this stack
        for i in range(len(aStack._data)):
            item = aStack.peekAt(i)
            self.push(item)
        #pass

    def toString(self):
        #---------------Enter your source code here----------------#
        #Return a string representing the content of this stack
        string = ""
        if MyStack.size(self) > 0:
            for i in range(0,MyStack.size(self)):
                string += str(self._data[i]) + " "
            return string
        else:
            return ""
        #pass
