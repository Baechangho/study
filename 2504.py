#2504
str = input()
bra = list(str)
stack = []
top = 0
answer = 0
mul = 1
last = ' '
for i in range(len(bra)):
    if bra[i] =="("or bra[i] =="{":
        stack.append('(')
        mul *= 2
        top += 1
        last = "("
    elif bra[i] =="[":
        stack.append('[')
        mul *= 3
        top += 1
        last = "["
    elif bra[i] ==")" or bra[i] =="}":
        if top < 1:
            answer = 0
            break
        if last == "(":
            answer += mul
        top -= 1
        if stack[top] == "[":
            answer = 0
            break
        stack.pop()
        mul /= 2
        last = ")"
    elif bra[i] == "]":
        if top < 1:
            answer = 0
            break
        if last == "[":
            answer += mul
        top -= 1
        if stack[top] == "(" or stack[top] == "{":
            answer = 0
            break
        stack.pop()
        mul /= 3
        last = "]"
if top > 0:
    answer = 0
    
print(int(answer))