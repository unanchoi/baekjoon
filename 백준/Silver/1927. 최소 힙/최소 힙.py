import sys
import heapq

N = int(sys.stdin.readline())

heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)