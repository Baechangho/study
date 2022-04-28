#20115
n = int(input())
drink = list(map(int, input().split()))
answer = sum(drink)/2 + max(drink)/2
print(answer)