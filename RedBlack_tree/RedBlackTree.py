from typing import Self
from enum import Enum

class Color(Enum):
    RED = 1,
    BLACK = 2

class Node:
    def __init__(self, key: int, color: Color, parent: Self | None = None, \
                 left: Self | None = None, right: Self | None = None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color
    
    def __str__(self) -> str:
        if self.parent != None:
            return f"({self.key} {self.left} {self.right} {self.color} parent={self.parent.key})"
        else:
            return f"({self.key} {self.left} {self.right} {self.color})"

class RedBlackTree:
    def __init__(self) -> None:
        self._head: Node | None = None

    def rotate_left(self, x: Node, y: Node) -> Node:
        x.right = y.left
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
        y.left = x
        #print(self._head, x.parent, y.parent)
        return x
    
    def rotate_right(self, x: Node, y: Node) -> Node:
        #print(x,y)
        x.left = y.right
        if x.left != None:
            x.left.parent = x
        y.parent = x.parent

        if x.parent != None:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        else:
            self._head = y

        x.parent = y
        y.right = x
        #print(self._head)
        return x

    def _add_fixup(self, current: Node) -> None:
        #print(current, "current")
        if current.parent.color == Color.BLACK or current.parent == self._head:
            return
        
        # father is left
        if current.parent == current.parent.parent.left:
            if current.parent.parent.right == None:
                if current == current.parent.right:
                    current = self.rotate_left(current.parent, current)
                
                current.parent.color = Color.BLACK
                current.parent.parent.color = Color.RED
                self.rotate_right(current.parent.parent, current.parent)
                return

            elif current.parent.parent.right.color == Color.BLACK:
                if current == current.parent.right:
                    current = self.rotate_left(current.parent, current)
                
                current.parent.color = Color.BLACK
                current.parent.parent.color = Color.RED
                self.rotate_right(current.parent.parent, current.parent)
                return
            
            else:
                current.parent.parent.right.color = Color.BLACK
                current.parent.color = Color.BLACK
                current.parent.parent.color = Color.RED
                current = current.parent.parent
                
                if current == self._head:
                    current.color = Color.BLACK
                    return
                
                self._add_fixup(current)
                return
        
        # father is right
        else:
            if current.parent.parent.left == None:
                if current == current.parent.left:
                    current = self.rotate_right(current.parent, current)
                
                current.parent.color = Color.BLACK
                current.parent.parent.color = Color.RED
                self.rotate_left(current.parent.parent, current.parent)
                return

            elif current.parent.parent.left.color == Color.BLACK:
                if current == current.parent.left:
                    current = self.rotate_right(current.parent, current)
                
                current.parent.color = Color.BLACK
                current.parent.parent.color = Color.RED
                self.rotate_left(current.parent.parent, current.parent)
                return
            
            else:
                current.parent.parent.left.color = Color.BLACK
                current.parent.color = Color.BLACK
                current.parent.parent.color = Color.RED
                current = current.parent.parent

                if current == self._head:
                    current.color = Color.BLACK
                    return

                self._add_fixup(current)
                return
        
            


    def add(self, key: int) -> None:
        #print(self._head)
        if self._head == None:
            self._head = Node(key, Color.BLACK)
            return
        
        current = self._head
        
        while True:
            if key < current.key:
                if current.left != None:
                    current = current.left
                else:
                    current.left = Node(key=key, color=Color.RED, parent=current)
                    current = current.left
                    break
            elif key >= current.key:
                if current.right != None:
                    current = current.right
                else:
                    current.right = Node(key=key, color=Color.RED, parent=current)
                    current = current.right
                    break
        self._add_fixup(current)
    
    def print(self, head_node) -> None:
        if head_node.key != None:
            print(head_node.key, end=" ")
    
        if head_node.left != None:
            self.print(head_node.left)
        if head_node.right != None:
            self.print(head_node.right)
    
    def delete(self, key: int) -> None:
        current = self._head

        if current == None:
            raise Exception("No tree")

        while True:
            print(current.key, key)
            if current.key == key:
                break
            
            if current.key <= key:
                if current.right != None:
                    current = current.right
                else:
                    raise Exception("Element not found")
            else:
                if current.left != None:
                    current = current.left
                else:
                    raise Exception("Element not found")
        
        if current == self._head and current.left == None and current.right == None:
            self._head = None
            return

        if current.left != None and current.right != None:
            remove_node = self.min(current.right)

            tmp = remove_node.key
            remove_node.key = current.key
            current.key = tmp

            if remove_node.right != None:
                remove_node.parent.left = remove_node.right
                remove_node.right.parent = remove_node.parent
            else:
                remove_node.parent.left = None

        elif current.color == Color.BLACK and current.left != None and current.right == None:
            tmp = current.left.key
            current.left.key = current.key
            current.key = tmp

            current.left = None
        
        elif current.color == Color.BLACK and current.left == None and current.right != None:
            tmp = current.right.key
            current.right.key = current.key
            current.key = tmp

            current.right = None
        
        elif current.color == Color.RED and current.left == None and current.right == None:
            if current.parent.right == current:
                current.parent.right = None
            else:
                current.parent.left = None

        elif current.color == Color.BLACK and current.left == None and current.right == None:
            self._delete_fixup(current, current.color)

            if current.parent.right == current:
                current.parent.right = None
            else:
                current.parent.left = None



        
    def _delete_fixup(self, fixup_node: Node, fixup_color: Color) -> None:
        print(fixup_node)
        if fixup_color == Color.RED:
            return
        
        
        if fixup_node.parent.left == fixup_node:
            if fixup_node.parent.right.color == Color.RED:
                if fixup_node.parent.right.left != None and fixup_node.parent.right.right != None:
                    if fixup_node.parent.right.left.color == Color.BLACK and fixup_node.parent.right.right.color == Color.BLACK:
                        fixup_node.parent.color = Color.RED
                        fixup_color.parent.right.color = Color.BLACK
                        self.rotate_left(fixup_node.parent, fixup_node.parent.right)
                elif fixup_node.parent.right.left == None and fixup_node.parent.right.right != None:
                    if fixup_node.parent.right.right.color == Color.BLACK:
                        fixup_node.parent.color = Color.RED
                        fixup_color.parent.right.color = Color.BLACK
                        self.rotate_left(fixup_node.parent, fixup_node.parent.right)
                elif fixup_node.parent.right.left != None and fixup_node.parent.right.right == None:
                    if fixup_node.parent.right.left.color == Color.BLACK:
                        fixup_node.parent.color = Color.RED
                        fixup_color.parent.right.color = Color.BLACK
                        self.rotate_left(fixup_node.parent, fixup_node.parent.right)
                else:
                    fixup_node.parent.color = Color.RED
                    fixup_color.parent.right.color = Color.BLACK
                    self.rotate_left(fixup_node.parent, fixup_node.parent.right)
            else:
                if fixup_node.parent.right.left != None and fixup_node.parent.right.right != None:
                    if fixup_node.parent.right.left.color == Color.BLACK and fixup_node.parent.right.right.color == Color.BLACK:
                        fixup_node.parent.right.color = Color.RED
                        self._delete_fixup(fixup_node.parent, fixup_node.parent.color)

                    elif fixup_node.parent.right.left.color == Color.RED and fixup_node.parent.right.right.color == Color.BLACK:
                        fixup_node.parent.right.color = Color.RED
                        fixup_node.parent.right.left.color = Color.BLACK
                        self.rotate_right(fixup_node.parent.right, fixup_node.parent.right.left)
                        self._delete_fixup(fixup_node, fixup_color)
                    else:
                        fixup_node.parent.right.color = fixup_node.parent.color
                        fixup_node.parent.right.right.color = Color.BLACK
                        fixup_node.parent.color = Color.BLACK
                        self.rotate_left(fixup_node.parent, fixup_node.parent.right)
                        return
                elif fixup_node.parent.right.left == None and fixup_node.parent.right.right != None:
                    if fixup_node.parent.right.right.color == Color.BLACK:
                        fixup_node.parent.right.color = Color.RED
                        self._delete_fixup(fixup_node.parent, fixup_node.parent.color)

                    else:
                        fixup_node.parent.right.color = fixup_node.parent.color
                        fixup_node.parent.right.right.color = Color.BLACK
                        fixup_node.parent.color = Color.BLACK
                        self.rotate_left(fixup_node.parent, fixup_node.parent.right)
                        return
                elif fixup_node.parent.right.left != None and fixup_node.parent.right.right == None:
                    if fixup_node.parent.right.left.color == Color.BLACK:
                        fixup_node.parent.right.color = Color.RED
                        self._delete_fixup(fixup_node.parent, fixup_node.parent.color)

                    elif fixup_node.parent.right.left.color == Color.RED:
                        fixup_node.parent.right.color = Color.RED
                        fixup_node.parent.right.left.color = Color.BLACK
                        self.rotate_right(fixup_node.parent.right, fixup_node.parent.right.left)
                        self._delete_fixup(fixup_node, fixup_color)
                else:
                    fixup_node.parent.right.color = Color.RED
                    self._delete_fixup(fixup_node.parent, fixup_node.parent.color)
                
        

        else:
            if fixup_node.parent.left.color == Color.RED:
                if fixup_node.parent.left.left != None and fixup_node.parent.left.right != None:
                    if fixup_node.parent.left.left.color == Color.BLACK and fixup_node.parent.left.right.color == Color.BLACK:
                        fixup_node.parent.color = Color.RED
                        fixup_color.parent.left.color = Color.BLACK
                        self.rotate_right(fixup_node.parent, fixup_node.parent.left)
                elif fixup_node.parent.left.left == None and fixup_node.parent.left.right != None:
                    if fixup_node.parent.left.right.color == Color.BLACK:
                        fixup_node.parent.color = Color.RED
                        fixup_color.parent.left.color = Color.BLACK
                        self.rotate_right(fixup_node.parent, fixup_node.parent.left)
                elif fixup_node.parent.left.left != None and fixup_node.parent.left.right == None:
                    if fixup_node.parent.left.left.color == Color.BLACK:
                        fixup_node.parent.color = Color.RED
                        fixup_color.parent.left.color = Color.BLACK
                        self.rotate_right(fixup_node.parent, fixup_node.parent.left)
                else:
                    fixup_node.parent.color = Color.RED
                    fixup_color.parent.left.color = Color.BLACK
                    self.rotate_right(fixup_node.parent, fixup_node.parent.left)
            else:
                if fixup_node.parent.left.left != None and fixup_node.parent.left.right != None:
                    if fixup_node.parent.left.left.color == Color.BLACK and fixup_node.parent.left.right.color == Color.BLACK:
                        fixup_node.parent.left.color = Color.RED
                        self._delete_fixup(fixup_node.parent, fixup_node.parent.color)

                    elif fixup_node.parent.left.right.color == Color.RED and fixup_node.parent.left.left.color == Color.BLACK:
                        fixup_node.parent.left.color = Color.RED
                        fixup_node.parent.left.right.color = Color.BLACK
                        self.rotate_left(fixup_node.parent.left, fixup_node.parent.left.right)
                        self._delete_fixup(fixup_node, fixup_color)
                    else:
                        fixup_node.parent.left.color = fixup_node.parent.color
                        fixup_node.parent.left.left.color = Color.BLACK
                        fixup_node.parent.color = Color.BLACK
                        self.rotate_right(fixup_node.parent, fixup_node.parent.left)
                        return
                elif fixup_node.parent.left.left == None and fixup_node.parent.left.right != None:
                    if fixup_node.parent.left.right.color == Color.BLACK:
                        fixup_node.parent.left.color = Color.RED
                        self._delete_fixup(fixup_node.parent, fixup_node.parent.color)

                    elif fixup_node.parent.left.right.color == Color.RED:
                        fixup_node.parent.left.color = Color.RED
                        fixup_node.parent.left.right.color = Color.BLACK
                        self.rotate_left(fixup_node.parent.left, fixup_node.parent.left.right)
                        self._delete_fixup(fixup_node, fixup_color)

                elif fixup_node.parent.left.left != None and fixup_node.parent.left.right == None:
                    if fixup_node.parent.left.left.color == Color.BLACK:
                        fixup_node.parent.left.color = Color.RED
                        self._delete_fixup(fixup_node.parent, fixup_node.parent.color)

                    else:
                        fixup_node.parent.left.color = fixup_node.parent.color
                        fixup_node.parent.left.left.color = Color.BLACK
                        fixup_node.parent.color = Color.BLACK
                        self.rotate_right(fixup_node.parent, fixup_node.parent.left)
                else:
                    fixup_node.parent.left.color = Color.RED
                    self._delete_fixup(fixup_node.parent, fixup_node.parent.color)
            
    
    def min(self, tree: Node) -> Node:
        while tree.left != None:
            tree = tree.left
        
        return tree
    
    def max(self, tree: Node) -> Node:
        while tree.right != None:
            tree = tree.right
        
        return tree


        
