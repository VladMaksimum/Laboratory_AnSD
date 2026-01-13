#Арифметическое выражение
equation = input()


notation_stack = ['=']
new_equation = []
number = ''

for symbol in equation:

    is_active = True

    #print(new_equation, notation_stack, symbol)
    if symbol.isnumeric():
        number += symbol
        is_active = False

    while is_active:
        if number != '':
            new_equation.append(int(number))
            number = ''

        if symbol == '(' or ((symbol == '*' or symbol == '/') and (notation_stack[-1] == '=' or notation_stack[-1] == '+' or \
            notation_stack[-1] == '-' or notation_stack[-1] == '(')) or ((symbol == '+' or symbol == '-') and \
            (notation_stack[-1] == '=' or notation_stack[-1] == '(')):

            notation_stack.append(symbol)
            is_active = False
        
        elif ((symbol == ')' or symbol == '+' or symbol == '-' or symbol == '=') and (notation_stack[-1] == '+' or \
            notation_stack[-1] == '-' or notation_stack[-1] == '*' or notation_stack[-1] == '/')) or \
            ((symbol == '*' or symbol == '/') and (notation_stack[-1] == '*' or notation_stack[-1] == '/')):

            new_equation.append(notation_stack[-1])
            notation_stack.pop()
        
        elif symbol == ')' and notation_stack[-1] == '(':
            notation_stack.pop()
            is_active = False
        
        elif symbol == '=' and notation_stack[-1] == '=':
                notation_stack.pop()
                break
                
        elif (symbol == ')' and notation_stack[-1] == '=') or (symbol == '=' and notation_stack[-1] == '('):
                break
        
        else:
            is_active = False


#print(new_equation)

count_stack = []
alright = True

if len(notation_stack)==0:

    for element in new_equation:
        #print(count_stack)
        if type(element) == int:
            count_stack.append(element)
            
        elif element == '+':
            num1 = count_stack[-2]
            num2 = count_stack[-1]

            count_stack.pop()

            count_stack[-1] = num1 + num2
        
        elif element == '-':
            num1 = count_stack[-2]
            num2 = count_stack[-1]

            count_stack.pop()

            count_stack[-1] = num1 - num2

        elif element == '*':
            num1 = count_stack[-2]
            num2 = count_stack[-1]

            count_stack.pop()

            count_stack[-1] = num1 * num2
        
        elif element == '/':
            num1 = count_stack[-2]
            num2 = count_stack[-1]

            if num2 != 0:
                count_stack.pop()

                count_stack[-1] = num1 / num2
            
            else:
                print("Division by zero")
                alright = False
                break
else:
    alright = False

#print(alright)
if alright:
    print(count_stack[0])


        




