'''


- 대기열 -> 왼쪽 순으로 검사
    예외: 왼쪽이 비어있을 때
- 만약 순서가 아니면, 왼쪽으로 빠지기
-


'''

import sys
from collections import deque

info = [list(map(int, line.split())) for line in sys.stdin.readlines()]

n = info[0][0]
line = info[1]

q = deque(line)
stack = []

turn = 1

while True:

    # if not q:
    #     break
    nex = 0
    if q:
        nex = q.popleft()

    if nex == turn:
        turn += 1
    elif stack and stack[-1] == turn:
        stack.pop()
        turn += 1
    else:
        stack.append(nex)

    if not q:
        break

if turn == n:
    print("Nice")
else:
    print("Sad")