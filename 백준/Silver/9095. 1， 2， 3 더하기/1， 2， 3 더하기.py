N = int(input())

d = [0] * 100000

def calc(x):
    if x == 1:
        return 1 # 1
    elif x == 2:
        return 2 # 1 + 1, 2
    elif x == 3:
        return 4 # 1 + 1 + 1, 1 + 2, 3
    
    if d[x] != 0:
        return d[x]
    
    d[x] = calc(x-1) + calc(x-2) + calc(x-3)
    return d[x]
for _ in range(N):
    num = int(input())
    print(calc(num))