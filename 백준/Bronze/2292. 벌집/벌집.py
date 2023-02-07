import sys

N = int(sys.stdin.readline())

i = 0
while N > 0:
    N = N - 6 * i
    i += 1

    if N == 1:
        break
print(i)
