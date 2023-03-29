import sys

N = int(sys.stdin.readline())

stairs = []
cache = [0] * (N + 2)

for _ in range(N):
    score = int(sys.stdin.readline())
    stairs.append(score)

if N <= 2:
    print(sum(stairs))
else:
    cache[0] = stairs[0]
    cache[1] = stairs[0] + stairs[1]

    # 연속된 3개의 계단을 밟으면 안되는 조건 구현 방법 고민
    for i in range(2, N):
        cache[i] = max(cache[i-3] + stairs[i-1] + stairs[i], cache[i-2] + stairs[i])
    
    print(cache[N-1])