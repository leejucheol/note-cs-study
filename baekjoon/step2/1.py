# 1330번 문제 : 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다. (-10,000 ≤ A, B ≤ 10,000)

a,b = map(int, input().split())

if( a > b ):
    print(">")
elif( a < b ):
    print("<")
elif( a == b ):
    print("==")