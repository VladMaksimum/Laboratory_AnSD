#Скобки
stack = [0]
flag = False
string = input()


for bracket in string:
    if (bracket == ')' and stack[-1] != '(') or (bracket == ']' and stack[-1] != '[') or (bracket == '}' and stack[-1] != '{'):
        print("wrong")
        flag = True
        break
    
    if bracket == '(' or bracket == '[' or  bracket == '{':
        stack.append(bracket)
    else:
        stack.pop(-1)
    

if len(stack)==1:
    print("correct")
elif not(flag):
    print("wrong")