BLACK = 'BLACK'
RED = 'RED'

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    def get(self):
        return self.key
    def set(self, key):
        self.key = key
    def getChildren(self):
        children = []
        if (self.left != None):
            children.append(self.left)
        if (self.right != None):
            children.append(self.right)
        return children

class ABR:
    def __init__(self):
        self.root = None
    def setRoot(self, key):
        self.root = Node(key)
    def insert(self, key):
        if (self.root is None):
            self.setRoot(key)
        else:
            self.insertNode(self.root, key)

    def insertNode(self, currentNode, key):
        if (key <= currentNode.key):
            if (currentNode.left):
                self.insertNode(currentNode.left, key)
            else:
                currentNode.left = Node(key)
        elif (key > currentNode.key):
            if (currentNode.right):
                self.insertNode(currentNode.right, key)
            else:
                currentNode.right = Node(key)

    def find(self, key):
        return self.findNode(self.root, key)

    def findNode(self, currentNode, key):
        if (currentNode is None):
            return False
        elif (key == currentNode.key):
            return True
        elif (key < currentNode.key):
            return self.findNode(currentNode.left, key)
        else:
            return self.findNode(currentNode.right, key)

    def findMax(self, currentNode):
        if (currentNode.right == None):
            return currentNode.key
        else:
            return self.findMax(currentNode.right)

    def inorder(self):
        def _inorder(v):
            if (v is None):
                return
            if (v.left is not None):
                _inorder(v.left)
            print(v.key)
            if (v.right is not None):
                _inorder(v.right)
        _inorder(self.root)

class NodeRN(Node):
    def __init__(self, key):
        super().__init__(key)
        #self.key = key
        #self.left = None
        #self.right = None
        self.color = None
        self.p = None

    def getP(self):
        return self.p
    def setP(self, parent):
        self.p = parent
    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color

class RN:
    def __init__(self):
        self.root = None
    def setRoot(self, node):
        self.root = node
        #self.root = NodeRN(key)
        self.root.color = BLACK


    def insert(self, key):
        if (self.root is None):
            node = NodeRN(key)
            self.setRoot(node)
        else:
            self.insertNode(self.root, key)

    def insertNode(self, currentNode, key):
        if ( currentNode is not None and key <= currentNode.key):
            if (currentNode.left):
                self.insertNode(currentNode.left, key)
            else:
                currentNode.left = NodeRN(key)
                currentNode.left.setColor(RED)
                currentNode.left.setP(currentNode)
                self.insertFixup(currentNode.left)
        elif (currentNode is not None and key > currentNode.key):
            if (currentNode.right):
                self.insertNode(currentNode.right, key)
            else:
                currentNode.right = NodeRN(key)
                currentNode.right.setColor(RED)
                currentNode.right.setP(currentNode)
                self.insertFixup(currentNode.right)

    def insertFixup(self, currentNode):
        while currentNode.p is not None and currentNode.p.color == RED:
            if currentNode.p == currentNode.p.p.left :
                uncle = currentNode.p.p.right
                #if uncle is not None:
                if uncle is not None and uncle.color==RED:
                    currentNode.p.setColor(BLACK)
                    uncle.setColor(BLACK)
                    currentNode.p.p.setColor(RED)
                    currentNode = currentNode.p.p
                elif currentNode == currentNode.p.right:
                    currentNode = currentNode.p
                    self.leftRotate(currentNode)
                if currentNode.p is not None:
                    currentNode.p.setColor(BLACK)
                    if currentNode.p.p is not None:
                        currentNode.p.p.setColor(RED)
                        self.rightRotate(currentNode.p.p)
            else:
                uncle = currentNode.p.p.left
                #if uncle is not None:
                if uncle is not None and uncle.color == RED:
                    currentNode.p.setColor(BLACK)
                    uncle.setColor(BLACK)
                    currentNode.p.p.setColor(RED)
                    currentNode = currentNode.p.p
                elif currentNode == currentNode.p.left:
                    currentNode = currentNode.p
                    self.rightRotate(currentNode)
                if currentNode.p is not None:
                    currentNode.p.setColor(BLACK)
                    if currentNode.p.p is not None:
                        currentNode.p.p.setColor(RED)
                        self.leftRotate(currentNode.p.p)
        self.root.setColor(BLACK)

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.p = x
        y.p = x.p
        if x.p is None:
            self.setRoot(y)
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.p = x
        y.p = x.p
        if x.p is None:
            self.setRoot(y)
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y

    def findMax(self, currentNode):
        if (currentNode.right == None):
            return currentNode.key
        else:
            return self.findMax(currentNode.right)

    def inorder(self):
        def _inorder(v):
            if (v is None):
                return
            if (v.left is not None):
                _inorder(v.left)
            print("%d %s" % (v.key, v.getColor()))
            if (v.right is not None):
                _inorder(v.right)
        _inorder(self.root)

    def find(self, key):
        return self.findNode(self.root, key)

    def findNode(self, currentNode, key):
        if (currentNode is None):
            return False
        elif (key == currentNode.key):
            return True
        elif (key < currentNode.key):
            return self.findNode(currentNode.left, key)
        else:
            return self.findNode(currentNode.right, key)





