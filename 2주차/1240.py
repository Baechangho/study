#1240
n,m = input().split()
n = int(n)
m = int(m)
arr = [list() for i in range(n+1)]
visit = [0 for i in range(n+1)]
for i in range(n-1):
    a,b,dis = map(int,input().split())
    arr[a].append((b,dis))
    arr[b].append((a,dis))
#########https://velog.io/@chaegil15/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B7%B8%EB%9E%98%ED%94%84-%EA%B0%80%EC%9E%A5-%EB%A8%BC-%EB%85%B8%EB%93%9C

def find(finding_point,cur_point,sum_,answer):
    visit[cur_point] = 1
    for i,j,k in arr: ##데이터프레임의 형태 리스트 추출
        for x in range(j):
            if arr[cur_point][i][0] != finding_point and visit[finding_point] == 0:
                sum_ += arr[cur_point][i][1]
                cur_point = arr[cur_point][i][0]
                find(finding_point,cur_point,sum_,answer)
            elif arr[cur_point][i][0] == finding_point:
                if answer > sum_:
                    answer = sum_
            else:
                visit[cur_point] == 0
    print(answer)
for i in range(m):
    p,q = input().split()
    p = int(p)
    q = int(q)
    find(p,q,0,0)