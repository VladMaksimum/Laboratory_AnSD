from BinarySearchTree import BinarySearchTree

tree = BinarySearchTree(input("Input binary search tree: \n"))

while True:
    print("Choose operation:\n" \
            "1. Search value\n" \
            "2. Insert value\n" \
            "3. Remove value\n" \
            "4. Exit")

    choice = int(input("Your choice: "))

    match choice:
        case 1:
            value = int(input("Input value: \n"))
            search_node = tree.search(value, tree.root)
            left, right = search_node.left, search_node.right

            if search_node.left != None:
                left = search_node.left.value
            if search_node.right != None:
                right = search_node.right.value

            print(f'Node with value {value} has {left} left leaf and {right} right leaf')
        
        case 2:
            value = int(input("Input value: \n"))
            tree.insert(value, tree.root)
            print(f"Value {value} was inserted")
        
        case 3:
            value = int(input("Input value: \n"))
            tree.remove(value, tree.root, tree.root)
            print(f"Value {value} was removed")

        case 4:
            print("Final tree", str(tree), sep="\n")
            break