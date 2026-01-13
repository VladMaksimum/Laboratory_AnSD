n = int(input())
letters = input()

stack = ["*"]

for symbol in letters:
    if symbol == stack[-1]:
        stack.pop()
    else:
        stack.append(symbol)

if len(stack) == 1:
    print(1)
else:
    print(0)