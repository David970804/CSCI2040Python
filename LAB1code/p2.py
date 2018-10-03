while(True):
	n=int(input('Enter an integer: '))
	if n == -1:
		break
	str= input('Enter a string: ')
	for i in range(1,n+1):
		print((str+' ')*i)
print('Program ends.')
