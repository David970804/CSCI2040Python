units=['I','V']
tens=['X','L']
hundreds=['C','D']
thousands=['M']
digit=[units,tens,hundreds,thousands]

def roman_number(n):
	num_of_digits=0
	n_digits = []
	roman_num=""
	if n<=0 or n>9999:
		return 'Number is out of range'
	while n>0:
		n_digits.append(n%10)
		n = n//10
#for each digit of a number, the conversion logic is the same
#split four different cases: <4 =4 <9 =9
#and create the list "digit" to store sequentially the corresponding 
#roman number digit representation so that it is easier to refer to in this for loop
	for i in range(len(n_digits)):
		if i < 3:
			if n_digits[i]<4:
				roman_num = n_digits[i]*digit[i][0] + roman_num
			elif n_digits[i]==4:
				roman_num = digit[i][0]+digit[i][1]+roman_num
			elif n_digits[i]<9:
				roman_num = digit[i][1]+(n_digits[i]-5)*digit[i][0]+roman_num
			elif n_digits[i]==9:
				roman_num = digit[i][0]+digit[i+1][0]+roman_num
		else:
			roman_num = digit[i][0]*n_digits[i] + roman_num
	return roman_num

