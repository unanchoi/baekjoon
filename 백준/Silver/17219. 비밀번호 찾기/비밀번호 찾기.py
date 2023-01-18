import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

info_dict = dict()

for _ in range(N):
    key, value = sys.stdin.readline().rstrip().split()
    
    info_dict[key] = value
    
for _ in range(M):
    domain = sys.stdin.readline().rstrip()
    print(info_dict[domain])
    
    