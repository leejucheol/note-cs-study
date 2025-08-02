from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, w = map(int, input().split())
    graph[u].append(w)
    graph[w].append(u)

for i in range(1, n+1):
    graph[i].sort()

visited_dfs = [0] * (n+1)
dfs_order = []
cnt_dfs = 1

def dfs(node):
    global cnt_dfs
    visited_dfs[node] = cnt_dfs
    dfs_order.append(node)
    for nxt in graph[node]:
        if visited_dfs[nxt] == 0:
            cnt_dfs += 1
            dfs(nxt)

def bfs(start):
    visited_bfs = [0] * (n+1)
    bfs_order = []
    cnt_bfs = 1
    queue = deque([start])
    visited_bfs[start] = cnt_bfs
    bfs_order.append(start)
    print(bfs_order)

    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            if visited_bfs[nxt] == 0:
                cnt_bfs += 1
                bfs_order.append(nxt)
                print(bfs_order)
                visited_bfs[nxt] = cnt_bfs
                queue.append(nxt)

    return bfs_order


dfs(v)
for i in range(n):
    print(dfs_order[i], end=' ')

bfs_order = bfs(v)
print(bfs_order)