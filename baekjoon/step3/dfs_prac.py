# DFS (깊이 우선 탐색) 구현
n,m,r = map(int, input().split())
graph = [[] for _ in range(n + 1)] # 인접 리스트: 각 정점마다 연결된 점 저장

for i in range(m):
	u,v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u) # 양방향

for i in range(1,n+1):
	graph[i].sort() # 정점 오름차순 작은 번호 부터 방문

visited = [0] * (n+1)
cnt = 1 # 첫방문은 1번부터 시작

stack = [r] # 시작 정점 r을 스택에 넣음
while stack:
    node = stack.pop()
    if visited[node] == 0:
        visited[node] = count
        count += 1
        for next_node in graph[node]:
            if visited[next_node] == 0:  # 방문하지 않은 정점만 스택에 추가
                stack.append(next_node)

for i in range(1, n+1):
    print(visited[i])   # 정점 번호 i의 방문 순서 출력

# 재귀함수
# DFS (깊이 우선 탐색) 구현
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline # 시간초과 원인 제거 (input은 너무 느려서 위 라이브러리 stdin 객체의 메서드로 바꿔야함)

n,m,r = map(int, input().split())
graph = [[] for _ in range(n + 1)] # 인접 리스트: 각 정점마다 연결된 점 저장

for i in range(m):
	u,v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u) # 양방향

for i in range(1,n+1):
	graph[i].sort() # 정점 오름차순 작은 번호 부터 방문

visited = [0] * (n+1)
cnt = 1 # 첫방문은 1번부터 시작

def dfs(node):
	global cnt
	visited[node] = cnt # 방문 순서 기록
	for next_node in graph[node]:
		if visited[next_node] == 0:
			cnt +=1
			dfs(next_node)
dfs(r)
for i in range(1, n+1):
    print(visited[i])   # 정점 번호 i의 방문 순서 출력
