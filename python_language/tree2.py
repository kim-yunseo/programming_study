class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=TreeNode(10)
root.left=TreeNode(20)
root.right=TreeNode(30)

print("루트",root.data)
print("왼쪽 자식",root.left.data)
print("오른쪽 자식",root.right.data)

class TreeNode2:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=TreeNode(10)
root.left=TreeNode(20)
root.right=TreeNode(30)
root.left.left=TreeNode(40)
root.left.right=TreeNode(50)
root.right.left=TreeNode(60)
root.right.right=TreeNode(70)

print("-----------------------------------------------------------")
print("루트",root.data)
print("왼쪽 자식",root.left.data)
print("오른쪽 자식",root.right.data)
print("왼쪽-왼쪽 자식",root.left.left.data)
print("왼쪽-오른쪽 자식",root.left.right.data)
print("오른쪽-왼쪽 자식",root.right.left.data)
print("오른쪽-오른쪽 자식",root.right.right.data)

def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)
print("전위순회")
preorder(root)

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)
print("\n중위순회")
inorder(root)

def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")
print("\n후위순회")
postorder(root)