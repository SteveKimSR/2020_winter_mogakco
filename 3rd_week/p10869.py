a, b = map(int, input().split())
l = [a + b, a - b, a * b, a // b, a % b]
print('\n'.join(map(str, l)))