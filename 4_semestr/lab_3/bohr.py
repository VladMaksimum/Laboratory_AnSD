from typing import Self

def count_prefixs(string: str) -> list[int]:
    res: list[int] = [0 for _ in range(len(string))]
    res[0] = -1
    cnt = 0

    for i in range(2, len(string)):
        while cnt != 0 and string[cnt] != string[i]:
            cnt = res[cnt-1]
        
        if string[cnt] == string[i]:
            cnt += 1

        res[i] = cnt
    

    return res

class Node:
    def __init__(self, string: str, is_possible: bool):
        self.string = string
        self.next: dict[str, Self] = {}
        self.suff_link: list[Self] = []
        self.is_possible = is_possible
    
    def min_suff(self) -> str:
        prefixs = count_prefixs(self.string)

        return self.string[:prefixs[-1]:]


class String_Tree:
    def __init__(self):
        self.root = Node('', True)
    
    def add(self, string: str) -> None:
        current = self.root

        i = 0
        while current.string != string[:(len(string) - 1):]:
            if string[i] in current.next.keys():
                current = current.next[string[i]]
            else:
                current.next[string[i]] = Node(string, False)
            i += 1
        
        current.next[string[-1]] = Node(string, True)
        current = current.next[string[-1]]

        suff = current.min_suff()
        suff_node = self._find(suff)[1]

        if suff_node == None:
            return
        
        if not suff_node.is_possible:
            return
        
        current.suff_link = suff_node

    
    def _find(self, string: str) -> tuple[bool, Node | None]:
        current = self.root

        i = 0
        while current.string != string:
            if string[i] in current.next.keys():
                current = current.next[string[i]]
                i+=1
            else:
                return (False, None)
        
        return (True, current)

    def find_in(self, string: str) -> tuple[int, int]:
        q = 0
        res = ()

        for symbol in string:
            

        return res
    


