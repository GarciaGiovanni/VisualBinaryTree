from GameObject import GameObject
from dataclasses import dataclass

@dataclass
class Node(GameObject):
    def __init__(self, data: int, x: int, y: int):
        super().__init__(x, y, 35, 35, (255, 255, 255), True)
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data: int):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data, 100, 100)
                    print("LEFT")
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data, 100, 100)
                    print("RIGHT")
                else:
                    self.right.insert(data)
        else:
            print("Hit")
            self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
            print( self.data),
        if self.right:
            self.right.PrintTree()
            print( self.data),
        