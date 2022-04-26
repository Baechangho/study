#1062
n,k = input().split()
n = int(n)
k = int(k)
all = []
for i in range(n):
    word = []
    a = input()
    all.append(list(set(a)))
set(all)
print(all)