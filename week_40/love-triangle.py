# https://codeforces.com/gym/403303/problem/C

from collections import defaultdict

n = int(input())
pln = [0] + [int(n) for n in input().split()]

graph = defaultdict(int)
for i, p in enumerate(pln[1:]):
    graph[i+1] = p

f = False
for i in range(1, n + 1):
    if graph[graph[graph[i]]] == i:
        f = True
        break

print('YES' if f else 'NO')
