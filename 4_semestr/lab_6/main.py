from funcs import count_hash
from funcs import update_hash

string = input("Input main string: ")
substr = input("Input what you want to find: ")

power = 128
q = 2**32

k = 0
hs = count_hash(string[k:k+len(substr):], power, q)
hq = count_hash(substr, power, q)


while True:
    #print(string[k:k+len(substr):], hs, substr, hq)

    if hs == hq:
        if string[k:k+len(substr):] == substr:
            print("Substring in range:", k, k + len(substr) - 1)
            break
        continue

    if k + len(substr) >= len(string):
        print("Substring not found")
        break

    hs = update_hash(hs, string[k], string[k + len(substr)], len(substr), power, q)

    k += 1
        

