a, b = map(int, input().split())
if a == b:
    print('==')
elif a > b:
    c = '>'
else:
    c = '<'
print(c)
