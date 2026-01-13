class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class ChainedHashTable:
    def __init__(self, capacity=100, table_load = 3/4) -> None:
        self.table = [None] * capacity
        self.capacity = capacity
        self.table_load = table_load
        self.size = 0
    
    def hash_function(self, key) -> int:
        return int(hash(key)) % self.capacity
    

    def _insert(self, key, table) -> bool:
        index = self.hash_function(key)
        tmp_node = Node(key)

        if table[index] == None:
            table[index] = tmp_node
            return True
        
        current_node = table[index]
        while current_node != None:
            if current_node.key == tmp_node.key:
                return False
            
            if current_node.next == None:
                break

            current_node = current_node.next
        
        current_node.next = tmp_node
        return True
    

    def insert(self, key) -> None:
        is_inserted = self._insert(key, self.table)

        if not is_inserted:
            return 
        
        self.size += 1
        tmp_load = self.size / self.capacity
        if tmp_load > self.table_load:
            self.table_load = tmp_load
            self.resize()
    

    def resize(self) -> None:
        self.capacity *= 2
        tmp_table = [None] * self.capacity

        for i in range(len(self.table)):
            if self.table[i] == None:
                continue
            
            current = self.table[i]
            chain_list = []
            while current:
                chain_list.append(current.key)
                if not current.next:
                    break
                
                current = current.next
            
            for elem in chain_list:
                self._insert(elem, tmp_table)

        
        self.table = tmp_table
    

    def find(self, key) -> int:
        index = self.hash_function(key)
        current = self.table[index]
        if not current:
            return -1
        
        while current:
            if current.key == key:
                return current.key
            if current.next == None:
                return -1
            
            current = current.next


    
    def __str__(self) -> str:
        result = ''

        for index, current in enumerate(self.table):
            if not current:
                continue

            result += (str(index) + " : ")
            while current:
                result += str(current.key)
                if not current.next:
                    result += '\n'
                    break
                
                result += ", "
                current = current.next

            

        
        return result
    
