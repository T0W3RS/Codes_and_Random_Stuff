def fibonacci(n):
	#complete the recursive function
	if n<=1:
		return n
	else:
		return (fibonacci(n-1)+fibonacci(n-2))

num = int(input())
if num <=0:
	print("error")
else:
	for i in range(num):
		print (fibonacci(i))
