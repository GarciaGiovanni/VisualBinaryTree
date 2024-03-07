from GameObject import GameObject
from dataclasses import dataclass
from GameObject import GameObject
from dataclasses import dataclass

@dataclass
class Node(GameObject):
    value: int
    left: 'Node' = None
    right: 'Node' = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_recursive(node.right, value)

    def print_tree(self):
        self._print_recursive(self.root)


    def _print_recursive(self, node):
        stack = []
        current = node

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
                print("Left")
            elif stack:
                current = stack.pop()
                print(current.value)
                current = current.right
                print("Right")
            else:
                break

    