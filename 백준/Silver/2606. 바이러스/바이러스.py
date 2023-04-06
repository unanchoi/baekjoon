import sys

cpu_num = int(sys.stdin.readline())
edge_num = int(sys.stdin.readline())


def dfs(graph, start, visited, count):
    visited[start] = True
    count += 1

    for i in graph[start]:
        if not visited[i]:
            count = dfs(graph, i, visited, count)
    return count

graph = [[] for _ in range(edge_num + 10)]

for _ in range(edge_num):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(edge_num):
    graph[i+1].sort()

visited = [False] * ((edge_num) + 10)
count = dfs(graph, 1, visited, 0)

print(count-1)
# DFS로 찾고, return True일 떄, count +=1 
