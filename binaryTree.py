class Node():
    def __init__(self, content):
        self._content = content

    def getContent(self):
        return self._content

    def addLeft(self, leftNode):
        self._left = leftNode

    def getLeft(self):
        try:
            return self._left
        except AttributeError:
            return None

    def addRight(self, rightNode):
        self._right = rightNode

    def getRight(self):
        try:
            return self._right
        except AttributeError:
            return None


class Tree():
    def __init__(self, content):
        self._root = Node(content)

    def add(self, content):
        self._add(content, self._root)

    def _add(self, content, node):
        if node.getContent() < content:
            if node.getRight() is None:
                node.addRight(Node(content))
            else:
                self._add(content, node.getRight())
        else:
            if node.getLeft() is None:
                node.addLeft((Node(content)))
            else:
                self._add(content, node.getLeft())

    def getSorted(self):
        self._getSorted(self._root)

    def _getSorted(self, node):
        if node.getLeft() is not None:
            self._getSorted(node.getLeft())
        print(node.getContent(), end=" ")
        if node.getRight() is not None:
            self._getSorted(node.getRight())

    def printTree(self):
        node = self._root
        print(node.getContent())
        if node.getLeft() is not None:
            self._printTree(node.getLeft(), 1, '[L]')
        if node.getRight() is not None:
            self._printTree(node.getRight(), 1, '[R]')

    def _printTree(self, node, depth, position):
        for i in range(depth):
            print('-', end='')
        print(node.getContent(), position)
        if node.getLeft() is not None:
            self._printTree(node.getLeft(), depth + 1, '[L]')
        if node.getRight() is not None:
            self._printTree(node.getRight(), depth + 1, '[R]')

    def maxDepth(self):
        return self._maxDepth(self._root)

    def _maxDepth(self, node):
        if node.getLeft() is not None:
            leftDepth = self._maxDepth(node.getLeft())
        else:
            leftDepth = 0
        if node.getRight() is not None:
            rightDepth = self._maxDepth(node.getRight())
        else:
            rightDepth = 0
        if leftDepth > rightDepth:
            return leftDepth + 1
        else:
            return rightDepth + 1


tree = Tree(8)
tree.add(2)
tree.add(7)
tree.add(4)
tree.add(5)
tree.add(9)
tree.add(3)
tree.add(1)
tree.add(16)
tree.getSorted()
tree.printTree()
print(tree.maxDepth())