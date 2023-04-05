import sys

N = int(sys.stdin.readline())

alphabets = set()
score_list = []
total_score_list = []

for _ in range(N):
    word = sys.stdin.readline().rstrip()

    for i, w in enumerate(word):
        score = 10 ** (len(word) - i - 1)
        score_list.append((w, score))
        alphabets.update(w)

alphabets = list(alphabets)
total_score_dict = dict()

for a in alphabets:
    total_score_dict[a] = 0

for a in alphabets:
    for w, score in score_list:
        if a == w:
            total_score_dict[a] += score

items = list(total_score_dict.items())
items.sort(key= lambda x: x[1])
items.reverse()

result = 0
for i in range(len(items)):
     result += (9-i) * items[i][1]

print(result)