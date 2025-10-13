

class LinearHashTable:
        
    def __init__(self, capacity=100, table_load = 3/4) -> None:
        self.table = [None] * capacity
        self.capacity = capacity
        self.table_load = table_load
        self.size = 0
    
    
    def hash_function(self, key) -> int:
        return int(hash(key)) % self.capacity
    

    def _insert(self, key, table) -> bool:
        index = self.hash_function(key)

        while table[index] != None:
            if table[index] == key:
                return False
            
            index = (index + 1) % len(table)
        
        table[index] = key
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

            self._insert(self.table[i], tmp_table)
        
        self.table = tmp_table
    

    def find(self, key) -> int:
        index = self.hash_function(key)

        while self.table[index] != None:
            if self.table[index] == key:
                return index
            
            index = (index + 1) % self.capacity
        
        return -1

    


            

        

