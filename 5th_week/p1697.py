from collections import deque


def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= maximum and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)


n, k = map(int, input().split())
maximum = 10 ** 5
dist = [0] * (maximum + 1)
bfs()
