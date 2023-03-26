import sys
from collections import deque

case_num = int(sys.stdin.readline())

for i in range(case_num):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    priorities = list(map(int, sys.stdin.readline().rstrip().split()))

    queue = deque()
    중요도_list = list()
    for 처음위치, 중요도 in enumerate(priorities):
        queue.append((처음위치, 중요도))
        중요도_list.append(중요도)

    가장높은중요도 = max(중요도_list)
    result = dict()
    탈출순위 = 1

    while len(queue) > 0:
        if queue[0][1] >= 가장높은중요도:
            result[queue[0][0]] = 탈출순위
            탈출순위 += 1
            중요도_list.remove(가장높은중요도)
            if len(중요도_list) > 0:
                가장높은중요도 = max(중요도_list)
            queue.popleft()
        else:
            queue.append(queue.popleft())

    print(result[M])