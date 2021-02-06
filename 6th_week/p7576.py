import sys

m, n = map(int, sys.stdin.readline().split())
box = []
ripe = []
for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    box.append(line)
    for j in range(m):
        if line[j] == 1:
            ripe.append([i, j])

temp = ripe.copy()
day = 0
while True:
    if len(temp):
        temp2 = []
        for x, y in temp:
            neighbor = [[x + 1, y], [x, y + 1], [x - 1, y], [x, y - 1]]
            for z, w in neighbor:
                if -1 < z < n and -1 < w < m and box[z][w] == 0:
                    temp2.append([z, w])
                    box[z][w] = 1
        temp = temp2.copy()
        day += 1
    else:
        break
flag = True
for i in box:
    if i.count(0):
        flag = False
print(day-1 if flag else -1)