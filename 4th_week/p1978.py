def prime(i):
    if i == 1:
        return False
    elif i < 4:
        return True
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


n = int(input())
l = list(map(int, input().split()))
count = 0
for i in l:
    if prime(i):
        count += 1
print(count)
