import sys

N = sys.stdin.readline().rstrip()

arr = list(N)

for x in arr:
    x = int(x)

arr.sort(reverse=True)

s = "".join(arr)
print(int(s))