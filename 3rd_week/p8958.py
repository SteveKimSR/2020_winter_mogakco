t = int(input())
for _ in range(t):
    case = input()
    total = 0
    count = 0
    for i in case:
        if i == 'O':
            count += 1
            total += count
        else:
            count = 0
    print(total)