from B_Tree import B_Tree

tree = B_Tree()

q_nums = int(input("Input quantity of numbers: "))
for _ in range(q_nums):
    tree.add(int(input()))
print(tree._head)