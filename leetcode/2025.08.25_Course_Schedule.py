#There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
#For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
#Return true if you can finish all courses. Otherwise, return false.

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 각 노드의 진입차수를 저장할 리스트
        degree = [0] * numCourses
        # 각 노드의 인접 리스트를 저장할 리스트
        graph = [[] for _ in range(numCourses)]
        # 위상 정렬을 위한 큐
        queue = []
        # 모든 노드의 진입차수와 인접 리스트를 초기화
        for course, prereq in prerequisites:
            degree[course] += 1
            graph[prereq].append(course)

        # 진입차수가 0인 노드를 큐에 추가
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)

        # 큐가 빌 때까지 반복
        while queue:
            node = queue.pop(0)
            numCourses -= 1
            for neighbor in graph[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    queue.append(neighbor)


## 두번째 풀이

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 과목수만큼 배열을 만들고 진입차수..선수과목을 이수해야 다음과목을 들을수있음

        pre = [[] for _ in range(numCourses)]

        for course, p in prerequisites:
            pre[course].append(p)

        visited = set()

        def dfs(course):
            if not pre[course]:
                return True

            if course in visited:
                return False
            
            visited.add(course)

            for p in pre[course]:
                if not dfs(p): return False

            pre[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True




