i=0
listOfNums=[]
order=['first','second','third','fourth']
while(i<4):
	num=input('Please input the %s number: '%order[i])
	try:
		num = float(num)
		listOfNums += [num]
	except ValueError:
		print('Your input is not a number!')
		i -= 1
	i += 1
listOfNums.sort()
print('The second smallest number is: ' +str(listOfNums[1]))
print("Program Ends...")