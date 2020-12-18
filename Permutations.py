n = int(input(''))
#n=4
n_i =[i for i in range(1,n+1)]
a = [i for i in range(1,n+1) if n_i[i-1]%2 ==0]
b = [i for i in range(1,n+1) if n_i[i-1]%2 !=0]

c = a + b
for i in range(1,n):
	
	if abs(c[i]-c[i-1]) == 1:

		print('NO SOLUTION')
		break
	elif len(c) <0 :
		print('NO SOLUTION')
		break
	else:
		print(*c)
		break

if n == 1:
	print(1)