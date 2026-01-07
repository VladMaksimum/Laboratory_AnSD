from AVLTree import AVL_Tree

tree = AVL_Tree()

q_nums = int(input("Input quantity of numbers: "))
for _ in range(q_nums):
    tree.add(int(input()))


print(tree._head)
tree.delete(int(input("Remove key: ")))
print(tree._head)