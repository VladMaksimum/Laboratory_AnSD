from BinaryTree import BinaryTree


def forawrd_passing(tree):
    if tree.value != None:
        print(tree.value, end=" ")
    
    if tree.left != None:
        forawrd_passing(tree.left)
    if tree.right != None:
        forawrd_passing(tree.right)

def central_passing(tree):
    if tree.left != None:
        central_passing(tree.left)

    if tree.value != None:
        print(tree.value, end=" ")

    if tree.right != None:
        central_passing(tree.right)

def reverse_passing(tree):
    if tree.left != None:
        reverse_passing(tree.left)

    if tree.right != None:
        reverse_passing(tree.right)

    if tree.value != None:
        print(tree.value, end=" ")


if __name__ == "__main__":
    tree = BinaryTree('8 (3 (1, 6 (4,7)), 10 (, 14 (13,)))')

    print("Прямой оюход бинарного дерева:")
    forawrd_passing(tree.root)

    print('\n', "Центральный оюход бинарного дерева:")
    central_passing(tree.root)

    print('\n', "Концевой оюход бинарного дерева:")
    reverse_passing(tree.root)
    

