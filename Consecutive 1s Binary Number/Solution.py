import math

n = int(input())
b = str(bin(n))[2:].split('0')
c = [len(num) for num in b]
print(max(c))
