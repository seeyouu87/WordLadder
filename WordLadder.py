from MyQueue import MyQueue
from MyStack import MyStack

dictionary = []
def readFromDictionary(fileName):
    global dictionary

    f = open(fileName, "r")
    for line in f:
        line = line.replace("\n", "", )
        line = line.lower()
        dictionary.append(line)
    dictionary = list(set(dictionary))
    dictionary.sort()
    f.close()

def findWords(firstWord, lastWord):
    global dictionary

    #---------------Enter your source code here----------------#
    #Print a shortest word ladder for the firstWord and lastWord and return 1 if such a ladder can be found
    #Return -1 if there exists no word ladder for the firstWord and lastWord

    queue = MyQueue()#declare a new queue
    existingwordlist = []#to keep track of used words
    firtFound = False
    lastFound = False
    # if both words exist in dictionary, then posible to have ladder
    for i in range(len(dictionary)):
        if firstWord == dictionary[i]:
            firstFound = True
        if lastWord == dictionary[i]:
            lastFound = True
    if lastFound and firstFound:
        if firstWord == lastWord:
            print [firstWord]
            return 1
        elif len(firstWord) != len(lastWord):
            return -1
        else:
            existingwordlist.append(firstWord)
            refStack = MyStack()
            refStack.push(firstWord)
            whileCounter = 0
            curword = firstWord
            while lastWord not in existingwordlist and whileCounter<100:
                queuedCount = 0
                for i in range(len(dictionary)):#go through dictionary list
                    if len(curword)==len(dictionary[i]):#if word length matches                        
                        counter = 0
                        for k in range(len(curword)):
                            a=dictionary[i]
                            if a[k]==curword[k]:#go through each character and match if they are the same
                              counter +=1
                        
                        if counter == (len(dictionary[i])-1) and dictionary[i] not in existingwordlist:#do checking if only one letter different
                            existingwordlist.append(dictionary[i])
                            curStack = MyStack()
                            curStack.copyFrom(refStack)
                            curStack.push(dictionary[i])
                            queue.enqueue(curStack)#enqueue the stack into the queue
                            queuedCount +=1
                
                if queuedCount ==0 and queue.size()>0:
                    refStack = MyStack()
                    firstStack = queue.dequeue()
                    refStack.copyFrom(firstStack)
                    curword = firstStack.pop()
                whileCounter +=1 # can't think of any smarter way to prevent infinite loop
            outputlist=[]#declare a list to store the word ladder
            if lastWord in existingwordlist:
                for k in range(queue.size()):
                    outputlist.append(queue.dequeue().toString())
                print(outputlist[-1])
                return 1
            else:
                return -1
    else:
        return -1

def test(firstWord, lastWord):
    result = findWords(firstWord, lastWord)
    if result == -1:
        print("No Ladder for ", firstWord, "->", lastWord)
    else:
        print result


readFromDictionary('dictionary.txt')
# findWords('smart', 'scars')
#No solution test cases
test('sail', 'ruin')