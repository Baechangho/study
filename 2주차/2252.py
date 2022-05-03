# -*- coding: utf-8 -*-
#2252
start = []
end = []
n,m = map(int, input().split())
stu = [0 for i in range(n)]
ans = []
arr = [0 for i in range(n)]
for i in range(m):
        a,b = map(int, input().split())
        start.append(a)
        end.append(b)
        stu[b-1] += 1
        
for i in range(n):
    if stu[i] == 0:
        ans.append(i+1)
        arr[i] = 1
        break
    
for i in range(len(stu)):
    print(ans[0])
    for i in range(len(start)):
        if start[i] == ans[0]:
            stu[end[i]-1] -= 1
    arr[ans[0]-1] = 1
    del ans[0]
    for j in range(n):
        if stu[j] == 0 and arr[j] != 1:
            ans.append(j+1)
            break
#https://yoongrammer.tistory.com/86
#pypy로 시간초과해결 질문