from sys import stdin

a = int(input(""))
c = {int(i) for i in stdin.readline().split()}
S = int((a+1)/2 *a)
x = S - sum(c)
print(x)