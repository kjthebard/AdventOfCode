myfile = open('/Users/kieran/PycharmProjects/adventofcode_day1/data.txt', 'r')
contents = myfile.read().strip().split() ## Reads file correctly, this is easy with pandas but I wanted to not use pandas
myfile.close()

def solve():
    ans = 0
    old = set([ans])   

    found = False
    iter = 0
    while not found:

        for i in contents:
            if i[0] == '-':
                ans -= int(i[1:])
            elif i[0] == '+':
                ans += int(i[1:])

            if ans in old:
                print("Part Two:", ans)
                found = True
                break

            old.add(ans)

        if iter == 0:
            print("Part One:", ans)

        iter += 1

solve()
