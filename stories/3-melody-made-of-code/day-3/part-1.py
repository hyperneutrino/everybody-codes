import re

class Node:
    def __init__(self, id, plug, left, right):
        self.id = id
        self.plugType = plug
        self.leftType = left
        self.rightType = right
        self.leftNode = None
        self.rightNode = None

    def insert(self, node):
        if self.leftNode is None and self.leftType == node.plugType:
            self.leftNode = node
            return True

        if self.leftNode is not None:
            if self.leftNode.insert(node):
                return True

        if self.rightNode is None and self.rightType == node.plugType:
            self.rightNode = node
            return True

        if self.rightNode is not None:
            if self.rightNode.insert(node):
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

    if not root.insert(node): raise RuntimeError("!!")

array = root.traverse()
print(sum(index * value for index, value in enumerate(array, start=1)))