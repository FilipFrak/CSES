from sys import stdin
def board(size,x,y):
	array = dict()

	for i in range(1,(size+1)**2):
		array[f'{i}'] = f'{i,i}'

	return  dict((v,k) for k,v in array.iteritems())[x,y]
#t = int(input(''))
t=3
#x_y = list()
x_y = [[2,3],[1,1],[4,2]]
for i in range(0,t):
	#x_y.append(input('').split(' '))
	x,y = x_y[i]


print(x,y)

array = [1,1]
print(board(3))
array = list()
for y in range(1,max(x,y)+1):
	for x in range(1,max(x,y)+1):
		