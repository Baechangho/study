# -*- coding: utf-8 -*-
#16916
str = input()
S = list(str)
find = input()
P = list(find)
s = len(S)
p = len(P)
answer = 0
for i in range(s):
    if s-i >= p and answer == 0:
        if S[i] == P[0]:
            answer = 1
            for j in range(p):
                if S[i+j] != P[j]:
                    answer = 0
                    break
    else:
        break
print(answer)