def recursive_pow(x,n):
	if n%2==0 and n>0:
		return recursive_pow(x**2,n/2)
	elif n%2==1:
		return x*recursive_pow(x,n-1)
	else:
		return 1
