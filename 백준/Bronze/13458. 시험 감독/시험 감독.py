import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
B, C = map(int, sys.stdin.readline().rstrip().split())

count = 0
for num in arr:
    if num > B:
        count += 1
        num -= B
        if num % C == 0:
            count += num // C
        else:
            count += (num // C) + 1
    else:
        count += 1
   

print(count)