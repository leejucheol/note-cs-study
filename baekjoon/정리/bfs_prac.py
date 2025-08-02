from collections import deque

n,m,r = map(int, input().split())
graph = [[] for _ in range (n+1)]

for i in range (m):
	u,v = map(int,input().split())
	graph[u].append(v)
	graph[v].append(u)

for i in range(1, n+1):
	graph[i].sort()

visited = [0] * (n+1)
cnt = 1

def bfs(start):
	global cnt
	queue = deque([start])
	visited[start] = cnt
	cnt += 1
	
	while queue:
		node = queue.popleft()
		for next_node in graph[node]:
			if visited[next_node] == 0:
				visited[next_node] = cnt
				cnt +=1
				queue.append(next_node)

bfs(r)

for i in range (1, n+1):
	print(visited[i])

