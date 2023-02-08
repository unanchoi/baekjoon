import sys

L = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()

alphabet_dict = {chr(97 + i): i+1 for i in range(26)}

s = 0
i = 0
for char in list(string):
    s += alphabet_dict[char] * (31 ** i)
    i += 1

print(s % 1234567891)