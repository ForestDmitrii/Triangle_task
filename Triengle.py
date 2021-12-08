line = []
for i in range(1,51):
    line.append(i)
line.reverse()
a, b, c = 0, 0, 0
def s(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** (1/2)
    return 0


for i in range(len(line)):
    a = line[i]
    b = line[i + 1]
    c = line[i + 2]
    if s(a, b, c) != 0:
        print(s(a, b, c))
        print(a, b, c)
        break