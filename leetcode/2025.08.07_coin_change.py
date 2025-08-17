#You are given an integer array coins representing coins of different denominations 
# and an integer amount representing a total amount of money.

#Return the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.

#You may assume that you have an infinite number of each kind of coin.

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP 기법 (올바른 방법)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
             for i in range(coin, len(dp)):
                 dp[i] = min(dp[i-coin]+1, dp[i])
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
                                 
                 


        # grid기법 (잘못된 방법)
        #count = 0
        #sorted(coins, reverse= True)
        #if amount == 0:
        #    return 0
        
        #for i in coins:
        #    count += amount // i            
        #    amount -= i * (amount // i)
        #    if amount == 0:
        #        return count
        #return -1


# 접근방법
# 리스트 안에 숫자 파악 --> 이 숫자들의 조합으로 amount값을 생성한다
# 이 부분을 생각........ 조합으로 수 생성 경우의수? 
# 각 경우의 수 (인덱스 기준) 0,1 / 0,2 / 1,2 / 0,1,2 --> 없다면
# 각각 두번씩 더해줌 0,0 / 1,1 / 2,2 / 0,0,1 / 0,0,2 / 1,1,2 / 


#Example 1:

#Input: coins = [1,2,5], amount = 11
#Output: 3
#Explanation: 11 = 5 + 5 + 1
#Example 2:

#Input: coins = [2], amount = 3
#Output: -1
#Example 3:

#Input: coins = [1], amount = 0
#Output: 0

#Constraints:

#1 <= coins.length <= 12
#1 <= coins[i] <= 231 - 1
#0 <= amount <= 104