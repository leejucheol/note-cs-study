# 1000번 문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
A, B = map(int, input().split())

print(A + B)

# 1001번 문제 : 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
A, B = map(int, input().split())

print(A - B)

# 10998번 문제 : 두 정수 A와 B를 입력받은 다음, A*B를 출력하는 프로그램을 작성하시오.

# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
A, B = map(int, input().split())

print(A * B)

# 1008번 문제 : 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.
A, B = map(int, input().split())

print(A / B)

# 10869번 문제 : 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
A, B = map(int, input().split())

# 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
print(A + B)  # A+B
print(A - B)  # A-B
print(A * B)  # A*B
print(A / B)  # A/B (몫)
print(A % B)  # A%B (나머지)