case = int(input())
for _ in range(case):
    r, s = input().split()
    word = ''
    for w in s: word += w*int(r)
    print(word)