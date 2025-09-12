'''

' 퇴사는 개뿔, 취업 마렵다 '

풀이 접근 방식
- 첫번째 인덱스부터 구하려고 했는데, 안돼서,
맨 마지막 인덱스 부터 구하면서 갔음.

TODO: DP 바텁업과 탑다운 방식 차이를 공부.



'''

import sys

n = int(sys.stdin.readline().rstrip())
schedule = [] # [Time, Price] 꼴의 스케줄 리스트
for _ in range(n):
    schedule.append(list(map(int, sys.stdin.readline().split())))

d = [0] * (n+2) # dp 테이블 선언, n+2 인 이유는, n번째 날이 참조할 n+1번째 날이 필요하기 때문임.

for i in range(n, 0, -1):

    time = schedule[i-1][0]
    price = schedule[i-1][1]

    if i+time-1 <= n: # 만일 상담 소요날이 퇴사일 전이면
        d[i] = max(d[i + 1], d[i + time] + price)
    else:
        d[i] = d[i+1]

print(d[1])


from sys import stdin

n = int(input())

time = [-1]
point = [-1]

for _ in range(n):
    t, p = map(int, stdin.readline().split())
    time.append(t)
    point.append(p)

d = [0]*(n+51) 

for i in range(1, n+1):
    d[i+time[i]] = max(d[i+time[i]], d[i]+point[i]) # 상담을 진행하는 경우
    d[i+1] = max(d[i+1], d[i]) # 상담 안하고 기다리는 경우 print(d[n+1])