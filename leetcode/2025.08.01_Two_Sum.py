class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        a = len(nums)
        for i in range (a-1):
            for j in range (i+1, a):
                if nums[i] + nums[j] == target:
                    return i,j