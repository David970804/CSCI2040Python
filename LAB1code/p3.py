#from getpass import getpass
totalGrade = 0
totalUnit = 0
while(True):
	gradeAndUnits = input()
	if ' ' in gradeAndUnits:
		grade,unit = [float(x) for x in gradeAndUnits.split()]
		if grade <0:
			print('Wrong input !')
		else:
			totalGrade += grade*unit
			totalUnit += unit
			print('Current GPA: %.2f'%(totalGrade/totalUnit))
	else:
		if float(gradeAndUnits)==-1:
			print('Program ends.')
			break
		else:
			print('Wrong input!')
