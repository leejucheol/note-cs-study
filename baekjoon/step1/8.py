# 10430 문제 : (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 A, B, C가 주어진다. (2 ≤ A, B, C ≤ 10000)
a,b,c = map(int, input().split())

x = (a + b) % c
y = ((a%c) + (b%c)) % c 
z= ((a * b)) % c
w = ((a%c) * (b%c)) % c

print(x)
print(y)
print(z)
print(w)