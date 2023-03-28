import sys

def dp(N: int) -> int:
    cache = [N+1] * (N+1)
    cache[1] = 0
    
    for i in range(2, N+1):
        if i % 3 == 0:
            cache[i] = min(cache[i//3] + 1, cache[i])
    
        if i % 2 == 0:
            cache[i] = min(cache[i//2] + 1, cache[i])
        
        cache[i] = min(cache[i], cache[i-1]+1)
        
    return cache[N]
    

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    result = dp(N)
    print(result)