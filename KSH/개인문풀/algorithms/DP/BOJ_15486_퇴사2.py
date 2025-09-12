'''





'''
import sys

n = int(sys.stdin.readline())

consult_list = [0] * (n+1)

for i in range(n):
    time, price = list(map(int, sys.stdin.readline().split()))
    consult_list[i+1] = [time, price]

