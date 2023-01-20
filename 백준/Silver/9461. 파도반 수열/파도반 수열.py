# T: Test Case 개수
T = int(input())

dp = [0] * 100000
# Top-Down DP
def P(n:int) -> int:
    if n == 1 or n == 2 or n == 3:
        return 1
    elif n == 4 or n == 5:
        return 2
    elif n == 6:
        return 3
        
    if dp[n] != 0:
        return dp[n]
    
    dp[n] = P(n-1) + P(n-5)
    return dp[n]

for _ in range(T):
    N = int(input())
    print(P(N))