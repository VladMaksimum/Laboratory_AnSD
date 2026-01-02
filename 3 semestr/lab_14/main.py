from ChainedHashTable import ChainedHashTable


hash_table = ChainedHashTable(capacity=100, table_load=0.75)

with open("lab_14/input.txt") as file:

    while True:

        line = file.readline()
        if not line:
            break
        
        line = line.split()
        for word in line:
            hash_table.insert(word)
        

with open("lab_14/output.txt", "w") as out_file:
    out_file.write(str(hash_table))



        
