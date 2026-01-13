from BinaryTree import BinaryTree

tree = BinaryTree('8 (3 (1, 6 (4,7)), 10 (, 14 (13,)))')
result = ''
stack = [tree.root]

while len(stack) != 0:
    current = stack[-1]
    stack.pop(-1)

    while current != None:
        print(current.value, end=" ")

        if current.left != current:
            stack.append(current.left)
        
        current = current.right
