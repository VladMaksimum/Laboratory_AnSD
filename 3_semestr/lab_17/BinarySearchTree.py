class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self):
        if self.left == None and self.right == None:
            return str(self.value)
        if self.left == None and self.right != None:
            return str(self.value) + " (, " + str(self.right) + ")"
        if self.left != None and self.right == None:
            return str(self.value) + " (" + str(self.left) + ",)"
        
        return str(self.value) + " (" + str(self.left) + ", " + str(self.right) + ")"

class BinarySearchTree:
    def __init__(self, tree: str) -> None:
            self.root = BinarySearchTree.create_node(tree)

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
        #print(subtree)
        if subtree == '':
            return None

        if BinarySearchTree.is_elem_tree(subtree):
            left, right = subtree[subtree.index("(") + 1: -1 :].split(",")
            if left == '':
                root = Node(int(subtree[: subtree.index("("):]), None, Node(int(right), None, None))
                if root.value > root.right.value:
                    raise Exception("The condition of the binary tree is violated. Right side must be not less than root")
            elif right == '':
                root = Node(int(subtree[: subtree.index("("):]), Node(int(left), None, None), None)
                if root.value <= root.left.value:
                    raise Exception("The condition of the binary tree is violated. Left side must be less than root")
            else:
                root = Node(int(subtree[: subtree.index("("):]), Node(int(left), None, None), Node(int(right), None, None))
                if root.value > root.right.value or root.value <= root.left.value:
                    raise Exception("The condition of the binary tree is violated. Left side must be less than root and\
                                                                                    Right side must be not less than root")
            
            return root
        
        else:
            root = Node(int(subtree[: subtree.index("("):]), None, None)

            kids = subtree[subtree.index("(") + 1 : -1 :]
            split_index = BinarySearchTree.find_split_index(kids)

            left_side = kids[:split_index:]
            right_side = kids[(split_index+2)::]
            #print(left_side, "||" , right_side, "here")

            if left_side.isdigit():
                root.left = Node(int(left_side), None, None)
                if root.value <= root.left.value:
                    raise Exception("The condition of the binary tree is violated. Left side must be less than root")
            else:
                root.left = BinarySearchTree.create_node(left_side)
                if root.left != None:
                    if root.value <= root.left.value:
                        raise Exception("The condition of the binary tree is violated. Left side must be less than root")
            
            if right_side.isdigit():
                root.right = Node(int(right_side), None, None)
                if root.value > root.right.value:
                    raise Exception("The condition of the binary tree is violated. Right side must be not less than root")
            else:
                root.right = BinarySearchTree.create_node(right_side)
                if root.right != None:
                    if root.value > root.right.value:
                        raise Exception("The condition of the binary tree is violated. Right side must be not less than root")

            return root
    

    def search(self, value, current) -> Node:
        if value == current.value:
            return current
        
        if current.left != None and value < current.value:
            return self.search(value, current=current.left)
        elif current.right != None and value >= current.value:
            return self.search(value, current=current.right)
        else:
            return Node(None, None, None)
    
    def insert(self, value, current) -> None:
        if current.value == value:
            raise Exception("Value already inserted")
        if current.value > value:
            if current.left == None:
                current.left = Node(value, None, None)
                return
            else:
                return self.insert(value, current.left)
        if current.value <= value:
            if current.right == None:
                current.right = Node(value, None, None)
                return
            else:
                return self.insert(value, current.right)
    

        

    def remove(self, value, parent, current):
        if self.search(value, self.root).value == None:
            raise Exception("No value in tree")

        if current.value == value:

            if current.left == None and current.right == None:
                if parent.left == current:
                    parent.left = None
                    return
                else:
                    parent.right = None
                    return
                
            if current.left == None and current.right != None:
                if parent.left == current:
                    parent.left = current.right
                    return
                else:
                    parent.right = current.right
                    return
                
            if current.left != None and current.right == None:
                if parent.left == current:
                    parent.left = current.left
                    return
                else:
                    parent.right = current.left
                    return
                
            if current.left != None and current.right != None:
                parent_swap = current
                swap_node = current.right
                while swap_node.left != None:
                    parent_swap = swap_node
                    swap_node = swap_node.left
                
                self.remove(swap_node.value, parent_swap, swap_node)
                current.value = swap_node.value
                return
        
        if value < current.value:
            return self.remove(value, parent=current, current=current.left)
        if value >= current.value:
            return self.remove(value, parent=current, current=current.right)
    


    def __str__(self):
        if self.root.left == None and self.root.right == None:
            return str(self.root.value)
        if self.root.left == None and self.root.right != None:
            return str(self.root.value) + " (, " + str(self.root.right) + ")"
        if self.root.left != None and self.root.right == None:
            return str(self.root.value) + " (" + str(self.root.left) + ",)"
        
        return str(self.root.value) + " (" + str(self.root.left) + ", " + str(self.root.right) + ")"
        

            



if __name__ == "__main__":
    tree = BinarySearchTree("8 (3 (1, 6 (4,7)), 10 (, 14(13,)))")
    #print(tree.search(13, tree.root).value)
    #tree.insert(10, tree.root)

    test = 8
    tree.remove(test, tree.root, tree.root)
    print(str(tree))

    




