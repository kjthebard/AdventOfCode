myfile = open('/Users/kieran/PycharmProjects/adventofcode_day1/data2.txt', 'r')
from collections import Counter

contents = myfile.read().strip().splitlines()
myfile.close()

c = [0, 0]
for i in contents:
    a = [j for i,j in Counter(i).most_common()]
    if 3 in a:
        c[0] += 1
    if 2 in a:
        c[1] += 1



print(c[1] * c[0]) ## This is answer to part one.

for i in contents:
        for j in contents:
            diffs = 0
            for idx, ch in enumerate(i):
                if ch != j[idx]:
                    diffs += 1
            if diffs == 1:
                ans = [ch for idx, ch in enumerate(i) if j[idx] == ch]
                print("Part Two Answer:", ''.join(ans))
