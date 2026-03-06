import re

def match(socket, plug):
    socketColor, socketShape = socket.split()
    plugColor, plugShape = plug.split()

    colorMatch = socketColor == plugColor
    shapeMatch = socketShape == plugShape

    if colorMatch and shapeMatch:
        return "strong"
    if colorMatch or shapeMatch:
        return "weak"

    return False

class Pointer:
    def __init__(self, value):
        self.value = value

class Node:
    def __init__(self, id, plug, left, right):
        self.id = id
        self.plugType = plug
        self.leftType = left
        self.rightType = right
        self.leftNode = None
        self.rightNode = None

    def insert(self, node):
        if self.leftNode is None and match(self.leftType, node.value.plugType):
            self.leftNode = node.value
            return True

        if self.leftNode is not None:
            if match(self.leftType, self.leftNode.plugType) == "weak" and match(self.leftType, node.value.plugType) == "strong":
                self.leftNode, node.value = node.value, self.leftNode
            elif self.leftNode.insert(node):
                return True

        if self.rightNode is None and match(self.rightType, node.value.plugType):
            self.rightNode = node.value
            return True

        if self.rightNode is not None:
            if match(self.rightType, self.rightNode.plugType) == "weak" and match(self.rightType, node.value.plugType) == "strong":
                self.rightNode, node.value = node.value, self.rightNode
            elif self.rightNode.insert(node):
                return True

        return False

    def traverse(self):
        output = []
        if self.leftNode: output += self.leftNode.traverse()
        output.append(self.id)
        if self.rightNode: output += self.rightNode.traverse()
        return output

root = None

for line in open(0):
    id, plug, left, right = re.match(r"id=(\d+), plug=(.+?), leftSocket=(.+?), rightSocket=(.+?), data=.+", line).groups()
    id = int(id)
    node = Node(id, plug, left, right)

    if root is None:
        root = node
        continue

    ptr = Pointer(node)

    while not root.insert(ptr): pass

array = root.traverse()
print(sum(index * value for index, value in enumerate(array, start=1)))