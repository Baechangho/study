# -*- coding: utf-8 -*-
#1806
# =============================================================================
# import sys
# n,s = input().split()
# n = int(n)
# s = int(s)
# num = list(map(int, input().split()))
# k_sum = [0 for c in range(n)]
# if sum(num) < s:
#     print(0)
# else:
#     for i in range(n):
#         for j in range(n-i):
#             k_sum[j] += num[j+i]
#             if k_sum[j] >= s:
#                 print(i+1)
#                 sys.exit()
# =============================================================================
                                
n,s = input().split()
n = int(n)
s = int(s)
num = list(map(int, input().split()))
a = 0
b = 0
cur = num[0]
answer = n+1
while(a != n-1):
    if answer > b-a+1 and cur >= s:
        answer = b-a+1
    if b == n-1:                #오른쪽끝에도달
        cur -= num[a]
        a += 1
    elif b == a:                #왼쪽과 오른쪽이 같으면
        b += 1
        cur += num[b]
    elif cur < s :              #합이 더 작다면
        b += 1
        cur += num[b]
    elif cur > s:               #합이 더 크다면
        cur -= num[a]
        a += 1
    else:                       #합이 같다면
        b += 1
        cur += num[b]
        cur -= num[a]
        a += 1

if answer > b-a+1 and cur >= s:
    answer = b-a+1
if answer == n+1:
    print(0)
else:
    print(answer)