import sys

# N은 100000개
N = int(sys.stdin.readline())

f_list = []

for _ in range(N):
    f = int(sys.stdin.readline())
    f_list.append(f)

f_list.sort()
result = 0
init_length = len(f_list)
while len(f_list) > 0:
    new_f = init_length * min(f_list)

    if new_f >= result:
        result = new_f
    f_list.pop(0)
    init_length -= 1
print(result)