# 재귀함수
# DFS (깊이 우선 탐색) 구현
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline # 시간초과 원인 제거 (input은 너무 느려서 위 라이브러리 stdin 객체의 메서드로 바꿔야함)

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

def dfs(node):
	global cnt 
	visited[node] = cnt
	for next_node in graph[node]:
		if visited[next_node] == 0:
			cnt+=1
			dfs(next_node)

dfs(r)
for i in range (1, n+1):
	print(visited[i])

