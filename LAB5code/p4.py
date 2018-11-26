import numpy as np

def get_average_grades(file='grades.csv'):
	denomenator = []
	grades_list = []
	with open(file) as file:
		for grades in file:
			grades = [float(x) for x in grades.split(',')]
			grades_list.append([x  if x >=0 else np.NaN for x in grades])
	file.close()
	return list(np.nanmean(grades_list,axis=0))

#print(get_average_grades())	