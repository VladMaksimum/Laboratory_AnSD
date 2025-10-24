class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, tree: str) -> None:
        self.root = BinaryTree.create_node(tree)

    @classmethod
    def is_elem_tree(self, subtree):
        return subtree.count("(") == 1

    @classmethod
    def find_split_index(self, tree):
        stack = []
        
        for index in range(len(tree)):
            if tree[index] == "," and len(stack) == 0:
                return index
            
            if tree[index] == "(":
                stack.append("(")
            if tree[index] == ")":
                stack.pop(-1)
    



    @classmethod
    def create_node(self, subtree):
        print(subtree)
        if subtree == '':
            return None

        if BinaryTree.is_elem_tree(subtree):
            left, right = subtree[subtree.index("(") + 1: -1 :].split(",")
            if left == '':
                root = Node(int(subtree[0]), None, int(right))
            elif right == '':
                root = Node(int(subtree[0]), int(left), None)
            else:
                root = Node(int(subtree[0]), int(left), int(right))
            return root
        
        else:
            root = Node(int(subtree[0]), None, None)

            kids = subtree[subtree.index("(") + 1 : -1 :]
            split_index = BinaryTree.find_split_index(kids)

            left_side = kids[:split_index:]
            right_side = kids[(split_index+2)::]

            if left_side.isdigit():
                root.left = int(left_side)
            else:
                root.left = BinaryTree.create_node(left_side)
            if right_side.isdigit():
                root.right = int(right_side)
            else:
                root.right = BinaryTree.create_node(right_side)

            return root
                

    

        

if __name__ == "__main__":
    tree = BinaryTree('8 (3 (1, 6 (4,7)), 10 (, 14(13,)))')