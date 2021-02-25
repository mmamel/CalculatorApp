def fib(n):
	seq = []
	curr = 0
	if (n>0):
		seq.append(0)
	if(n>1):
		seq.append(1)
	for i in range(2, n):
		new = seq[i-2] + seq[i-1]
		seq.append(new)
	return seq

def fact(n):
	if n == 0:
		return 1
	else:
		return n*fact(n-1)