#cnt1 = 0
#cnt2 = 0 

n = int(input())

#def fib(n):
#    global cnt1
#    if (n == 1 or n == 2):
#        cnt1 += 1
#        return 1
#    else: return (fib(n - 1) + fib(n - 2))

#def fibonacci(n):
#    global cnt2
#    f = [0] * (n + 1)
#    f[1] = f[2] = 1
#    for i in range (3, n+1):
#        f[i] = f[i - 1] + f[i - 2]
#        cnt2 += 1
#    return cnt2

#fib(n)
#fibonacci(n)

#print(cnt1,cnt2)

def fib_count(n):
	#if (n ==1 or n ==2):
	#	return 1
	#else: return (fib_count(n-1) + fib_count(n-2)) # 이거는 재귀함수로 시간복잡도가 O(2^n)으로 매우 비효율적임
	f = [0]* (n+1) # 괄호 필수!!!!
	f[1] = f[2] = 1
	for i in range(3,n+1):
		f[i] = f[n-1] + f[n-2]
	return f[n] # O(n)으로 시간복잡도 개선됨 더 효율적임

def fibo_cot(n):
	return n-2

print(fib_count(n), fibo_cot(n))