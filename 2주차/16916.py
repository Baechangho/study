# -*- coding: utf-8 -*-
#16916
str = input()
S = list(str)
find = input()
P = list(find)
answer = 0
for i in range(len(S)):
    if len(S)-i< len(P):
        break
    if S[i] == P[0]:
        answer = 1
        for j in range(len(P)-1):
            if S[i+1+j] == P[j+1]:
                answer = 1
            elif S[i+1+j] != P[j+1]:
                answer = 0
                break
print(answer)