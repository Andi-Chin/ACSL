def doStuff():
	number = input("number please:\n")
	n = int(input('n please:\n'))
	lis = []
	for i in range(0, len(number), n):
		sli	= number[i:i+n]
		lis.append(sli)
	difference = (n-len(lis[-1]))
	lis = [int(i) for i in lis]
	lis[-1] *= 10 ** difference

	print(sum(lis))

for i in range(5):
	doStuff()