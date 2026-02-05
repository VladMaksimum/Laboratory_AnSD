from typing import Self


class Node:
    def __init__(self, string: str, is_possible: bool, parent: Self | None = None):
        self.string = string
        self.next: dict[str, Self] = {}
        self.suff_link: Self | None = None
        self.parent = parent
        self.is_possible = is_possible


class String_Tree:
    def __init__(self):
        self.root = Node('', False)
    
    def add(self, string: str) -> None:
        current = self.root

        i = 0
        while current.string != string[:(len(string) - 1):]:
            if string[i] in current.next.keys():
                current = current.next[string[i]]
            else:
                current.next[string[i]] = Node(string[:(i+1):], False, current)
                current = current.next[string[i]]

            i += 1
        
        if string[-1] in current.next.keys():
            current = current.next[string[-1]]
            current.is_possible = True
        else:
            current.next[string[-1]] = Node(string, True, current)

    def get_move(self, current: Node, symbol: str) -> Node:
        #print(current.string, symbol, "move", current.next.keys())
        if not symbol in current.next.keys():
            if current == self.root:
                current.next[symbol] = self.root
            else:
                current.next[symbol] = self.get_move(self.get_suff_link(current), symbol)
        
        return current.next[symbol]
    
    def get_suff_link(self, current: Node) -> Node:
        #print(current.string, "link")
        if current.suff_link == None:
            if len(current.string) <= 1:
                current.suff_link = self.root
            
            else:
                current.suff_link = self.get_move(self.get_suff_link(current.parent), current.string[-1])
            

        return current.suff_link


    def find_in(self, string: str) -> None:
        current = self.root

        for i in range(len(string)):
            #print(current.string)
            current = self.get_move(current, string[i])
            #print(i)

            if current.is_possible:
                print(f"Substring {string[(i - len(current.string)) + 1:i + 1:]} in range {i - len(current.string) + 1} \
{(i)}")
            
            #print(current.string, "after")


if __name__ == "__main__":
    tree = String_Tree()

    print(tree.root, tree.get_suff_link(tree.root))
