import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    a = int (sys.stdin.readline().rstrip()) #한줄에 하나 strip기능 공백 및 줄바꿈 제거
    b = int(sys.stdin.readline().rstrip())
    c = a+b
    print(c)
    


#t = int(input())

#for i in range(t):
#    a,b = map(int, input().split()) 
#    c = a+b
#    print(c)
    