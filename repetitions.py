dna = list(str(input("")))
n = len(dna)

result = 1
count = 1

for i in range(1,n):

	if  dna[i] == dna[i-1]:
		count+=1
		result = max(result,count)

	elif dna[i] != dna[i-1]:
		result = max(result,count)
		count = 1

print(result)