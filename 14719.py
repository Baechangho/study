#14719
h,w = input().split()
h = int(h)
w = int(w)
num = list(map(int, input().split()))
answer = 0
flag = 0
count = 0
for i in range(h):
    for j in range(w):
        if num[j] == h - i:
            flag = 1
            answer += count
            count = 0
            num[j] -= 1
        elif flag == 1:
            count += 1
        if j == w-1:
            flag = 0
            count = 0
print(answer)