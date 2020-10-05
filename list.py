class Node():
    def __init__(self, content):
        self.content = content

    @classmethod
    def createAndSetPrev(cls, content, prev):
        node = cls(content)
        prev.setNext(node)
        return node

    def setNext(self, nextNode):
        self.nextNode = nextNode

    def getNext(self):
        try:
            return self.nextNode
        except AttributeError:
            return self.nextNode

    def getContent(self):
        return self.content


class List():
    def __init__(self, rootNode):
        self.root = rootNode
        self.tail = rootNode

    def add(self, content):
        newNode = Node.createAndSetPrev(content, self.tail)
        self.tail = newNode

    def addLeft(self, content):
        newNode = Node(content)
        newNode.setNext(self.root)
        self.root = newNode

    def printAll(self):
        currentNode = self.root
        print('[', end='')
        while (currentNode != self.tail):
            print(currentNode.getContent(), end=",")
            currentNode = currentNode.getNext()
        print(currentNode.getContent(), end="]")
        print()

    def get(self, index):
        currentNode = self.root
        for i in range(index):
            currentNode = currentNode.getNext()
        return currentNode.getContent

    def length(self):
        currentNode = self.root
        len = 1
        while (currentNode != self.tail):
            currentNode = currentNode.getNext()
            len += 1
        return len

    def insert(self, content, index):
        currentNode = self.root
        if index == 0:
            self.addLeft(content)
        else:
            for i in range(index - 1):
                currentNode = currentNode.getNext()
            if currentNode == self.tail:
                self.add(content)
            else:
                nextNode = currentNode.getNext()
                newNode = Node.createAndSetPrev(content, currentNode)
                newNode.setNext(nextNode)


list = List(Node(5))
list.add(1)
list.add(3)
list.add(4)
list.addLeft(2)
print(list.length())
list.printAll()
list.insert(7, 2)
list.printAll()
