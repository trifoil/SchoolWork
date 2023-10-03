class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def Prefixe(root):
    if root:
        print(root.value)
        Prefixe(root.left)
        Prefixe(root.right)

def Postfixe(root):
    if(root):
        Postfixe(root.left)
        Postfixe(root.right)
        print(root.value)

def Infixe(root):
    if(root):
        Infixe(root.left)
        print(root.value)
        Infixe(root.right)


root = Node("A")
root.left = Node("B")
root.left.left = Node("F")
root.left.right = Node("C")
root.left.left.right = Node("G")
root.left.left.right.left = Node("L")
root.left.left.right.left.right = Node("M")
root.left.left.right.right = Node("H")
root.left.right.right = Node("D")
root.left.right.right.left = Node("I")
root.left.right.right.right = Node("E")
root.left.right.right.right.left = Node("J")
root.left.right.right.right.left.right = Node("K")

print("Préfixe")
Prefixe(root)

print("Postfixe")
Postfixe(root)

print("Infixe")
Infixe(root)
