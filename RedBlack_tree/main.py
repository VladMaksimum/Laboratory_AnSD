from RedBlackTree import RedBlackTree

tree = RedBlackTree()

q_nums = int(input("Input quantity of numbers: "))
for _ in range(q_nums):
    tree.add(int(input()))
print(tree._head)

tree.delete(int(input("Remove element: ")))

print(tree._head)