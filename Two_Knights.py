n = int(input())
for i in range(1,n+1):
	a1 = i*i #board size
	a2 = a1*(a1-1)/2 #all possibilities of placement 2 knights
	if i>2:
		a2 -=  (4*(i-1)*(i-2))
	print(a2)