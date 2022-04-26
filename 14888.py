#14888
from itertools import permutations

Max = -1000000000
Min = 1000000000
    
N = int(input())
num = list(map(int, input().split()))
oper_4 = list(map(int, input().split()))
oper = list()
for i in range(oper_4[0]):
    oper.append('+')
for i in range(oper_4[1]):
    oper.append('-')
for i in range(oper_4[2]):
    oper.append('*')
for i in range(oper_4[3]):
    oper.append('/')

    
allList = list(permutations(oper,N-1))
allList = list(set(allList))
x = 0
for i in range(len(allList)):        
    a = num[0]
    for j in range(len(allList[i])):
        b = num[j+1]
        if allList[i][j] == "+":
            a = a + b
        elif allList[i][j] == "-":
            a = a - b
        elif allList[i][j] == "*":
            a = a * b
        elif allList[i][j] == "/":
            if a < 0:
                a = -a
                a = a//b
                a = -a
            else:
                a = a // b
    if a > Max:
        Max = a
    if a < Min:
        Min = a
print(Max)
print(Min)

