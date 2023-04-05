import sys
sys.setrecursionlimit(100000)

T =  int(sys.stdin.readline())


def dfs(x :int, y: int) -> bool:
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
            
    if graph[x][y] == 1:
        graph[x][y] = 0

        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


for _ in range(T):
    # 가로 길이 , 세로 길이, 점
    M, N, K = map(int, sys.stdin.readline().rstrip().split())

    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y =  map(int, sys.stdin.readline().rstrip().split())
        graph[Y][X] = 1

    result = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j) == True:
                result += 1
    print(result) 