from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1] * (i+1) for i in range(numRows)]
        
        for i in range (2,numRows):
            for j in range(1,i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        
        return dp


# 먼저 이차원 배열이라는 것을 생각해야한다
# dp로 이차원 배열을 만드는데 값은 1로 초기화한다
# 이제 이 배열을 어떻게 채울지 생각을 하는데 이 부분이 나에게는 어려웠다
# 점화식을 구해서 작성해야하는데 이는 직접 그려보면서 진행했다
# 각 행에 가운데는 전 행(i-1)에서 전 열(j-1)을 통해서 구한다
# 전체 파스칼 삼각형을 출력하기 위해 dp 전체를 리턴한다
