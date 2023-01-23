import sys

# 0 < N < 99
N = sys.stdin.readline().rstrip()

if len(N) == 1:
    N = int(N) * 10

cycle = 0

T = int(N)
while True:
    s = T // 10 + T % 10

    T = (T % 10) * 10 + (s % 10)
    cycle += 1

    if int(N) == T:
        break

print(cycle) 