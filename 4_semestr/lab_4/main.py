from funcs import count_prefixs

string = input("Input main string: ")
substr = input("Input what you want to find: ")

shifts = count_prefixs(substr)
#print(shifts)

k = 0 
flag = True

while k + len(substr) <= len(string):
    i = 0

    while True:
        if i >= len(substr):
            break

        if substr[i] != string[i+k]:
            break

        i += 1
    #print(i, substr, string[k:i+k:])
    
    if i == len(substr):
        print("Substring in range:", k, k + len(substr) - 1)
        flag = False
        break
    
    k += (i - shifts[i])

if flag:
    print("Not found")