import sys


def dfs(graph, start, visited):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)



if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    
    N, M = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    count = 0

    for _ in range(M):
        u, v = map(int, sys.stdin.readline().rstrip().split())

        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, N+1):
        if not visited[i]:
            dfs(graph, i, visited)
            count += 1
    
    print(count)
    
