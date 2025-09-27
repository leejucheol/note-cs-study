# 문제: There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. 
# You begin the journey with an empty tank at one of the gas stations.
# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, 
# otherwise return -1. If there exists a solution, it is guaranteed to be unique.
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        tank = 0
        start = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start += i + 1
                tank = 0
                return -1
        return start if tank >= 0 else -1
    
# 먼저 전체 주유소의 기름 양이 전체 비용보다 적으면 -1을 반환 > 이유는 전체 주유소를 돌 수 없기 때문
# 그렇지 않으면 탱크는 0이고 시작점도 0으로 설정해서 시작
# 각 주유소를 돌면서 탱크에 기름을 채우고 비용을 빼줌
# 만약 탱크가 0보다 작아지면 시작점을 다음 주유소로 바꾸고 start를 i+1로 설정
# 탱크를 0으로 초기화