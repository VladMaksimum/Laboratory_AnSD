from bohr import String_Tree

string = input("Input main string: ")
n = int(input("Input quantity of substrings: "))
substrs = [input("Input what you want to find: ") for _ in range(n)]

tree = String_Tree()

for s in substrs:
    tree.add(s)
    
tree.find_in(string)


