#1700
n,k = input().split()
n = int(n)
k = int(k)
num = list(map(int, input().split()))
plug = []
plug_can = []     
for b in range(n):
    plug_can.append(k+1)
answer = 0
for i in range(k):
    biggest = 0
    biggest_seat = 0
    
    if num[i] in plug:
        continue
    elif len(plug) < n:
        plug.append(num[i])
    else:
        for j in range(n):
            if plug[j] in num[i:]:
                plug_can[j] = num[i:].index(plug[j])
            else:
                plug_can[j] = k+1
        for a in range(n):
            if plug_can[a] > biggest:
                biggest = plug_can[a]
                biggest_seat = a
        plug[biggest_seat] = num[i]
        answer += 1
print(answer)