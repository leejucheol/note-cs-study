#Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
#Since the result may be very large, so you need to return a string instead of an integer.

from typing import List
# 내가 푼 방법
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 먼저 숫자를 배열로 제공 
        # 그 숫자를 string타입으로 변환 후 문자열끼리 더한후 그 값을 비교 한다.
        # 마지막 비교후 가장 큰 값을 반환.
        # 현재 조합한 값이 최고값이여야함 (그리디) 근데 이거를 어떻게 코드로 하는거야...........
        num_str = [str(num) for num in nums]

        for i in range (len(num_str)):
            best = i # 현재 기점에서 제일 큰 수의 인덱스는 i
            for j in range (i+1, len(num_str)):
                if num_str[j] + num_str[best] > num_str[best] + num_str[j]: # best를 j로 하려고 하기때문에 앞자리에 j가 오게된다.
                    best = j # 인덱스 값하고 비교하니 best는 j로 바뀜

            num_str[i], num_str[best] = num_str[best], num_str[i] # i와 best의 값을 바꿔줌
            # 그니까 이 의미가 i자리에 best가 와야하고 그렇게 해야 큰값이 나온다는거지
            
        result = ''.join(num_str) # 배열을 문자열로 합침
        return '0' if result[0] == '0' else result # 0으로 시작하는 경우는 0을 반환


# 문자열 크기비교...주어진 문자열을 0과1을 서로 비교하고 그 둘이 합쳤을경우(0,1 또는 1,0) 확인
# 현재 위치(i)랑 best위치랑 맞바꿈으로써 앞자리에 best값이 와야함

# 이거는 두번째 방안?
#def compare(x,y):
#    if x + y > y + x:
#        return -1
#    elif x + y > y + x:
#        return 1
#    else:
#        return 0

# 위 함수를 사용해서 비교 함수 실행

    
#num_str = ["3","30","39","34","5","9"]
#num_str.sort(key=cmp_to_key(compare))

# 최적의 시간 (답) 

#  list_nums = list(map(str, nums)) # map함수 사용해서 문자열로 변환
#  list_nums.sort(key = lambda x : x * 1000, reverse=True) # 이부분을 잘 모르겠는데 내림차순으로 정렬하는거고 lambda가 뭐를 의미하는지..?
#  return '0' if list_nums[0] == '0' else "".join(list_nums) # 인덱스 값이 0일경우 0을 출력

# Example 1:

# Input: nums = [10,2]
# Output: "210"