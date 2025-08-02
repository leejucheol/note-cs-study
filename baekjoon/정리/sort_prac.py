from collections import deque
import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1  # b에 대한 노드의 진입차수 증가

#queue = []
#for i in range(1, n+1):
#    if indegree[i] == 0:
#        heapq.heappush(queue, -i)

#while queue:
#    node = -heapq.heappop(queue)
#    result.append(node)
#    for next_node in graph[node]:
#        indegree[next_node] -= 1
#        if indegree[next_node] == 0:
#            heapq.heappush(queue, -next_node)

#print(result)




queue = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()
    result.append(node)
    for next_node in graph[node]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            queue.append(next_node)

print(*result)