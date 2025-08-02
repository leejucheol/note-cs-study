import sys
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sum = 0 
        ans = float("-inf")

        for i in nums:
            sum += i  # sum 값을 갱신을 하면서 비교해야함
            if sum > ans:
                ans = sum
            if sum < 0:
                sum = 0
        return ans