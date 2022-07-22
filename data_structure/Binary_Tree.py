# TreeNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
root.left = n1
root.right = n2

# trversal the tree, inorder
def traversal_tree(root):
    if root:
        traversal_tree(root.left)
        print(root.val)
        traversal_tree(root.right)
traversal_tree(root)
