from sys import stdin

n = int(input(""))
x = [int(i) for i in stdin.readline().split()]
res = 0
for i in range(1,n):
	if x[i]<x[i-1] :
		res += abs(x[i]-x[i-1])
		x[i]=x[i-1]

		
print(res)