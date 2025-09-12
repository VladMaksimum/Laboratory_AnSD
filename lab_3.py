#Множители
import math

x = int(input())
print('=======')


K = int(math.log(x,3))
L = int(math.log(x,5))
M = int(math.log(x,7))

for i in range(K+1):
    for j in range(L+1):
        for k in range(M+1):
            x_i = 3**i * 5**j * 7**k
            if x_i <= x:
                print(x_i)

