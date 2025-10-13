from LinearHashTable import LinearHashTable


hash_table = LinearHashTable(capacity=100, table_load=3/4)

with open("lab_13/input.txt") as file:

    while True:

        line = file.readline()
        if not line:
            break
        
        line = line.split()
        for word in line:
            hash_table.insert(word)
        
        #print(hash_table.table)
print(hash_table.find("efforts"))

        
