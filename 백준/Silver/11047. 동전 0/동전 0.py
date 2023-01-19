import sys

# N개의 동전 가치, 가치의 합 K
N, K = map(int, sys.stdin.readline().rstrip().split())

value_list = []
for _ in range(N):
    v = int(sys.stdin.readline().rstrip())
    if v <= K:
        value_list.append(v)
    
value_list.sort(reverse = True)

cnt = 0
for v in value_list:
    cnt += (K//v)
    K %= v
    
print(cnt)