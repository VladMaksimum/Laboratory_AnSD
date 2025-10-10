

class HashTable:
        
    def __init__(self, capcity=64) -> None:
        self.table = [None] * capacity
        self.capacity = capacity
        self.size = 0
    
    
    def hash_function(self, key) -> int:
        if not size:
            size =self.capacity
        
        return int(hash(key)) % size
    

    def insert(self, key) -> None:
        index = hash_function(key)

        if not table[index]:
            table[index] = key
            return
        
        while table[index]:
            index += 1

            if index > size:
                pass
                #self.resize()
            

        

