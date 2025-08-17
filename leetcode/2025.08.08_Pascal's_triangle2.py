from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1] * (i + 1) for i in range(rowIndex + 1)]

        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

        return dp[rowIndex]

s = Solution()
n = int(input("rowIndex를 입력하세요: "))
print(s.getRow(n))


# 먼저 이차원 배열이라는 것을 생각해야한다
# dp로 이차원 배열을 만드는데 값은 1로 초기화한다
# 첫 번째 전체 삼각형을 채우는 코드를 참조하고 특정 인덱스 값만 구한다
# 기준은 입력하는 rowIndex를 기준으로 반복문을 수정한다 (그 특정 인덱스가 마지막 부분이다)
# 각 행에 가운데는 전 행(i-1)에서 전 열(j-1)을 통해서 구한다 이 부분은 똑같이 진행한다
# 특정 행의 값만 출력하기 위해서는 dp[rowIndex]를 통해서 그 부분 값만 리턴하면 된다.