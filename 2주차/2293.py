# -*- coding: utf-8 -*-
#2293
n, k = map(int, input().split())
coin = []
d = []
for i in range(n):
    coin.append(int(input()))
coin.sort()
answer = [0 for i in range(k+1)]
answer[0] = 1

for i in coin:
    for j in range(i, k+1):
        answer[j] += answer[j - i]
print(answer[k])
    