'''

- 모든 경우를 다 탐색하기

조건
- 연산은 앞에서부터 차례대로
- 나누기는 몫만 취함
    음수/음수 나누기 -> 양수
    음수/양수 나누기 -> 나누고 - 붙임
    양수/음수 나누기 -> 안됨
    양수/양수 나누기 -> 양수


- 최댓값과 최솟값 구하기


'''
import sys
from itertools import permutations

# 1. 입력 받기
n = int(sys.stdin.readline().rstrip())
# print(n, type(n))

numbers = list(map(int, sys.stdin.readline().split()))
# print(numbers)

operator = ['p','m','t','d']
operator_count = list(map(int, sys.stdin.readline().split()))
# print(operator_count)
operators = []
for op, op_c in zip(operator, operator_count):
    for i in range(op_c):
        operators.append(op)

'''
# 2. 백트래킹
cases = list(permutations(operators, n-1))
# print(cases)

ans = numbers[0]
count = 1
cals = []

for case in cases:
    for c in case:
        next_num = numbers[count]
        if c == "p":
            ans += next_num
        elif c == "m":
            ans -= next_num
        elif c == "t":
            ans = ans*next_num
        else:
            if ans < 0 and next_num < 0:
                ans = abs(ans) // abs(next_num)
            elif ans < 0 and next_num > 0:
                ans = (abs(ans) // next_num) * -1
            elif ans >= 0 and next_num < 0:
                ans = (ans // abs(next_num)) * -1
            else:
                ans = (ans // abs(next_num))
        count += 1
    cals.append(ans)
    ans = numbers[0]
    count = 1

print(max(cals))
print(min(cals))
'''


# 1e9는 실수여서 정수로 변환 해줘야함
max_value = -int(1e9)
min_value = int(1e9)

# 실수 포인트
# visited = [[0] * (n-1)]
visited = [0] * (n-1)
# print(visited)

def dfs(value, count):
    global max_value, min_value, visited

    # print(value)

    if count == n: # 실수 포인트 - n-1로 함. 왜? n-1개니까. 그치만 그게 아님. 1부터 이기 때문.
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value

        return True

    for idx, ops in enumerate(operators):
        if not visited[idx]:
            visited[idx] = True
            if ops == 'p':
                new_value = value + numbers[count]
            elif ops == 'm':
                new_value = value - numbers[count]
            elif ops == 't':
                new_value = value * numbers[count]
            else:
                if value < 0:
                    new_value = (abs(value) // numbers[count]) * -1
                else:
                    new_value = value // numbers[count]

            count += 1
            dfs(new_value, count)
            visited[idx] = False
            count -= 1

    return None

dfs(numbers[0], 1)

print(max_value)
print(min_value)
















