'''
[Note]
1 = 1       1
2 = 1 1     2
3 = 1 1 1   3
4 = 4       1
5 = 4 1     2
6 = 4 1 1   3
7 = 4 1 1 1 4
8 = 4 4     2
9 = 9       1
10= 9 1     2
...

'''

N = int(input())
dp = [0] * (N+1) # 0~N까지의 dp테이블을 만들기

for target_num in range(1, N+1): # target_num이 제곱수로 만들 자연수
    dp[target_num] = target_num # 최악의 경우로 초기화 : 오직 1의 제곱으로만

    j = 1
    while j**2 <= target_num: # target_num을 넘지않는 제곱수 모두 탐색
        '''
        [dp[target_num - j**2] + 1] 🚨이 부분 생각이 가장 어려웠음
        j**2을 하나 쓰고 남은 값의 최적해(이는 이전 단계에서 미리 구해둔 값 DP)
        +1 은 j**2를 하나 썼으니 제곱수 하나 추가해주는 값
        '''
        dp[target_num] = min(dp[target_num], dp[target_num - j**2] + 1) # 최솟값 갱신
        j+=1
print(dp[N])
