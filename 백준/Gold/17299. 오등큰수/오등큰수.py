from collections import defaultdict
import sys

N = int(input())
a = list(map(int, sys.stdin.readline().rstrip().split()))

def next_greater_frequency(arr):
    n = len(arr)
    frequency = defaultdict(int)
    for num in arr:
        frequency[num] += 1

    stack = []
    result = [-1] * n
    for i in range(n - 1, -1, -1):
        while stack and (frequency[stack[-1]] <= frequency[arr[i]]):
            stack.pop()

        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])

    return result

output = next_greater_frequency(a)
print(*output)