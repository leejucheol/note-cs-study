from typing import List 

height = [1,8,6,2,5,4,8,3,7]
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        width = right - left # 굳이 변수로 선언할 필요는 없음 while 안에서 계속 갱신됨
        maxA = 0
        while left < right: # left와 right가 같아지면 넓이는 0이 됨, index값으로 비교, 이후 너비 계산
            width = right - left # 너비 갱신, 제일 넓은 너비를 구하는 것이 목적
            minHeight = min(height[left], height[right]) # 높이는 더 낮은 쪽이 기준
            maxA = max(maxA, minHeight*width) # 여기서 시간 복잡도를 줄이는 방식은 temp를 사용하여 max를 갱신
            if height[left] < height[right]: # 더 높은 쪽으로 이동해야 넓이가 커질 가능성이 있음 그래서 더 낮은 쪽을 이동
                left += 1
            else:
                right -= 1
            
            # maxA = max(maxA, min(height[left], height[right])*width)
            #temp = min(height[left], height[right])*width
            #if temp > maxA:
            #    maxA = temp
            # 위와 같이 temp를 사용하여 max를 갱신하는 방법도 있음
            
        
# dp로 시도해보려 했으나 실패 적절한 방법이 아니었음

        # maxA = 0

        # for i in range(len(height)-1):
        #     for j in range(i+1, len(height)):
        #         minHeight = min(height[i], height[j])
        #         wide = j-i

        #         maxA = max(maxA, minHeight*wide)
        #         # if(maxA < minHeight*wide):
        #         #     maxA = minHeight*wide

        return maxA


s = Solution()
n = list(map(int, input("height 리스트를 입력하세요: ").split()))