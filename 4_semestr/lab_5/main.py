string = input("Input main string: ")
substr = input("Input what you want to find: ")


shifts: dict[str, int] = {}

for symbol in string:
    if symbol in shifts.keys():
        continue

    if symbol not in substr:
        shifts[symbol] = len(substr)

    elif string[-1] != symbol:
        i=len(substr) - 1
        while substr[i] != symbol:
            i -= 1
        
        shifts[symbol] = len(substr) - i - 1
    
    elif string[-1] == symbol and substr.count(symbol) >= 2:
        i=len(substr) - 2
        while substr[i] != symbol:
            i -= 1
        
        shifts[symbol] = len(substr) - i - 1
    
    else:
        shifts[symbol] = len(substr)
#print(shifts)
    
j = len(substr)
while j <= len(string):
    #print(substr, string[(j - len(substr)):j:])
    if substr == string[(j - len(substr)):j:]:
        print("Substring in range:", j - len(substr), j - 1)
        break

    j += shifts[string[j - 1]]


