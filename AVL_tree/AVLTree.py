from typing import Self

class Node:
    def __init__(self, key: int, left: Self | None, right: Self | None, balance: int, parent: Self | None) -> None:
        self.key = key
        self.left = left
        self.right = right
        self.balance = balance
        self.parent = parent
    
    def __str__(self) -> str:
        if self.parent != None:
            return f'({self.key} {self.left} {self.right} parent={self.parent.key} balance={self.balance})'
        
        return f'({self.key} {self.left} {self.right} balance={self.balance})'


class AVL_Tree:
    def __init__(self):
        self._head = None
    
    def add(self, key: int) -> None:
        if self._head == None:
            self._head = Node(key, None, None, 0, None)
            return
        
        current = self._head
        while True:
            if key < current.key:
                if current.left != None:
                    current.balance += 1
                    current = current.left
                else:
                    current.left = Node(key, None, None, 0, current)
                    current.balance += 1
                    break
            else:
                if current.right != None:
                    current.balance -= 1
                    current = current.right
                else:
                    current.right = Node(key, None, None, 0, current)
                    current.balance -= 1
                    break
        #print("before", self._head)
        self._add_fixup(current)
        #print("after", self._head)
        
    def _add_fixup(self, fixup_node: Node) -> None:
        if fixup_node.balance == 0:
            return
        

        if fixup_node.balance == -2:
            if fixup_node.right.balance <= 0:
                fixup_node.balance += (1 - fixup_node.right.balance)
                fixup_node.right.balance += 1

                self.rotate_left(fixup_node, fixup_node.right)
            else:
                if fixup_node.right.left.balance == 1:
                    fixup_node.balance = 0
                    fixup_node.right.balance = -1
                    fixup_node.right.left.balance = 0
                elif fixup_node.right.left.balance == -1:
                    fixup_node.balance = 1
                    fixup_node.right.balance = 0
                    fixup_node.right.left.balance = 0
                else:
                    fixup_node.balance = 0
                    fixup_node.right.balance = 0
                    fixup_node.right.left.balance = 0

                self.rotate_right(fixup_node.right, fixup_node.right.left)
                self.rotate_left(fixup_node, fixup_node.right)

            parent = fixup_node.parent
            while parent != None:
                if parent.balance > 0:
                    parent.balance -= 1
                elif parent.balance < 0:
                    parent.balance += 1
                parent = parent.parent
            
            return

        elif fixup_node.balance == 2:
            if fixup_node.left.balance >= 0:
                fixup_node.balance += (1 - fixup_node.left.balance)
                fixup_node.left.balance += 1

                self.rotate_right(fixup_node, fixup_node.left)
            else:
                if fixup_node.left.right.balance == 1:
                    fixup_node.balance = 0
                    fixup_node.left.balance = -1
                    fixup_node.left.right.balance = 0
                elif fixup_node.left.right.balance == -1:
                    fixup_node.balance = 1
                    fixup_node.left.balance = 0
                    fixup_node.left.right.balance = 0
                else:
                    fixup_node.balance = 0
                    fixup_node.left.balance = 0
                    fixup_node.left.right.balance = 0

                self.rotate_left(fixup_node.left, fixup_node.left.right)
                self.rotate_right(fixup_node, fixup_node.left)
            
            parent = fixup_node.parent
            while parent != None:
                #print(parent, "wtf")
                if parent.balance > 0:
                    parent.balance -= 1
                elif parent.balance < 0:
                    parent.balance += 1
                parent = parent.parent
            
            return

        if fixup_node.parent != None:
            self._add_fixup(fixup_node.parent)
        else:
            return
        


    def rotate_left(self, x: Node, y: Node) -> None:
        x.right = y.left
        y.left = x

        if x.right != None:
            x.right.parent = x

        if x.parent != None:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        else:
            self._head = y

        y.parent = x.parent
        x.parent = y

    
    def rotate_right(self, x: Node, y: Node) -> None:
        x.left = y.right
        y.right = x

        if x.left != None:
            x.left.parent = x
        
        if x.parent != None:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        else:
            self._head = y
        
        y.parent = x.parent
        x.parent = y
    
    def delete(self, key: int) -> None:
        print("hello")
        current = self._head
        remove_node = current

        while current != None:
            if current.key == key:
                break

            if key < current.key:
                current = current.left
            else:
                current = current.right
        else:
            return
        print("this is current", current)
        

        brother = None
        if current.parent != None:
            if current.parent.left == current:
                brother = current.parent.right
            else:
                brother = current.parent.left
        
        if brother == None:
            balance_node = current

            while balance_node.parent != None:
                if balance_node == balance_node.parent.left:
                    balance_node.parent.balance -= 1
                else:
                    balance_node.parent.balance += 1

        
        if current.left == None and current.right == None:
            if current.parent != None:
                if current == current.parent.left:
                    current.parent.left = None
                    current.parent.balance -= 1
                else:
                    current.parent.right = None
                    current.parent.balance += 1
            else:
                self._head = None

        elif current.left != None and current.right == None:
            if current.parent != None:
                current.left.parent = current.parent

                if current == current.parent.left:
                    current.parent.balance -= 1
                    current.parent.left = current.left
                else:
                    current.parent.right = current.left
                    current.parent.balance += 1
            else:
                self._head = self._head.left
                self._head.parent = None
                
        
        elif current.left == None and current.right != None:
            if current.parent != None:
                current.right.parent = current.parent

                if current == current.parent.left:
                    current.parent.balance -= 1
                    current.parent.left = current.right
                else:
                    current.parent.right = current.right
                    current.parent.balance += 1
            else:
                self._head = self._head.right
                self._head.parent = None
        
        else:
            remove_node = self.min(current.right)

            current.key = remove_node.key

            if remove_node.right != None:
                brother = remove_node.right
                remove_node.right.parent = remove_node.parent

                if remove_node == remove_node.parent.left:
                    remove_node.parent.balance -= 1
                    remove_node.parent.left = remove_node.right
                else:
                    remove_node.parent.right = remove_node.right
                    remove_node.parent.balance += 1
            else:
                brother = None

                if remove_node == remove_node.parent.left:
                    remove_node.parent.left = None
                    remove_node.parent.balance -= 1
                else:
                    remove_node.parent.right = None
                    remove_node.parent.balance += 1
        
        if brother == None:
            remove_node = remove_node.parent
            
            while remove_node != None:
                if remove_node.balance == 2 or remove_node.balance == -2:
                    self._add_fixup(remove_node)
                
                remove_node = remove_node.parent
        
        
    def min(self, tree: Node) -> Node:
        while True:
            if tree.left == None:
                return tree
            else:
                tree = tree.left
    
    def max(self, tree: Node) -> Node:
        while True:
            if tree.right == None:
                return tree
            else:
                tree = tree.right

