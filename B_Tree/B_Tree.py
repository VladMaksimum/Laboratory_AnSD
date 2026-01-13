from typing import Self

class Node:
    def __init__(self, keys: list[int], parent: Self | None, children: list[Self]):
        self.keys = keys
        self.children = children
        self.parent = parent
    
    def __str__(self) -> str:
        if self.parent != None:
            return f"({self.keys} {[str(node) for node in self.children]} parent={self.parent.keys})"
        else:
            return f"({self.keys} {[str(node) for node in self.children]})"

class B_Tree:
    def __init__(self) -> None:
        self._head: Node | None = None
    
    def add(self, key: int) -> None:
        if self._head == None:
            self._head = Node([key], None, [])
            return
        
        current = self._head
        while True:
            if current.children == []:
                current.keys.append(key)
                break
            else:
                if len(current.keys) == 1:
                    if key < current.keys[0]:
                        current = current.children[0]
                    else:
                        current = current.children[1]
                else:
                    if key < current.keys[0]:
                        current = current.children[0]
                    elif key < current.keys[1]:
                        current = current.children[1]
                    else:
                        current = current.children[2]
        current.keys.sort()
        
        self._add_fixup(current)
        
        print(self._head)
    
    def split(self, node: Node) -> None:
        if node.parent == None:
            self._head = Node([node.keys[1]], None, [])
            
            if node.children != []:
                left = Node([node.keys[0]], self._head, [node.children[0], node.children[1]])
                right = Node([node.keys[2]], self._head, node.children[2::])

                node.children[0].parent = left
                node.children[1].parent = left
                node.children[2].parent = right

                if len(node.children) == 4:
                    node.children[3].parent = right
            else:
                left = Node([node.keys[0]], self._head, [])
                right = Node([node.keys[2]], self._head, [])

            self._head.children = [left, right]
        else:
            node.parent.keys.append(node.keys.pop(1))

            if node.children != []:
                chl1 = Node([node.keys[0]], node.parent, [node.children[0], node.children[1]])
                chl2 = Node([node.keys[1]], node.parent, node.children[2::])

                node.children[0].parent = chl1
                node.children[1].parent = chl1
                node.children[2].parent = chl2
                
                if len(node.children) == 4:
                    node.children[3].parent = chl2
            else:
                chl1 = Node([node.keys[0]], node.parent, [])
                chl2 = Node([node.keys[1]], node.parent, [])

            node.parent.children.remove(node)
            node.parent.children.append(chl1)
            node.parent.children.append(chl2)
    
    def transfer(self, node: Node) -> None:
        #print(node, "its problem")
        if len(node.parent.keys) == 1:
            if node == node.parent.children[0]:
                node.parent.keys.append(node.keys.pop(2))
                node.parent.children[1].keys.insert(0, node.parent.keys.pop(0))

                if len(node.children) == 4:
                    node.parent.children[1].children.insert(0, node.children.pop(3))
            else:
                node.parent.keys.append(node.keys.pop(0))
                node.parent.children[0].keys.append(node.parent.keys.pop(0))

                if len(node.children) == 4:
                    node.parent.children[0].children.append(node.children.pop(0))
        else:
            if node == node.parent.children[0]:
                if len(node.parent.children[1].keys) == 1:
                    node.parent.keys.insert(0, node.keys.pop(2))
                    node.parent.children[1].keys.insert(0, node.parent.keys.pop(1))

                    if len(node.children) == 4:
                        node.parent.children[1].children.insert(0, node.children.pop(3))
                else:
                    node.parent.keys.insert(0, node.keys.pop(2))
                    node.parent.children[2].keys.insert(0, node.parent.keys.pop(2))

                    if len(node.children) == 4:
                        node.parent.children[1].children.insert(0, node.children.pop(3))
                        if len(node.parent.children[1].children) == 4:
                            node.parent.children[2].children.insert(0, node.children[1].children.pop(3))

            elif node == node.parent.children[1]:
                if len(node.parent.children[0].keys) == 1:
                    node.parent.keys.insert(1, node.keys.pop(1))
                    node.parent.children[0].keys.insert(1, node.parent.keys.pop(0))

                    if len(node.children) == 4:
                        node.parent.children[0].children.append(node.children.pop(0))
                else:
                    node.parent.keys.insert(0, node.keys.pop(1))
                    node.parent.children[2].keys.insert(0, node.parent.keys.pop(2))

                    if len(node.children) == 4:
                        node.parent.children[2].children.insert(0, node.children.pop(3))
            else:
                if len(node.parent.children[1].keys) == 1:
                    node.parent.keys.append(node.keys.pop(0))
                    node.parent.children[1].keys.insert(1, node.parent.keys.pop(1))

                    if len(node.children) == 4:
                        node.parent.children[1].children.append(node.children.pop(0))
                else:
                    node.parent.keys.append(node.keys.pop(0))
                    node.parent.children[0].keys.append(node.parent.keys.pop(0))

                    if len(node.children) == 4:
                        node.parent.children[1].children.append(node.children.pop(0))
                        if len(node.parent.children[1].children) == 4:
                            node.parent.children[0].children.append(node.children[1].children.pop(0))
                    

    def _add_fixup(self, fixup_node: Node) -> None:
        if len(fixup_node.keys) < 3:
            return

        if fixup_node.parent == None:
            self.split(fixup_node)
        else:
            to_transfer = False
            for kid in fixup_node.parent.children:
                if kid != fixup_node and len(kid.keys) == 1:
                    to_transfer = True
                    break
            
            if to_transfer:
                self.transfer(fixup_node)
            else:
                self.split(fixup_node)
                self._add_fixup(fixup_node.parent)
