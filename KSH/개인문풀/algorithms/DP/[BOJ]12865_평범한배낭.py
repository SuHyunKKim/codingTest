import sys

info, *products = [list(map(int, line.split())) for line in sys.stdin.readlines()]

n, k = info # 물품의 수 n, 버틸수 있는 무게 k
