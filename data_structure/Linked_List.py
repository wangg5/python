# Node objects
#  node
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3


print("node1.val = ", node1.val)
iter = node1
while iter:
    print("val = ", iter.val)
    iter = iter.next
