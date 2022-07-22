# we can use list as stack
stack = []
# push
stack.append(1)
stack.append(2)
stack.append(3)
# or stack.extend([1,2,3])
print("stack = ", stack)

# pop the last push item
stack.pop()
print("stack = ", stack)
