from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # star graph의 중심은 모든 간선에 연결된 노드가 된다
        # 두 간선에서 공통된 노드가 중심 노드가 된다.
        a,b = edges[0]
        
        if a in edges[1]:
            return a
        return b
    
    # 왜 이런 생각이 안났을까
    # 모든 간선을 탐색할 필요가 없다
    # 첫 번째 간선의 두 노드 중 하나가 중심 노드가 된다 즉, 하나의 간선과 다른 하나의 간선으로 비교해서 공통된 노드를 찾으면 된다