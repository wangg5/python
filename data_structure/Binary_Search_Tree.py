""" Binary Search Tree

BST: a binary tree, in which:
    * -all values in left are < value
    * -all values in right are > value
    * -left and right are BSTs 

    duplicates not allowed.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

class BST_methods:

    def searchNode(self, root, val):
        if root is None:
            return False
        elif root.val == val:
            return True
        elif root.val > val:
            return self.searchNode(root.left, val)
        elif root.val < val:
            return self.searchNode(root.right, val)
    
    def insertNode(self, root, val):
        if root is None:
            return TreeNode(val)
        elif root.val < val:
            if root.right is None:
                root.right = TreeNode(val)
                root.right.parent = root
            else:
                root.right = self.insertNode(root.right, val)
        elif root.val > val:
            if root.left is None:
                root.left = TreeNode(val)
                root.left.parent = root
            else:
                root.left = self.insertNode(root.left, val)
        return root

    def inorderTraversal(self, root):
        #print("come in inorder traverseal.")
        if root:
            self.inorderTraversal(root.left)
            print(root.val)
            self.inorderTraversal(root.right)
    def minVal(self, root):
        if root.left is None:
            return root.val
        else:
            return self.minVal(root.left)
    def minNode(self, root):
        if root.left is None:
            return root
        else:
            return self.minNode(root.left)
    def deleteNode(self, root, val):
        if root is None:
            return None
        if root.val < val:
            root.right = self.deleteNode(root.right, val)
        if root.val > val:
            root.left = self.deleteNode(root.left, val)
        if root.val == val:

        # case 1: it is a leaf.
        # case 2: it has one child.
            if root.left is None:
                temp = root.right
                if root.parent and temp is not None:
                    if root.val == root.parent.left.val: # root is the left child of his parent
                        root.parent.left = temp
                        temp.parent = root.parent

                    if root.val == root.parent.right.val: # root is the right child of his parent. 
                        root.parent.right = temp
                        temp.parent = root.parent
                root = None
                return temp

            if root.right is None:
                temp = root.left
                if root.parent and temp is not None:
                    if root.val == root.parent.left.val: # root is the left child of his parent
                        root.parent.left = temp
                        temp.parent = root.parent

                    if root.val == root.parent.right.val: # root is the right child of his parent.
                        root.parent.right = temp
                        temp.parent = root.parent
                root = None
                return temp
            
            # case 3: it has two children
            # find the minmum node of right subtree
            temp = self.minNode(root.right)
            root.val = temp.val
            # delete this min node. it is a leaf. or it has a right child.
            root.right = self.deleteNode(root.right, temp.val)
        return root

"""     
                    10
             8             16

         4       9       11    17
      3                           18
"""
"""
root = TreeNode(10)
n1 = TreeNode(8)
n2 = TreeNode(16)
n3 = TreeNode(4)
n4 = TreeNode(9)
n5 = TreeNode(11)
n6 = TreeNode(17)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.left = n5
n2.right = n6
"""
#root = TreeNode(10)
bst = BST_methods()
root = None
root = bst.insertNode(root, 10)

root = bst.insertNode(root, 10)
root = bst.insertNode(root, 8)
root = bst.insertNode(root, 16)
root = bst.insertNode(root, 4)
root = bst.insertNode(root, 9)
root = bst.insertNode(root, 11)
root = bst.insertNode(root, 17)
root = bst.insertNode(root, 18)
root = bst.insertNode(root, 3)

bst.inorderTraversal(root)

print("search 9: ")
print(bst.searchNode(root, 9))
print("search 5: ")
print(bst.searchNode(root,5))


# find the minmum value of the BST.
minValue = bst.minVal(root)
print("minmum value of the tree = ", minValue)

# delete a node
root = bst.deleteNode(root, 10)
bst.inorderTraversal(root)

mn = bst.minNode(root)
while mn:
    print("mn.val = ", mn.val)
    mn = mn.parent







